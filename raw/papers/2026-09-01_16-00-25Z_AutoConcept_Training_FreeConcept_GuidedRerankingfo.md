---
title: AutoConcept: Training-Free Concept-Guided Reranking for Metadata-Available Composed Image Retrieval
published: 2026-09-01T16:00:25Z
authors: Tianyu Wang, Tianjiao Wu
url: http://arxiv.org/abs/2609.01456v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoConcept: Training-Free Concept-Guided Reranking for Metadata-Available Composed Image Retrieval

## Abstract
Composed image retrieval (CIR) retrieves a target image from a reference image and a text modification. This paper studies metadata-available CIR reranking, where a fixed CIR model first returns a candidate pool and gallery metadata is then used for second-stage concept-guided scoring. We introduce AutoConcept, a training-free reranker that converts concept evidence into an interpretable memory. AutoConcept filters noisy concepts, activates query-relevant positive constraints with an auxiliary negative penalty, and combines base retrieval scores with metadata-based concept-candidate alignment through inference-time calibration. On FashionIQ, AutoConcept yields significant early-rank improvements over WeiMoCIR and consistent plug-in gains on LinCIR candidate pools. Metadata-aware controls show that structured concept memory adds signal beyond direct query-text and extracted-attribute matching, while a query-only variant further supports the effectiveness of concept-level reranking. A supplementary real-human concept-label study indicates that the same memory interface can consume participant-provided evidence. These results position AutoConcept as an interpretable concept-memory reranker for product-style CIR galleries with available metadata.

## Metadata
- **Published**: 2026-09-01T16:00:25Z
- **Authors**: Tianyu Wang, Tianjiao Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01456v1)