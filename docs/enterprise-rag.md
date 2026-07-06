# Enterprise Retrieval-Augmented Generation

## Overview
The architecture powering corporate AI knowledge retrieval using vector databases.

## Key Diagram
```mermaid
graph TD
    A[User Query] --> B[Embedding Model]
    B --> C[Vector DB Search]
    C --> D[Context Rows Fetched]
    D --> E[LLM Generation]
```

## Detailed Information
RAG maps queries into dense coordinates, looking up precise matching context in databases like Pinecone, Milvus, or Qdrant.
