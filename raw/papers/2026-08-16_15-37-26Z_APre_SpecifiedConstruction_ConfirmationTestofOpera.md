---
title: A Pre-Specified Construction-Confirmation Test of Operation-Level Causal Transfer Across Finite Isomorphic Symbolic Domains
published: 2026-08-16T15:37:26Z
authors: Xinyi Shan
url: http://arxiv.org/abs/2608.15809v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Pre-Specified Construction-Confirmation Test of Operation-Level Causal Transfer Across Finite Isomorphic Symbolic Domains

## Abstract
Behavioral accuracy, linear decodability, and successful activation interventions do not by themselves show that a model carries an operation-level structure from one symbolic domain to another. We ask a narrower question in finite isomorphic state spaces: if the hidden-state difference between two operations is estimated separately for each source input, does adding that difference to a mapped recipient input move the model toward the corresponding recipient answer? The design compares this input-specific intervention with wrong-operation, norm-matched random, and no-op controls, and separates candidate construction from an independently isolated confirmation split. On a frozen Qwen2.5-7B-Instruct model at layers 20--21, one route--domain--operation candidate from a family pre-specified and frozen before confirmation access, transparent | integer_mod16--letters16 | successor->predecessor, passed both PyVene splits; its confirmation intersection--union p-value was 0.000198 and its 36-family Holm-adjusted p-value was 0.006943. A subsequent NNsight 0.7.0 experiment, pre-specified and frozen before its confirmation access, tested only this selected prompt route, without candidate or layer reselection. It reproduced all 12 confirmation effect estimates, confidence intervals, and exact sign-flip p-values numerically; its 36-family Holm-adjusted p-value was 0.007141. The result is therefore limited to one prompt route and one candidate, replicated across two intervention implementations on one model revision and one layer interval. It does not establish cross-model generalization, full-family backend independence, domain-general transfer, or algebraic invariance.

## Metadata
- **Published**: 2026-08-16T15:37:26Z
- **Authors**: Xinyi Shan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15809v1)