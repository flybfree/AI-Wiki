---
title: Looped Transformers with Source-Centered State Evolution
url: http://arxiv.org/abs/2607.27656v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_04-13-58Z_LoopedTransformerswithSource_CenteredStateEvolutio.md
generated_at: 2026-07-30 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
Looped Transformers reuse a shared block across recurrent depths to increase effective depth without adding parameters, but they face challenges with input conditioning and reference invariance. The paper introduces Source-Centered State Evolution (SCSE), a design that keeps the anchor fixed while allowing state-dependent computation through learned deviations. Experiments on multiple benchmarks show SCSE improves controlled recurrent quality.

## Key Takeaways
- The shared block must govern an entire trajectory of varying hidden states, making input conditioning problematic.
- SCSE retains input dependence via a learned anchor and initial deviation while mapping zero deviation to zero state.
- A zero-deviation forcing bias is set to zero to guarantee exact anchor invariance.

## Context
This work advances the design space for recurrent neural networks by separating conditioning from recurrence, enabling more stable training on long sequences. It aligns with trends toward modular, trainable components in deep learning architectures.

## Implications
For practitioners, SCSE offers a principled way to balance flexibility and stability, potentially reducing overfitting in long-context models. The field may adopt similar anchor-based mechanisms for better control over recurrent dynamics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27656v1)
