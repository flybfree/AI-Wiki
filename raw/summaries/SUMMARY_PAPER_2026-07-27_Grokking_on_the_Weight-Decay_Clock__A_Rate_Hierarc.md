---
title: Grokking on the Weight-Decay Clock: A Rate Hierarchy from Softly Broken Symmetries
url: http://arxiv.org/abs/2607.23967v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_03-30-44Z_GrokkingontheWeight_DecayClock_ARateHierarchyfromS.md
generated_at: 2026-07-27 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a theoretical framework that explains delayed generalization in linear models and neural networks trained with full-batch heavy-ball optimization and weight decay. It identifies an exact solvable relaxation mechanism tied to a grokking subspace where predictions stay constant while weight decay slowly restores them, leading to a predictable slow decay of population risk.

## Key Takeaways
- The training loss remains unchanged during the grokking phase because the model’s predictions lie in a population‑active component called the grokking subspace, leaving only weight decay as the restoring force.
- The exact relaxation rate is given by (1−β)/(ηλ) where β is the heavy‑ball parameter, η the step size and λ the regularization strength, matching empirical observations of delayed generalization.
- Only this subspace contributes to the slow asymptotic decay of population risk, so interventions that modify it can accelerate or delay grokking.

## Context
Delayed generalization, also known as grokking, has been observed in many deep‑learning experiments but lacks a unified theoretical explanation. This work bridges that gap by providing an exact solution for linear models and extending it to nonlinear networks via a locally quadratic extension of the relaxation law.

## Implications
Understanding the grokking clock helps practitioners design training regimes that avoid unnecessary long delays, such as adjusting optimizer parameters or regularization strength. It also offers causal predictions for how changes in weight decay affect generalization timelines, which could be applied to real‑world model deployment pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23967v1)
