---
title: Cycle-Consistent and Uncertainty-Aware Neural Surrogates for Tokamak Edge Plasmas
url: http://arxiv.org/abs/2607.21407v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_15-06-57Z_Cycle_ConsistentandUncertainty_AwareNeuralSurrogat.md
generated_at: 2026-07-23 22:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a cycle-consistent neural surrogate designed to predict key edge plasma quantities in tokamaks such as temperature and density profiles on the SOLPS-ITER mesh. By combining a conditional U-Net forward model with an optimization-based inverse method that enforces consistency, the approach recovers all five control parameters from observations without ground‑truth labels. The ensemble also provides uncertainty estimates, enabling fast real‑time analysis.

## Key Takeaways
The conditional U-Net achieves normalized root‑mean‑square errors below 2.6% and Pearson correlations above 0.95 for all predicted fields. Cycle‑consistency regularization lifts the average cyclical R² from 0.59 to 0.99 while preserving forward accuracy, allowing reliable recovery of the core fueling rate with Pearson r ≥0.97 across all five parameters. An ensemble predicts electron temperature and density profiles at the outboard midplane and divertor targets, delivering uncertainty estimates that flag regions requiring additional simulations.

## Context
In AI‑driven plasma engineering, replacing slow high‑fidelity simulations with fast neural surrogates is a key challenge. This work shows how self‑supervised learning can deliver both accuracy and reliability in a setting where ground data are scarce, opening the door to automated optimization pipelines.

## Implications
Faster parameter scans reduce risk during tokamak operation, while real‑time uncertainty flags support adaptive control strategies. The approach enables digital twins that accelerate research and commercial deployment of advanced fusion devices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21407v1)
