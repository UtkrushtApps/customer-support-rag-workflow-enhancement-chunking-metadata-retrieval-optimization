# Task Overview
Your company manages a customer support search assistant utilizing RAG: a Chroma vector database contains 8,000 pre-ingested support articles. However, retrieval quality is poor due to large, unoverlapped text chunks and missing metadata, leading to generic or irrelevant answers. You are to enhance chunking, metadata, retrieval, and generation logic so customer queries receive accurate, context-rich responses from the support corpus.

## Guidance
- Current document chunks are too large (2000 tokens) and lack overlap or metadata, which hinders retrieval granularity.
- Cosine similarity retrieval isn't optimized for k=5 or for fast top-k document selection.
- Metadata fields (category, priority, last_updated_date) are missing from chunks; these should be included and used in filtering or reranking if possible.
- The LLM generation script is incomplete, so query responses are not context-specific or properly substantiated.
- Your infrastructure, Chroma DB setup, and embedding model are all pre-configured; focus on the Python pipeline changes needed.

## Database Access
- Vector database: Chroma, URL: http://<DROPLET_IP>:8000
- Collection: support_articles
- Number of pre-embedded articles: 8000
- Embedding dimension: 384 (sentence-transformers)
- Chroma Python client is provided; data files for support docs are in ./vector_data/
- Validate your final Chroma population and chunking via collection.count() in the vector_db_client.py utilities.

## Objectives
- Implement 500-token chunking of articles, with 200-token overlap between chunks.
- Attach metadata (category, priority, last_updated_date) for each chunk.
- Generate embeddings using sentence-transformers (already in requirements.txt).
- Store all chunk embeddings and metadata in Chroma.
- Implement fast, top-5 cosine similarity retrieval for input queries, returning chunk content and metadata.
- Wire a basic LLM generation pipeline that produces contextually relevant answers using retrieved support chunks.

## How to Verify
- Use provided test queries (sample_queries.txt) to run end-to-end retrieval and answer generation.
- Confirm retrieved chunks are granular, relevant, and carry appropriate metadata in results.
- Output answers that are accurate, cite the specific support document context, and resolve the customer’s question.
- Manual spot-check retrieval accuracy, and observe substantial improvement over initial configuration (large, unoverlapped chunks with poor relevance).
