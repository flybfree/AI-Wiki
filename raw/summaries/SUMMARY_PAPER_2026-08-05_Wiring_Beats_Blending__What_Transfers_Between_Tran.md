---
title: Wiring Beats Blending: What Transfers Between Transformer Sizes -- and What Doesn't
url: http://arxiv.org/abs/2608.02829v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_19-44-08Z_WiringBeatsBlending_WhatTransfersBetweenTransforme.md
generated_at: 2026-08-05 01:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how pretrained large language models can be converted into smaller models and whether the transferred knowledge persists across different sizes. It analyzes the conversion from a 1.4B to a 410M model within the Pythia family, showing that representation alignment is strong while parameter alignment is weak. The authors demonstrate that dense weight projection destroys functional structures and that conversion quality depends on initialization.

## Key Takeaways
- Representations align strongly across sizes with ridge R^2=0.84 but parameters align weakly, indicating that the mapping between model dimensions is not a simple scaling of weights.
- Dense weight projection is functionally destructive because basis mixing breaks rotary, per-head GELU and LayerNorm structures, making conversion dependent on initialization rather than assembly artifacts.
- After fitting a best-fit linear operator, residual weights are indistinguishable from noise under shuffle controls, confirming that conversion value resides in the initial state.

## Context
Model scaling remains a major challenge as training resources increase. Efficiently shrinking large models without losing performance is crucial for deployment and cost reduction. This study provides empirical evidence on which aspects of knowledge survive transfer and how to optimize it.

## Implications
Practitioners can focus conversion efforts on initialization tuning rather than retraining, saving tokens and compute. The findings suggest a path toward modular model architectures where smaller components inherit large models’ capabilities with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02829v1)
