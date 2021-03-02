# Milvus_Sentence_Transformer
Milvus (https://milvus.io/) is a vector similarity search engine that is highly flexible, reliable, and blazing fast. It supports adding, deleting, updating, and near-real-time search of vectors on a scale of trillion bytes.

This project provides a tutorial of setting up the Milvus in the Ubuntu VM through VirtualBox, and uses a toy example to demonstrate how to integrate pre-trained sentence transformer model with Milvus for text-based vector similarity search.

Steps of setting Milvus in Ubuntu VM:
1. Download and install VirtualBox (https://www.virtualbox.org/wiki/Downloads)
2. Download Ubuntu iso image (https://ubuntu.com/download)
3. Create Ubuntu VM with 6G memory and 20 GB storage (Note: it is important to allocate enough memory and storage to properly run Mivuls and Sentence Transformer Models)
4. Install docker in Ubuntu VM:
    1. sudo apt-get update 
    2. sudo apt install docker.io
    3. sudo snap install docker
    4. sudo docker —version
    5. sudo docker run hello-world
5. Install python in Ubuntu VM: sudo apt-get install python3.5
6. Install Miluvus: https://milvus.io/docs/v0.10.6/milvus_docker-cpu.md
7. Run example: https://milvus.io/docs/v0.10.6/example_code.md
8. Install pip3: sudo apt-get -y install python3-pip
10. Install Sentencetransfomer: pip3 install -U sentence-transformers
11. Run the given example in the reporsitory:
    1. Parameter setting:
      1. index_data: contains text data for creating the Milvus data collection
      2. query_data: use the text in the file to make the query
      3. pretrained_sentence_transformer_model: the name of pretrained sentence transformer model for text embedding
      4. dim: the dimension of embedding
    2. python3 milvus_sentence_transformer.py --index_data './data/index_data' --query_data './data/query_data' --pretrained_sentence_transformer_model 'paraphrase-distilroberta-base-v1' --dim 768
    3. Return: the search results for given queries

Return example:

 [[-0.01361994 -0.26041457 -0.14991447 ...  0.08899624 -0.03414515
   0.20742574]
 [-0.01017451 -0.10114314 -0.11551546 ...  0.11610635 -0.23206173
   0.12250963]
 [ 0.18402587  0.10305503  0.10840097 ... -0.1451152  -0.32262647
  -0.16831118]
 ...
 [ 0.23727262  0.22600946  0.06773458 ... -0.02185502  0.14735295
  -0.09761411]
 [ 0.11854181  0.16509262  0.15550615 ...  0.55348754  0.16981289
  -0.40636525]
 [-0.10381754  0.27720377 -0.1110699  ...  0.46858153 -0.1193108
  -0.04110763]]
[1614665243304677000, 1614665243304677001, 1614665243304677002, 1614665243304677003, 1614665243304677004, 1614665243304677005, 1614665243304677006, 1614665243304677007, 1614665243304677008, 1614665243304677009, 1614665243304677010, 1614665243304677011]
1614665243304677000 A man is eating food.
1614665243304677001 A man is eating a piece of bread.
1614665243304677002 The girl is carrying a baby.
1614665243304677003 A man is riding a horse.
1614665243304677004 A woman is playing violin.
1614665243304677005 Two men pushed carts through the woods.
1614665243304677006 A man is riding a white horse on an enclosed ground.
1614665243304677007 A monkey is playing drums.
1614665243304677008 Someone in a gorilla costume is playing a set of drums.
1614665243304677009 It is a beautiful day in the neighborhood
1614665243304677010 Do you like hiking?
1614665243304677011 I have a green bike at home.
{'partitions': [{'row_count': 12, 'segments': [{'data_size': 36960, 'index_name': 'IDMAP', 'name': '1614665243310564000', 'row_count': 12}], 'tag': '_default'}], 'row_count': 12}
Creating index: {'nlist': 2048}
(collection_name='example_collection_', index_type=<IndexType: IVFLAT>, params={'nlist': 2048})
Searching ... 
Query result is correct
id:1614665243304677000, text:A man is eating food., distance: 31.884197235107422
id:1614665243304677007, text:A monkey is playing drums., distance: 43.76609420776367
id:1614665243304677003, text:A man is riding a horse., distance: 20.04574966430664
