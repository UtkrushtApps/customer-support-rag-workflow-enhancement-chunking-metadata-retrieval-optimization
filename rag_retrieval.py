from vector_db_client import get_chroma_client
from config import COLLECTION_NAME, K

# Placeholder: expects user query string
# Returns list of (chunk, metadata, similarity_score)
def retrieve_relevant_chunks(query, top_k=K):
    client = get_chroma_client()
    collection = client.get_collection(COLLECTION_NAME)
    # TODO: Encode query, perform cosine similarity search, return top_k chunks with metadata
    results = []  # incomplete
    return results

if __name__ == "__main__":
    query = "How do I reset my account password?"
    results = retrieve_relevant_chunks(query)
    for ch in results:
        print(ch)
