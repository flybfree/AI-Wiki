---
title: From Base Rollouts to RL Reasoning: A Budgeted Search Perspective
url: http://arxiv.org/abs/2609.01274v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-08-39Z_FromBaseRolloutstoRLReasoning_ABudgetedSearchPersp.md
generated_at: 2026-09-01 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how reinforcement learning with verifiable rewards changes language-model reasoning and whether it reflects new capabilities or merely more efficient search. Using a Unified Decoding Framework they show that RL gains correspond to moving the decoding budget toward operating points already reachable by the base model, not new parameters. On several benchmarks the pass@k recovery follows a Budgeted Operating-Point Transition Rule with exponent relationships.

## Key Takeaways
- The RL default-policy curve can be approximated by a structured path of Base operating points defined by N_Base ≈ α N_RL^β, indicating a budget scaling relationship.  
- Pass@k recovery on Math500, AIME, GPQA, IFEval follows this BOPTR rule with benchmark-conditioned exponents, showing efficiency gains rather than new reasoning.  
- The rule yields low transfer error (3.41 pp) and holds across models without RL checkpoints or supervision.

## Context
Language-model reasoning is a key challenge in AI alignment and performance; RL can improve output but its impact on inference time remains debated. This study provides a behavioral framework to distinguish between capability and efficiency improvements, offering diagnostic tools for researchers.

## Implications
Practitioners should treat RL gains as search optimizations rather than parameter updates when evaluating deployment trade-offs. The BOPTR rule offers a quantitative benchmark for assessing how much extra compute is needed to realize RL benefits, guiding resource allocation in large language systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01274v1)
