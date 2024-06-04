from sentence_transformers import SentenceTransformer
from opensearchpy import OpenSearch
from pprint import pprint

INDEX_NAME = "azerbaijani_legal_docs"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = OpenSearch(
    hosts=["http://localhost:9200/"]
)

text = input("What are you looking for? ")
embedded_search = model.encode(text)

query = {
    "size": 2,
    "query": {"knn": {"embedding": {"vector": embedded_search, "k": 2}}},
    "_source": False,
    "fields": ["title", "content"],
}

response = client.search(body=query, index=INDEX_NAME)
pprint(response["hits"]["hits"])
