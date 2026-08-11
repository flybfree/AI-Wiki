---
title: What Would Fix This RAG Failure? Auditing Counterfactual Response with Paired Evidence Interventions
published: 2026-08-09T22:43:27Z
authors: Wenzhang Du
url: http://arxiv.org/abs/2608.08944v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Would Fix This RAG Failure? Auditing Counterfactual Response with Paired Evidence Interventions

## Abstract
A failed retrieval-augmented generation (RAG) answer can be consistent with several unseen responses to evidence repair. We introduce Pair-ID, an offline audit that holds one query, retrieval state, and reader constant, then crosses two operations, adding missing support and deleting verified nonsupport, to measure a same-failure counterfactual response vector. A complete funnel over 19,981 benchmark queries identifies 11,105 eligible Qwen failures, from which a prospectively fixed SHA-256 ordering selects 1,200 before generating any sampled response. Among 1,190 regenerated-valid failures, support addition repairs 197/600 JOINT cases (0.328, 95% CI [0.292, 0.367]), and deletion repairs 162/1,190 cases (0.136, 95% CI [0.117, 0.155]); length- and position-matched shams retain semantic contrasts of 0.223 and 0.101. The original view carries partial predictive signal for individual response cells (macro AUROC 0.678; Brier 0.152 versus 0.160 for a marginal baseline), but exact-vector accuracy, 0.637, does not exceed the 0.646 majority-vector baseline, and vector macro-F1 is 0.170. Across four readers, both marginal sensitivities recur, while pooled exact-vector agreement is 0.675-0.765 and JOINT-only agreement falls to 0.538-0.691. These results show that evidence sensitivity occurs at meaningful rates in the hash-selected eligible-failure sample, is only partially predictable from the observed failure, and is conditional on the reader. The evidence supports a frame-scoped offline response audit, not an information-theoretic impossibility result, reader-independent taxonomy, or runtime repair policy.

## Metadata
- **Published**: 2026-08-09T22:43:27Z
- **Authors**: Wenzhang Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08944v1)