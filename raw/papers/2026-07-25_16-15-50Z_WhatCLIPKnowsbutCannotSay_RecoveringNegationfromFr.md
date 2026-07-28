---
title: What CLIP Knows but Cannot Say: Recovering Negation from Frozen Intermediate Features
published: 2026-07-25T16:15:50Z
authors: Chen-Yi Lu, Yueh-Shao Chen, Somali Chaterji
url: http://arxiv.org/abs/2607.23271v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What CLIP Knows but Cannot Say: Recovering Negation from Frozen Intermediate Features

## Abstract
Contrastive vision-language models such as CLIP map semantically opposite phrases (e.g., "a dog" vs. "not a dog") to nearly identical embeddings, rendering them insensitive to negation. We attribute this failure to a phenomenon we call Representational Collapse: by tracking compositional divergence and visual alignment across the CLIP text encoder, we show that middle layers build compositional syntax, but the final layers collapse this structure as visual alignment rises, producing a syntax-blind final representation. To recover the lost negation signal without altering pretrained weights, we propose PeakPatch, a lightweight post-hoc correction system that intercepts the encoder at its compositional peak. An Embedding Correction Network (ECN) uses cross-attention to extract a negation-specific signal from the peak layer, anchored to a stable baseline, and predicts a deviation vector that re-injects the lost syntax into the final-layer embedding space. A complementary Score Correction Network (SCN) predicts bounded scalar score offsets for discriminative tasks. Both modules are trained jointly end-to-end while all CLIP parameters remain frozen, adding only 5.2M parameters (3.5% of the backbone) and preserving the standard cosine similarity interface. On NegBench, PeakPatch achieves 74.3% on COCO MCQ (+35.1 over CLIP, +17.8 over the best encoder fine-tuning method) and 65.5% on VOC MCQ, while outperforming all fine-tuning baselines on fully out-of-distribution negation retrieval despite training only 3.5% of the parameters. The corrected embeddings also transfer to text-to-image generation (+18.4 negation score) and generalize across ViT-B/32, ViT-L/14, and SigLIP backbones. Project URL: https://stevencylu.github.io/PeakPatch/.

## Metadata
- **Published**: 2026-07-25T16:15:50Z
- **Authors**: Chen-Yi Lu, Yueh-Shao Chen, Somali Chaterji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23271v1)