---
title: RASP-QAOA: Resource-Aware Per-Instance Selection for Exact QAOA Simulation
url: http://arxiv.org/abs/2608.05646v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_06-41-41Z_RASP_QAOA_Resource_AwarePer_InstanceSelectionforEx.md
generated_at: 2026-08-06 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
RASP‑QAOA introduces a per‑instance selector that chooses among ten computational representations for exact QAOA simulation based on resource constraints and semantics. It succeeds on all admissible requests in a test set with high top‑1/2 performance, low regret relative to CUAOA, and demonstrates that representation features—not classifier complexity—drive the gains.

## Key Takeaways
- RASP‑QAOA first removes infeasible actions, then orders the remaining actions using instance features, handling unsupported ones analytically.  
- The method achieves 27/31 top‑1 and 31/31 top‑2 selection on a 60‑request H200 evaluation with geometric‑mean regret 1.051.  
- Its failure‑penalized PAR10 score is 0.0396 times that of CUAOA, indicating superior practical performance.

## Context
Exact QAOA simulation involves mapping quantum circuits to classical representations such as TensorFlow, PyTorch, or custom adapters, each with distinct memory and precision trade‑offs. Selecting a backend without considering these resources can lead to infeasible simulations, limiting the applicability of QAOA for real‑world problems.

## Implications
This resource‑aware selection framework enables practitioners to automatically match circuit requirements to available hardware constraints, improving both feasibility and efficiency of quantum algorithm simulations. As QAOA scales to deeper circuits and larger graphs, such adaptive selection will become essential for practical deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05646v1)
