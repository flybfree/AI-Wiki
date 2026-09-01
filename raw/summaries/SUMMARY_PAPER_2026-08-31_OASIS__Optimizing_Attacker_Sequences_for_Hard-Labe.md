---
title: OASIS: Optimizing Attacker Sequences for Hard-Label Black-Box Text Attacks
url: http://arxiv.org/abs/2608.29568v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_05-26-19Z_OASIS_OptimizingAttackerSequencesforHard_LabelBlac.md
generated_at: 2026-08-31 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OASIS, a method that optimizes attacker sequences for hard-label black-box text attacks by performing a bi-objective search to balance success rate and perturbation, then reusing the chosen chain during execution. Experiments across multiple datasets, victim models, and large language models show OASIS outperforms standalone baselines and manually constructed chains. The results indicate that composition of attackers is an optimization target.

## Key Takeaways
- OASIS performs a one-time bi-objective attack chain search to balance attack success rate and perturbation level.
- The selected global chain is reused during execution, reducing computational cost compared to recomputing each time.
- Experiments demonstrate consistent superiority over strong standalone baselines and simple manually constructed chains.

## Context
Hard-label black-box text attacks are a growing concern as AI systems become more robust. Existing approaches focus on individual attackers or manual composition, which limits scalability and performance. OASIS addresses this by treating attacker sequence optimization as a systematic problem.

## Implications
This work shifts the focus from ad-hoc solutions to algorithmic optimization, encouraging developers to consider chain design in model hardening. Practitioners can leverage OASIS to generate more effective attack sequences with lower perturbation, improving security testing efficiency and reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29568v1)
