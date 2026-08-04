---
title: Spatiotemporal Proximal Causal Inference under Hidden Confounding and Interference
url: http://arxiv.org/abs/2608.01352v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_16-13-21Z_SpatiotemporalProximalCausalInferenceunderHiddenCo.md
generated_at: 2026-08-03 23:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a spatiotemporal proximal causal inference framework that extends identification theory to real‑world data where hidden confounders and interference coexist. It identifies a bridge function that recovers outcomes without needing the confounder directly, using proxies and a neural architecture.

## Key Takeaways
- The method introduces treatment‑ and outcome‑inducing proxies to capture local confounding information in spatiotemporal settings.
- It derives an identifiable bridge function under proxy exclusion restrictions and a completeness condition, generalizing g‑computation for outcomes.
- A transformer encoder learns these proxies while a critic enforces exclusion and a network matches moments to satisfy the identifying equation.

## Context
In AI research, causal inference methods often assume exchangeability that breaks down with hidden variables, limiting real‑world applicability. This work bridges statistical theory and deep learning by using neural proxies to handle interference in spatiotemporal data.

## Implications
For climate or policy analysts, the framework provides a principled way to estimate causal effects despite unobserved confounders. Industries can apply it to improve decision‑making in regional economics where spatial and temporal patterns matter.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01352v1)
