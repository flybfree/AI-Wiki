---
title: The Boolean Power of ReLU
url: http://arxiv.org/abs/2608.12617v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_21-59-58Z_TheBooleanPowerofReLU.md
generated_at: 2026-08-13 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proves that Boolean queries expressible using Σ-MPLang with eventually constant activation functions are a strict subset of those expressible in ReLU-MPLang on finite simple undirected graphs with a single Boolean node feature. The result settles the open question of whether ReLU-MPLang is more powerful than trReLU-MPLang for Boolean queries.

## Key Takeaways
- [critical point 1 from the abstract, in detail] Boolean queries in Σ-MPLang are strictly less expressive than those in ReLU-MPLang, indicating a power gap.
- [critical point 2 from the abstract, in detail] The result holds for any collection Σ of eventually constant activation functions and arbitrary real coefficients on finite simple undirected graphs with Boolean features.
- [critical point 3 from the abstract, in detail] This implies that ReLU-GNNs are strictly more expressive than {TrReLU,id}-GNNs when evaluating Boolean queries.

## Context
Understanding the expressiveness limits of activation functions is crucial for designing efficient neural network architectures. This work clarifies a subtle difference between ReLU and its truncated variant in the context of graph neural networks, which has implications for theoretical analysis and practical model selection.

## Implications
Practitioners can rely on ReLU-based GNNs to achieve higher Boolean query capabilities than using only truncated ReLU with identity. This may guide research toward richer activation functions or alternative architectures when exact boolean reasoning is required.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12617v1)
