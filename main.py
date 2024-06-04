import json
from opensearchpy import OpenSearch, helpers
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# Load legal documents from data.json
with open('data.json', 'r', encoding='utf-8') as f:
    legal_docs = json.load(f)

INDEX_NAME = "azerbaijani_legal_docs"

client = OpenSearch(
    hosts=["http://localhost:9200/"]
)

settings = {
    "settings": {
        "index": {
            "knn": True,
        }
    },
    "mappings": {
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "text"},
            "content": {"type": "text"},
            "embedding": {
                "type": "knn_vector",
                "dimension": 384,
            },
        }
    },
}

res = client.indices.create(index=INDEX_NAME, body=settings, ignore=[400])
print(res)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

for doc in tqdm(legal_docs, total=len(legal_docs)):
    embedding = model.encode(f"{doc['title']} {doc['content']}")
    doc["embedding"] = embedding

    try:
        client.index(index=INDEX_NAME, body=doc)
    except Exception as e:
        print(f"Error indexing document {doc['id']}: {e}")

print("Finished uploading indexes for legal documents!")
