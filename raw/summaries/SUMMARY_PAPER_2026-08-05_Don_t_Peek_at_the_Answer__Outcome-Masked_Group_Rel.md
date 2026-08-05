---
title: Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR
url: http://arxiv.org/abs/2608.03119v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_04-41-20Z_Don_tPeekattheAnswer_Outcome_MaskedGroupRelativePo.md
generated_at: 2026-08-05 01:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces OM-GRPO, a label‑free reinforcement learning framework that separates reward estimation from policy optimization to avoid collapse in reasoning tasks. By masking gradients on answer spans and using a soft consensus signal, the method improves token‑level policies without reinforcing answers directly. Experiments across multiple benchmarks show OM‑GRPO outperforms existing label‑free RLVR methods and matches supervised ground‑truth training while providing stable test‑time performance.

## Key Takeaways
- OM-GRPO decouples reward estimation from policy optimization by masking gradients on the answer span, preventing the model from directly reinforcing answer tokens.  
- The framework retains answer‑level rewards through a soft consensus signal, shifting optimization pressure away from answer tokens to reasoning steps.  
- Contrast‑augmented reward refines reward estimates using low‑cost pairwise comparisons over existing trajectories without extra rollouts.

## Context
Label‑free RL for large language models aims to scale reinforcement learning without ground‑truth supervision, yet typical methods suffer from reward collapse that biases the model toward surface answers. This work addresses that limitation by introducing a principled gradient masking strategy and a contrast‑based reward refinement, aligning with broader efforts to make LLM training more efficient and robust.

## Implications
The stability achieved in test‑time training could reduce costly fine‑tuning cycles for industry applications where reliable reasoning is critical. Practitioners can adopt OM-GRPO to obtain high‑quality outputs without relying on expensive ground‑truth labels, fostering broader adoption of label‑free RL in AI research and deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03119v1)
