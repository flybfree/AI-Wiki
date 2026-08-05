---
title: Computing Actual Causes for Neural Network Predictions under Structured Causal Inputs
url: http://arxiv.org/abs/2608.03772v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_14-57-06Z_ComputingActualCausesforNeuralNetworkPredictionsun.md
generated_at: 2026-08-05 01:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a method for computing Halpern-Pearl actual causes of neural network predictions when input features are not independent, using Boolean structural causal models. It demonstrates that bound propagation and branch-and-bound can generate minimal cause sets efficiently, outperforming brute‑force and ILP baselines even on large search spaces up to 2.3×10¹³ candidate pairs within a 180‑second per instance budget.

## Key Takeaways
- The method models input dependencies with Boolean SCMs, allowing explanations that respect structural relationships rather than treating features as independent.
- Computation of HP causes is feasible for search spaces up to 2.3×10¹³ pairs using branch‑and‑bound, achieving completeness and minimality guarantees within a short runtime.
- Ignoring feature dependencies inflates the number of reported causes by about 14.9 %, many of which are spurious under the SCM.

## Context
Explainability in deep learning often relies on linear attribution models that ignore how features interact, leading to misleading or incomplete insights. This work addresses a fundamental gap by integrating causal structure into explanation pipelines, aligning with the need for trustworthy AI systems where inputs have known dependencies.

## Implications
For practitioners, this approach offers a scalable way to generate reliable minimal explanations, reducing noise and improving model interpretability. In industry, it can support compliance and safety assessments where understanding true cause‑effect relationships is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03772v1)
