import os
import re

os.makedirs('docs', exist_ok=True)

pages = [
    {
        "title": "The Static Word-Level Lookup Era (Word2Vec / GloVe)",
        "file": "docs/word2vec-glove.md",
        "match": r"\*\*The Static Word-Level Lookup Era \(Word2Vec / GloVe\)\*\*",
        "content": """# The Static Word-Level Lookup Era (Word2Vec / GloVe)

## Overview
The Static Word-Level Lookup Era (~2013-2017) revolutionized natural language processing by mapping discrete words to dense, continuous vector spaces. Models like Word2Vec and GloVe proved that continuous vector directions could capture abstract semantic meaning.

## Key Diagram
```mermaid
graph TD
    A[Input Word] --> B[Embedding Matrix Lookup]
    B --> C[Static Dense Vector 300D]
    C --> D[Semantic Meaning]
```

## Detailed Information
Unlike earlier sparse representations like One-Hot Encoding, Word2Vec generated a fixed-size vector for each word. While this captured broad semantic relationships, a major limitation was polysemy—a single word (like 'bank') had only one representation, regardless of context.
"""
    },
    {
        "title": "The Bidirectional Contextual Projection Era (BERT / ELMo)",
        "file": "docs/bert-elmo.md",
        "match": r"\*\*The Bidirectional Contextual Projection Era \(BERT / ELMo\)\*\*",
        "content": """# The Bidirectional Contextual Projection Era (BERT / ELMo)

## Overview
This era (~2018-2021) introduced dynamic, context-aware embeddings, solving the polysemy bottleneck of static embeddings.

## Key Diagram
```mermaid
graph TD
    A[Input Sequence] --> B[Self-Attention Layers]
    B --> C[Contextual Hidden State]
    C --> D[Dynamic Token Embedding]
```

## Detailed Information
Models like BERT process the entire surrounding sequence to compute an embedding for a specific token dynamically. The same word (e.g., 'bank') will have a different vector depending on whether the surrounding words discuss finance or nature.
"""
    },
    {
        "title": "The Siamese Bi-Encoder Revolution (Sentence-BERT / SBERT)",
        "file": "docs/sbert.md",
        "match": r"\*\*The Siamese Bi-Encoder Revolution \(Sentence-BERT / SBERT\)\*\*",
        "content": """# The Siamese Bi-Encoder Revolution (Sentence-BERT / SBERT)

## Overview
SBERT (2019-2023) revolutionized document retrieval by introducing Siamese Network configurations for fast cosine similarity scoring.

## Key Diagram
```mermaid
graph LR
    A[Sentence A] --> C[BERT Encoder] --> E[Vector A]
    B[Sentence B] --> D[BERT Encoder] --> F[Vector B]
    E & F --> G[Cosine Similarity]
```

## Detailed Information
Before SBERT, computing the similarity of two sentences required passing both through a single BERT model, causing massive latency. Bi-Encoders map sentences to vectors independently, dropping search time from hours to milliseconds.
"""
    },
    {
        "title": "The Multi-Task Instruction & Matryoshka Nesting Era",
        "file": "docs/multi-task-mrl.md",
        "match": r"\*\*The Multi-Task Instruction & Matryoshka Nesting Era\*\*",
        "content": """# The Multi-Task Instruction & Matryoshka Nesting Era

## Overview
This current era (2024-Present) merges massive parameter language models with instruction fine-tuning and Matryoshka representation learning.

## Key Diagram
```mermaid
graph TD
    A[Task Instruction + Text] --> B[Massive Auto-Regressive LM]
    B --> C[Truncatable Dense Vector]
    C --> D[Adaptive Search & Clustering]
```

## Detailed Information
By prepending task prompts (e.g., 'Represent this text for retrieval'), modern embeddings shape the vector density on the fly. Paired with MRL, these vectors can be cleanly sliced to save storage footprints while preserving accuracy.
"""
    },
    {
        "title": "Bi-Encoder Models (Dual-Tower Matching)",
        "file": "docs/bi-encoder.md",
        "match": r"\*\*Bi-Encoder Models \(Dual-Tower Matching\)\*\*",
        "content": """# Bi-Encoder Models (Dual-Tower Matching)

## Overview
A scalable architecture where texts are embedded independently.

## Key Diagram
```mermaid
graph TD
    A[Text] --> B[Encoder]
    B --> C[Vector]
    C --> D[Vector DB / Index]
```

## Detailed Information
Bi-Encoders generate vectors instantly and are highly scalable because vectors can be calculated offline and searched via approximate nearest neighbor (ANN) indexes.
"""
    },
    {
        "title": "Cross-Encoder Models (Full-Attention Fusion)",
        "file": "docs/cross-encoder.md",
        "match": r"\*\*Cross-Encoder Models \(Full-Attention Fusion\)\*\*",
        "content": """# Cross-Encoder Models (Full-Attention Fusion)

## Overview
An architecture that concatenates two texts for maximum semantic precision.

## Key Diagram
```mermaid
graph TD
    A[Text A + SEP + Text B] --> B[Cross-Attention Layers]
    B --> C[Similarity Score]
```

## Detailed Information
Unlike Bi-Encoders, Cross-Encoders calculate full attention between every word in both texts. While they are highly accurate, they are computationally unviable for large-scale database lookups and are usually reserved for late-stage reranking.
"""
    },
    {
        "title": "Dense vs. Sparse Embedding Models",
        "file": "docs/dense-vs-sparse.md",
        "match": r"\*\*Dense vs\. Sparse Embedding Models\*\*",
        "content": """# Dense vs. Sparse Embedding Models

## Overview
A comparison between high-dimensional continuous arrays (Dense) and uncompressed token frequency arrays (Sparse).

## Key Diagram
```mermaid
graph TD
    A[Input Text] --> B(Dense Encoder) --> D[Vector of Floats]
    A --> C(Sparse Encoder) --> E[Vector of Tokens with Weights]
```

## Detailed Information
Sparse models like SPLADE provide precise keyword-matching resolution, while Dense models excel at abstract cross-phrasing. Modern hybrid search systems often fuse both using Reciprocal Rank Fusion (RRF).
"""
    },
    {
        "title": "Matryoshka Representation Learning (MRL)",
        "file": "docs/mrl.md",
        "match": r"\*\*Matryoshka Representation Learning \(MRL\)\*\*",
        "content": """# Matryoshka Representation Learning (MRL)

## Overview
A loss paradigm that forces hierarchical nesting of semantic information within a single vector.

## Key Diagram
```mermaid
graph LR
    A[Full Vector 1536D] --> B[First 256D Contains Core Semantics]
    B --> C[Truncation without significant loss]
```

## Detailed Information
MRL packs the most critical signals into the earliest coordinates of the vector stream, unlocking adaptive vector truncation and saving massive storage costs.
"""
    },
    {
        "title": "Cross-Modal Joint-Embeddings (CLIP / SigLIP)",
        "file": "docs/clip-siglip.md",
        "match": r"\*\*Cross-Modal Joint-Embeddings \(CLIP / SigLIP\)\*\*",
        "content": """# Cross-Modal Joint-Embeddings (CLIP / SigLIP)

## Overview
Models designed to map diverse modalities (like images and text) into a shared coordinate space.

## Key Diagram
```mermaid
graph TD
    A[Image] --> B[Vision Encoder]
    C[Text] --> D[Text Encoder]
    B & D --> E[Shared Latent Space]
```

## Detailed Information
CLIP uses contrastive loss to pull matching image-text pairs close together and push mismatched pairs apart, revolutionizing open-vocabulary visual search.
"""
    },
    {
        "title": "The Long-Document Information Dilution (The Squashing Effect)",
        "file": "docs/long-document.md",
        "match": r"\*\*The Long-Document Information Dilution \(The Squashing Effect\)\*\*",
        "content": """# The Long-Document Information Dilution

## Overview
A major challenge where compressing a huge text block into a single vector results in information loss.

## Key Diagram
```mermaid
graph TD
    A[10,000 Word Doc] --> B[Chunking Engine]
    B --> C[200-Token Shards]
    C --> D[Precise Dense Indexing]
```

## Detailed Information
Mitigated by Hierarchical Parent-Child Chunking, which allows small shards to provide precision indexing while retrieving the broader parent context during inference.
"""
    },
    {
        "title": "The Distributed Vector Indexing Memory Wall",
        "file": "docs/distributed-indexing.md",
        "match": r"\*\*The Distributed Vector Indexing Memory Wall\*\*",
        "content": """# The Distributed Vector Indexing Memory Wall

## Overview
The issue of RAM saturation when storing and executing exhaustive distance matrices for millions of uncompressed dense vectors.

## Key Diagram
```mermaid
graph TD
    A[Millions of Vectors] --> B[ANN Graph like HNSW]
    B --> C[Quantized Vectors in RAM/SRAM]
    C --> D[Sub-millisecond Search]
```

## Detailed Information
Modern vector databases mitigate this by using Approximate Nearest Neighbors (ANN) and quantization to execute billions of distance checks rapidly.
"""
    },
    {
        "title": "Enterprise Retrieval-Augmented Generation (RAG Infrastructure)",
        "file": "docs/enterprise-rag.md",
        "match": r"\*\*Enterprise Retrieval-Augmented Generation \(RAG Infrastructure\)\*\*",
        "content": """# Enterprise Retrieval-Augmented Generation

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
"""
    },
    {
        "title": "Open-Vocabulary E-Commerce Product Catalog Ingestion",
        "file": "docs/ecommerce-catalog.md",
        "match": r"\*\*Open-Vocabulary E-Commerce Product Catalog Ingestion\*\*",
        "content": """# E-Commerce Product Catalog Ingestion

## Overview
Processing and sorting multi-modal merchant inventory listings without manual rules.

## Key Diagram
```mermaid
graph TD
    A[Product Image & Text] --> B[CLIP Encoder]
    B --> C[Unified Dense Vector]
    C --> D[Dynamic Taxonomy Branching]
```

## Detailed Information
Automates product sorting and visual search functionalities in huge multi-vendor marketplaces.
"""
    },
    {
        "title": "Automated Corporate E-Discovery & Legal Audit Reranking",
        "file": "docs/corporate-ediscovery.md",
        "match": r"\*\*Automated Corporate E-Discovery & Legal Audit Reranking\*\*",
        "content": """# Automated Corporate E-Discovery

## Overview
Using embedding models to process millions of unstructured legal contracts for litigation histories.

## Key Diagram
```mermaid
graph TD
    A[Legal Query] --> B[First-stage Bi-Encoder Retrieval]
    B --> C[Top 100 Candidates]
    C --> D[Cross-Encoder Reranker]
    D --> E[High-Precision Results]
```

## Detailed Information
Multi-Task Cross-Encoders evaluate complex legal liabilities with human-grade verification accuracy.
"""
    }
]

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

for p in pages:
    # Write page
    with open(p['file'], 'w', encoding='utf-8') as f:
        f.write(p['content'])
    
    # Replace in README
    readme = re.sub(p['match'], f"[**{p['title']}**]({p['file']})", readme)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("Created 14 pages and linked them in README.md")
