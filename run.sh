#!/bin/bash
set -e

echo "Starting Chroma vector database..."
docker-compose up -d

# Wait for Chroma DB to be ready
until curl -s http://localhost:8000/v1/collections > /dev/null; do
  echo "Waiting for Chroma DB to be ready..."
  sleep 2
done

echo "Chroma DB is running. Validating data..."
python3 init_vector_db.py

echo "Vector database initialization complete. System is ready for RAG logic implementation."
