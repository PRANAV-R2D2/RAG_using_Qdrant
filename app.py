from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceBgeEmbeddings
from qdrant_client import QdrantClient

# Load the embedding model
model_name = "BAAI/bge-large-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}

embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# Connect to the Qdrant server
url = "http://localhost:6333"
client = QdrantClient(url=url, prefer_grpc=False)

print(client)

# Load the vector database
db = Qdrant(client=client, embeddings=embeddings, collection_name="vector_db")

print(db)

# Perform a similarity search
query = "what is generally illegal"
docs = db.similarity_search_with_score(query=query, k=5)

for i in docs:
    doc, score = i
    print({"score": score, "content": doc.page_content, "metadata": doc.metadata})
