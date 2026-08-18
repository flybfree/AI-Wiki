---
title: NICE: Scale-Stable Perturbations for Graph Neural Network Explanations via Noise Corruption
url: http://arxiv.org/abs/2608.16038v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_03-08-14Z_NICE_Scale_StablePerturbationsforGraphNeuralNetwor.md
generated_at: 2026-08-17 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the problem of unreliable graph neural network explanations caused by deterministic scale contraction introduced by element‑wise masking. It introduces Noise Corruption, a perturbation that preserves message norms and reduces scale drift, and proposes NICE, which learns a stochastic restoration boundary to balance prediction recovery with compactness. Experiments show stronger explanation performance and model faithfulness compared to existing methods.

## Key Takeaways
- Element‑wise masking causes deterministic scale contraction across layers, leading to misleading importance scores.
- Noise Corruption perturbs each message using matched‑norm random‑direction noise while keeping the expected squared norm constant, mitigating scale drift.
- NICE learns a stochastic restoration boundary that restores predictions under NC uncertainty while minimizing explanation size.

## Context
Graph neural network explainers rely on post‑hoc perturbation strategies to highlight influential nodes or edges. Traditional masking approaches often degrade model behavior by altering message scales, which can obscure true feature importance and reduce trust in explanations.

## Implications
This work provides a scalable, distributionally stable alternative for GNN interpretability that preserves the integrity of learned messages. Practitioners can adopt Noise Corruption to generate more reliable explanations without sacrificing performance or introducing unwanted bias.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16038v1)
