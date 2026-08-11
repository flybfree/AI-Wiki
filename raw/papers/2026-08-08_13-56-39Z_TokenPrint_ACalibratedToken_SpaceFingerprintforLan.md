---
title: TokenPrint: A Calibrated Token-Space Fingerprint for Language-Model Provenance
published: 2026-08-08T13:56:39Z
authors: Yuqi Wu, Shengming Zhao, Jie Chen
url: http://arxiv.org/abs/2608.08139v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TokenPrint: A Calibrated Token-Space Fingerprint for Language-Model Provenance

## Abstract
Establishing the provenance of a language model---including its base checkpoint and possible overlap in training distributions---is a governance challenge that metadata alone cannot resolve. We introduce a training-free fingerprint based on the top-$k$ vocabulary projections of late hidden states elicited by 250 fixed knowledge probes, compared using Jaccard overlap over decoded token strings. We evaluate the method on 32 open-weight models from nine families (0.6B--32B) with documented relationships. (1)~A \emph{similarity ladder} broadly follows model relatedness: independently trained models on identical data score 0.48 raw (0.35 vocabulary-corrected), followed by shared-base fine-tunes (0.39/0.33), same-developer relatives (0.38/0.28), and models with no documented relationship (0.22/0.17). This identical-data signal persists across three organizations, two tokenizer families, and two architecture classes, and emerges within the first 1\% of training before measurable task competence, suggesting a contribution from shared training data beyond capability convergence. (2)~As a nearest-neighbor \emph{lineage-retrieval} method, the fingerprint ranks the exact documented base among the top two candidates for all five R1 distillations (mean rank 1.8, MRR 0.60), including a math-specialized base not identifiable from coarse metadata. (3)~A \emph{depth ablation} shows that lineage group discrimination strengthens toward the output distribution, with AUC increasing from 0.72 at quarter depth to 0.90 at the output; using only the top 5 output tokens retains AUC 0.87. (4)~The fingerprint remains stable under quantization, with Jaccard similarity of 0.92 under int8 and 0.82--0.85 under int4, compared with a maximum cross-model similarity of 0.81 in the calibration pool. We release the probes, code, and fingerprints.

## Metadata
- **Published**: 2026-08-08T13:56:39Z
- **Authors**: Yuqi Wu, Shengming Zhao, Jie Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08139v1)