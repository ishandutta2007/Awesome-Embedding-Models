# Automated Corporate E-Discovery

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
