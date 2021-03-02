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
    2. python3 example.py --index_data './data/index_data' --query_data './data/query_data' --pretrained_sentence_transformer_model 'paraphrase-distilroberta-base-v1'
    3. Return: the search results for given queries
