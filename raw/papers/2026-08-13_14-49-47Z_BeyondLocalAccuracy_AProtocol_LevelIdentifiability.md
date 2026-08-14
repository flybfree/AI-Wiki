---
title: Beyond Local Accuracy: A Protocol-Level Identifiability Audit for Controlled LLM Reasoning Evaluation
published: 2026-08-13T14:49:47Z
authors: Junhao Luo, Ning Huang, Ziqi Sha, Wenxuan Tang, Wei Deng
url: http://arxiv.org/abs/2608.13326v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Local Accuracy: A Protocol-Level Identifiability Audit for Controlled LLM Reasoning Evaluation

## Abstract
LLM benchmark scores can be precise even when the observation protocol does not identify the behavioral property they are intended to measure. In a controlled, solver-grounded setting, we formalize a protocol-level identifiability audit over a finite behavioral policy class: given policies H, observation support O, and estimand $τ$, we test whether O separates every pair with different $τ$. The audit requires zero model calls and resolves our diagnostic case: base-only observation collapses seven frozen deterministic policies into one equivalence class; full support yields seven classes and no cross-estimand collisions; every leave-one-out support retains a constructive collision witness. Empirically, both constrained-generation variants have pair-validity 1.0, yet base accuracy and selective-response fidelity diverge - 0.620 versus 0.324 across six balanced oracle-transition directions (cluster-bootstrap 95% CI [0.600, 0.642] vs. [0.304, 0.345]) - and the gap recurs on a second deterministic source (0.646 vs. 0.331). The audit also synthesizes a minimum identifying support $O^*$ for the frozen policy class: two cells instead of the full 36-cell tensor. This case shows how evaluation-design validity can be checked structurally before model inference and why base correctness does not determine intervention-response fidelity.

## Metadata
- **Published**: 2026-08-13T14:49:47Z
- **Authors**: Junhao Luo, Ning Huang, Ziqi Sha, Wenxuan Tang, Wei Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13326v1)