# Dense vs. Sparse Embedding Models

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
