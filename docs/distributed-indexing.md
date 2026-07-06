# The Distributed Vector Indexing Memory Wall

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
