---
title: ChaosProbe: A Neurochaotic Lens on Frozen Transformer Input-Embedding Spaces
published: 2026-08-03T09:35:11Z
authors: Kunal Kumar Pant, Nithin Nagaraj
url: http://arxiv.org/abs/2608.01968v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ChaosProbe: A Neurochaotic Lens on Frozen Transformer Input-Embedding Spaces

## Abstract
Transformer models are most often understood through what they do: their benchmark performance, generation quality, or behavior on downstream tasks. Yet frozen transformer input-embedding spaces may also be examined through their responses to a controlled deterministic probe before contextual computation or task-specific adaptation. Guided by this response-based view, we introduce \emph{ChaosProbe}, a deterministic neurochaos-inspired method for constructing response-based fingerprints of frozen transformer input-embedding spaces. For each prompt-level embedding matrix, ChaosProbe applies a chaotic trajectory-based transformation and summarizes its Firing Rate and Entropy channel responses with complementary representation-level measures, producing a fixed-length signature for each model. In a bounded proof-of-concept study of $80$ neutral prompts and four pretrained models---GPT-2, DistilGPT2, BERT-base-uncased, and RoBERTa-base---Pearson correlation, Spearman correlation, and cosine similarity each recover all four same-family nearest-neighbor assignments and both expected mutual family pairs. Euclidean distance recovers three of the four assignments and one of the two mutual family pairs. Paired bootstrap resampling supports the stability of the Pearson and Spearman pairings over the observed prompt set, and signature-validity checks show that constant or collapsed responses do not dominate the reported fingerprints. These results provide a cohort-dependent proof of concept that deterministic neurochaotic response signatures can expose broad structure among frozen transformer input-embedding spaces.

## Metadata
- **Published**: 2026-08-03T09:35:11Z
- **Authors**: Kunal Kumar Pant, Nithin Nagaraj
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01968v1)