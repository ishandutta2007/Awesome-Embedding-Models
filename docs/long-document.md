# The Long-Document Information Dilution

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
