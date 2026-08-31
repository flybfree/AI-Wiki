---
title: KLOD: Locality-Preserving Knowledge Editing via Non-Target Distribution Preservation
published: 2026-08-28T02:16:24Z
authors: Hojun Jeong, Gyunyeop Kim, Sangwoo Kang
url: http://arxiv.org/abs/2608.27839v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KLOD: Locality-Preserving Knowledge Editing via Non-Target Distribution Preservation

## Abstract
Fine-tuning-based knowledge editing is simple and architecture-agnostic, but standard cross-entropy increases the edited target probability without explicitly constraining changes in the non-target output distribution. In sequential editing, such unconstrained redistribution can accumulate as distributional drift and contribute to locality degradation. We propose KLOD, a bounded and distribution-preserving objective for fine-tuning-based knowledge editing that separates the intended target update from distributions that should remain stable. KLOD stops target amplification once a probability threshold is reached, while preserving the target-excluded non-target distribution at target positions and the full next-token distribution at prefix positions. Experiments on CounterFact and ZsRE with Llama3-8B-Instruct and Qwen2.5-7B-Instruct show that KLOD substantially mitigates locality degradation while maintaining high edit reliability. The target probability threshold further provides a controllable Generalization--Locality trade-off. Ablation, multi-seed, and distributional KL analyses support the interpretation that KLOD's locality gains are associated with preserving output distributions rather than simply weakening the edit. Code is available on GitHub https://github.com/Hostoday/KLOD .

## Metadata
- **Published**: 2026-08-28T02:16:24Z
- **Authors**: Hojun Jeong, Gyunyeop Kim, Sangwoo Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27839v1)