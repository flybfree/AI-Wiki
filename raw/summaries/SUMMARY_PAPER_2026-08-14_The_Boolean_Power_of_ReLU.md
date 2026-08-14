---
title: The Boolean Power of ReLU
url: http://arxiv.org/abs/2608.12617v1
type: paper-summary
date: 2026-08-14
source_paper: 2026-08-12_21-59-58Z_TheBooleanPowerofReLU.md
generated_at: 2026-08-14 11:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proves that Boolean queries expressible in Σ‑MPLang are a strict subset of those expressible in ReLU‑MPLang for finite simple undirected graphs with a single Boolean node feature. This settles the open question of whether ReLU‑MPLang is more powerful than trReLU‑MPLang, showing ReLU‑based models dominate on such data.

## Key Takeaways
- The Boolean query space of Σ‑MPLang is strictly smaller than that of ReLU‑MPLang, meaning some queries achievable with ReLU cannot be expressed in the Boolean setting.  
- This result holds for any collection Σ of eventually constant activation functions and arbitrary real coefficients, confirming generality across typical GNN activations.  
- Consequently, ReLU‑GNNs are strictly more expressive than {TrReLU,id}-GNNs when evaluating Boolean queries on graphs with Boolean features.

## Context
This work addresses a fundamental limitation in the expressivity of neural network architectures applied to graph data where inputs are binary or Boolean. Understanding which query types can be computed is crucial for designing models that respect input semantics and avoid unnecessary complexity. The distinction between ReLU‑based and TrReLU‑based models thus has practical implications for algorithmic design.

## Implications
For practitioners, the finding suggests that if Boolean features are available, using ReLU activations does not increase expressive power beyond what is already achievable with simpler models. This may guide resource allocation in training GNNs on binary data, encouraging use of more efficient architectures when full ReLU capacity is unnecessary. It also reinforces the need to match model complexity to query requirements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12617v1)
