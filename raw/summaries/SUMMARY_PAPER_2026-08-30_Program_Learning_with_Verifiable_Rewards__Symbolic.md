---
title: Program Learning with Verifiable Rewards: Symbolic Backpropagation for Post-Training LLMs
url: http://arxiv.org/abs/2608.28421v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_15-06-00Z_ProgramLearningwithVerifiableRewards_SymbolicBackp.md
generated_at: 2026-08-30 20:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PLVR, a post‑training method that learns reasoning programs from input‑output examples using symbolic backpropagation. Experiments on LiveCodeBench v6 and Tau2Bench show that 30B base models with PLVR beat reinforcement learning by an average of 27.8 points and outperform frontier models by 13.6 points at the same budget.

## Key Takeaways
- PLVR replaces reward‑guided search with uniform sampling over a type‑admissible program space, reducing median program length from 65.6 to 17.5 steps.
- The method uses symbolic backpropagation where credit assignment is derived via type inference rather than estimated gradients.
- A single primitive library serves both benchmarks, requiring only 100 examples of program search and no new finetuning data.

## Context
Current approaches for post‑training language model reasoning rely on black‑box RL or supervised fine‑tuning, which cannot inspect intermediate steps. Symbolic methods that separate reasoning from weights remain underutilized due to high computational cost and lack of verifiable credit assignment.

## Implications
PLVR offers a scalable way to embed interpretable reasoning into large models without retraining them, lowering the marginal cost of adding new tasks. This could enable industry‑wide deployment of verified AI assistants with transparent performance guarantees.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28421v1)
