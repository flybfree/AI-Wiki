---
title: Smooth Neural Point Processes via B-Splines
url: http://arxiv.org/abs/2607.21098v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_09-29-21Z_SmoothNeuralPointProcessesviaB_Splines.md
generated_at: 2026-07-23 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a neural TPP model that directly parametrizes the conditional intensity function using B-spline basis functions with neural network coefficients. This formulation allows exact negative log-likelihood evaluation and improves training efficiency compared to baseline methods.

## Key Takeaways
- The model defines the CIF as a non‑negative linear combination of B‑spline basis functions whose weights are learned by a neural network, enabling exact NLL computation.
- By using B‑splines the squared second derivative is naturally integrated, providing smoothness regularization without extra constraints on the architecture.
- Training can be parallelized because event contributions to the NLL are computed independently, unlike sequential baselines.

## Context
Temporal point processes are central to modeling events in continuous time and have driven advances in deep learning for sequential data. Recent neural TPP approaches often sacrifice flexibility or efficiency by approximating the compensator rather than the CIF directly.

## Implications
This approach offers a more efficient training pipeline that can be applied to real‑world event streams, potentially accelerating research and deployment of probabilistic temporal models. Practitioners may adopt B‑spline neural TPPs for better accuracy with less computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21098v1)
