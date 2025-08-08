import chromadb
from config import CHROMA_HOST, CHROMA_PORT

def get_chroma_client():
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    return client
