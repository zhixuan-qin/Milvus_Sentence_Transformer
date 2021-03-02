import random
import numpy as np
import argparse

from milvus import Milvus, IndexType, MetricType, Status
from sentence_transformers import SentenceTransformer


# Milvus server IP address and port.
# You may need to change _HOST and _PORT accordingly.
_HOST = '127.0.0.1'
_PORT = '19530'  # default value
# _PORT = '19121'  # default http value
_INDEX_FILE_SIZE = 32  # max file size of stored index


def text2vec(sentences):
    # Encode all sentences
    embeddings = model.encode(sentences)
    return embeddings


def main():
    # Specify server addr when create milvus client instance
    # milvus client instance maintain a connection pool, param
    # `pool_size` specify the max connection num.
    milvus = Milvus(_HOST, _PORT)

    # Create collection demo_collection if it dosen't exist.
    collection_name = 'example_collection_'

    status, ok = milvus.has_collection(collection_name)
    if not ok:
        param = {
            'collection_name': collection_name,
            'dimension': _DIM,
            'index_file_size': _INDEX_FILE_SIZE,  # optional
            'metric_type': MetricType.L2  # optional
        }

        milvus.create_collection(param)

    # Show collections in Milvus server
    _, collections = milvus.list_collections()

    # Describe demo_collection
    _, collection = milvus.get_collection_info(collection_name)
    print(collection)

    # element per dimension is float32 type
    # vectors should be a 2-D array
    vectors = text2vec(index_sentences)
    print(vectors)

    # Insert vectors into demo_collection, return status and vectors id list
    status, ids = milvus.insert(collection_name=collection_name, records=vectors)
    if not status.OK():
        print("Insert failed: {}".format(status))
    else:
        print(ids)
    #create a quick lookup table to easily access the indexed text/sentences given the ids
    look_up={}
    for ID, sentences in zip(ids, index_sentences):
        look_up[ID]=sentences

    for k in look_up:
        print(k, look_up[k])


    # Flush collection  inserted data to disk.
    milvus.flush([collection_name])
    # Get demo_collection row count
    status, result = milvus.count_entities(collection_name)

    # present collection statistics info
    _, info = milvus.get_collection_stats(collection_name)
    print(info)

    # Obtain raw vectors by providing vector ids
    status, result_vectors = milvus.get_entity_by_id(collection_name, ids)

    # create index of vectors, search more rapidly
    index_param = {
        'nlist': 2048
    }

    # Create ivflat index in demo_collection
    # You can search vectors without creating index. however, Creating index help to
    # search faster
    print("Creating index: {}".format(index_param))
    status = milvus.create_index(collection_name, IndexType.IVF_FLAT, index_param)

    # describe index, get information of index
    status, index = milvus.get_index_info(collection_name)
    print(index)


    # Use the query sentences for similarity search
    query_vectors = text2vec(query_sentences)

    # execute vector similarity search
    search_param = {
        "nprobe": 16
    }

    print("Searching ... ")

    param = {
        'collection_name': collection_name,
        'query_records': query_vectors,
        'top_k': 1,
        'params': search_param,
    }

    status, results = milvus.search(**param)
    if status.OK():
        # indicate search result
        # also use by:
        #   `results.distance_array[0][0] == 0.0 or results.id_array[0][0] == ids[0]`
        if results[0][0].distance == 0.0 or results[0][0].id == ids[0]:
            print('Query result is correct')
        else:
            print('Query result isn\'t correct')

        # print results
        for res in results:
            for ele in res:
                print('id:{}, text:{}, distance: {}'. format(ele.id, look_up[ele.id], ele.distance))

    else:
        print("Search failed. ", status)

    # Delete demo_collection
    status = milvus.drop_collection(collection_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--index_data", help="the path of the file containing data to be indexed",
                        default='./data/index_data')
    parser.add_argument("--query_data", help="the path of the file containing query data",
                        default='./data/query_data')
    parser.add_argument("--pretrained_sentence_transformer_model", help="the pretrained model name",
                        default='paraphrase-distilroberta-base-v1')
    parser.add_argument("--dim", help="the dimension of embedding",
                        default=768, type=int)
    args = parser.parse_args()
    model = SentenceTransformer(args.pretrained_sentence_transformer_model)
    # Index those sentences to milvus for query
    index_sentences = [line for line in open(args.index_data, 'r')]
    # sentences are used to generate query vector
    query_sentences = [line for line in open(args.query_data, 'r')]
    # Vector parameters
    _DIM = args.dim  # dimension of vector
    main()
