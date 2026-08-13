---
title: Three Tokens Force Exponential Feature Rank in Nonnegative Kernel Attention
url: http://arxiv.org/abs/2608.11427v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_20-49-34Z_ThreeTokensForceExponentialFeatureRankinNonnegativ.md
generated_at: 2026-08-12 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the computational complexity of nonnegative kernel attention when sequences contain two competing candidates. It demonstrates that full attention is exact for short sequences, while kernel attention incurs an exponential blow‑up in required feature dimension at length three. The analysis shows that dense softmax remains optimal with linear scores.

## Key Takeaways
- Kernel attention on a three‑token Boolean sequence demands $2^{Ω(m)}$ features even when token values are finite and readout is affine, whereas full attention solves it exactly.
- Rank‑one normalized kernel attention can solve any sequence of length at most two without extra feature growth.
- The lower bound approaches the exact $2^m$‑feature realization as context length grows, confirming exponential complexity.

## Context
This work highlights a fundamental trade‑off between representation efficiency and expressive power in neural models that compress sequences. It underscores how kernel tricks can inadvertently amplify computational cost beyond what is necessary for simple tasks.

## Implications
For practitioners designing scalable attention mechanisms, the paper warns against assuming constant feature budgets when handling longer contexts. It suggests revisiting model architectures to avoid exponential resource requirements in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11427v1)
