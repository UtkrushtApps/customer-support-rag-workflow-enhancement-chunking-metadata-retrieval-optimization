import chromadb
from vector_db_client import get_chroma_client
from rag_chunking.py import process_and_embed_articles
from config import COLLECTION_NAME, VECTOR_DIM

# Initialize Chroma and populate with embedded chunks

def initialize_vector_db():
    client = get_chroma_client()
    if COLLECTION_NAME in [c['name'] for c in client.list_collections()]:
        client.delete_collection(COLLECTION_NAME)
    collection = client.create_collection(COLLECTION_NAME)
    chunks, embeddings = process_and_embed_articles()
    # TODO: Add chunks and their embeddings to Chroma with metadata
    # collection.add(...)
    print(f"Initialized '{COLLECTION_NAME}' collection with processed support chunks.")

if __name__ == "__main__":
    initialize_vector_db()
