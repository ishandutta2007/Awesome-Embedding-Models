# Cross-Encoder Models (Full-Attention Fusion)

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
