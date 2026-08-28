---
title: A Table Is Worth 64 Tokens: Pixel-level Compression for Multi-Table Document Question Answering
published: 2026-08-27T10:50:13Z
authors: Iñigo Alonso, Mirella Lapata
url: http://arxiv.org/abs/2608.26949v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Table Is Worth 64 Tokens: Pixel-level Compression for Multi-Table Document Question Answering

## Abstract
Answering questions over real-world documents requires processing long inputs that interleave text with tables. Optical context compression, which represents context as images, promises to reduce token cost, but its effect on table understanding remains unclear. We study pixel-level table compression for question answering over documents with multiple tables, evaluating five VLMs across two benchmarks and five visual-token budgets. Representing tables as images at native resolution matches text in both performance and efficiency, but downscaling them makes models compensate the loss in readability with longer, less effective reasoning traces that cancel the expected savings. Highly downscaled tables, however, preserve enough signal to identify whether they are relevant to a question. We exploit this asymmetry with a training-free, two-step method: the model first identifies the tables needed to answer a question from a pixel-compressed context, and then reasons over those at native resolution. On long documents, our method saves 41% of total tokens and gains 7 accuracy points over single-step QA with native resolution tables. It also uses 15% fewer tokens than the most efficient single-step compressed configuration, with no accuracy loss.

## Metadata
- **Published**: 2026-08-27T10:50:13Z
- **Authors**: Iñigo Alonso, Mirella Lapata
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26949v1)