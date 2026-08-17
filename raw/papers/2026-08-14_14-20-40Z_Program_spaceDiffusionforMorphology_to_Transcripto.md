---
title: Program-space Diffusion for Morphology-to-Transcriptomics Prediction
published: 2026-08-14T14:20:40Z
authors: Ruyter Swann, Dorent Reuben, Racoceanu Daniel
url: http://arxiv.org/abs/2608.14330v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Program-space Diffusion for Morphology-to-Transcriptomics Prediction

## Abstract
Spatial transcriptomics (ST) enables genome-wide gene expression profiling while preserving tissue architecture, but its cost and limited scalability remain major bottlenecks. This has motivated models that predict spatial expression directly from routine histology. Despite promising results, most existing approaches operate at the gene level without leveraging established transcriptomic modeling practices and rely on heterogeneous gene selection strategies, which complicates fair comparison across methods.   We propose to reformulate morphology-to-transcriptomics prediction as conditional generation in transcriptional program space, thereby exploiting coordinated transcriptional variation instead of predicting genes independently. Using consensus non-negative matrix factorization (cNMF), we extract a low-dimensional set of transcriptional programs capturing coordinated expression variation in the training data, and train a conditional diffusion model to generate program activations from histology. This formulation exploits coordinated transcriptional variation and substantially lowers the dimensionality of the conditional generative task.

## Metadata
- **Published**: 2026-08-14T14:20:40Z
- **Authors**: Ruyter Swann, Dorent Reuben, Racoceanu Daniel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14330v1)