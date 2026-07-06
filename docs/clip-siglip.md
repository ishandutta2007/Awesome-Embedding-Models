# Cross-Modal Joint-Embeddings (CLIP / SigLIP)

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
