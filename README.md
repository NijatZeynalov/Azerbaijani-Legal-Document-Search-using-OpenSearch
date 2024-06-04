# Azerbaijani Legal Document Search using OpenSearch

This project demonstrates how to use OpenSearch with k-NN (K-Nearest Neighbors) search to perform semantic searches on Azerbaijani legal documents, specifically the "AZƏRBAYCAN RESPUBLİKASININ ƏMƏK MƏCƏLLƏSİ". The project uses the opensearch-py library for interacting with the OpenSearch cluster and the sentence-transformers library for generating text embeddings.


## Introduction
Finding relevant legal documents is crucial for research and legal practice. Traditional keyword searches can be limited in their ability to retrieve relevant documents, especially when dealing with large datasets. This project leverages OpenSearch's k-NN search algorithm for semantic search, allowing for more accurate and context-aware document retrieval.

## Features
Semantic Search: Uses k-NN to perform semantic searches on legal documents.
Text Embeddings: Utilizes Sentence Transformers to generate embeddings for legal text.
OpenSearch Integration: Interacts with OpenSearch using the opensearch-py library.
Setup
Prerequisites
Docker
Python 3.8 or higher
