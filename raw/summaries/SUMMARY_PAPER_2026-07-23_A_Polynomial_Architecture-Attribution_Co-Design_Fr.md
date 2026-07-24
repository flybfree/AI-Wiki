---
title: A Polynomial Architecture-Attribution Co-Design Framework for Exact Aumann-Shapley Attribution in GNNs
url: http://arxiv.org/abs/2607.21094v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_09-26-15Z_APolynomialArchitecture_AttributionCo_DesignFramew.md
generated_at: 2026-07-23 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces APEX, a model‑attribution co‑design framework that makes the Aumann–Shapley path integral computable exactly for graph neural networks. By employing PolyGIN, a GNN architecture whose message‑passing and transformation steps preserve bounded polynomial forms, the authors achieve exact quadrature evaluation with only 2^{L-1} deterministic points, outperforming standard numerical approximations.

## Key Takeaways
- The derivative along an attribution path has degree at most 2^L − 1 for a PolyGIN containing L polynomial transformation blocks.  
- Gauss–Legendre quadrature can evaluate the Aumann‑Shapley integral exactly up to floating‑point precision using 2^{L‑1} deterministic evaluation points.  
- PolyGIN retains competitive predictive performance while enabling exact attributions with far fewer evaluations than baseline methods.

## Context
Interpretable deep learning models often rely on path‑integral attribution techniques such as Integrated Gradients, which suffer from high computational cost due to numerical quadrature errors. Accurate explanations are essential for trustworthy AI systems, yet current approximations trade off fidelity and efficiency. This work addresses that gap by providing an exact solution within a tractable GNN design.

## Implications
The framework reduces the number of evaluation points needed for attribution dramatically, lowering inference latency without sacrificing interpretability. Practitioners can thus deploy explainable GNNs in real‑time applications where both performance and transparency are critical, fostering broader adoption of trustworthy AI solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21094v1)
