---
title: Disentangling Language Modeling and Boundaries
published: 2026-08-04T12:51:21Z
authors: Mykola Haltiuk
url: http://arxiv.org/abs/2608.03599v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangling Language Modeling and Boundaries

## Abstract
Byte-level language models are usually argued for on the grounds of robustness, multilingual fairness, and character-level skills. We point to a different, structural advantage: because they read and write bytes, any two of them share an output space, so knowledge transfer between them is exact and independent of how either was originally tokenized. We hypothesize that the two distributions a byte-level model produces, one over the next byte, one over where its patch boundaries fall, can be disentangled and changed almost independently. A model could absorb a teacher's capability while keeping its own boundaries, or change how it places those boundaries while keeping its capabilities. We lay out the two experiments that would settle the hypothesis, alongside preliminary measurements of the properties they rest on. We argue that the community should move toward a byte-level interface as a shared standard: if the hypothesis holds, then once byte-level models are the norm, transferring capabilities and reshaping boundaries between them become cheap and routine, free of the per-model tokenizer that blocks them today.

## Metadata
- **Published**: 2026-08-04T12:51:21Z
- **Authors**: Mykola Haltiuk
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03599v1)