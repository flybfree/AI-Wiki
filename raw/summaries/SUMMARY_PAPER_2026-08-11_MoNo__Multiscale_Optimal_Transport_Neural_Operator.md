---
title: MoNo: Multiscale Optimal Transport Neural Operator for Solving PDEs on General Geometries
url: http://arxiv.org/abs/2608.09764v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_15-55-11Z_MoNo_MultiscaleOptimalTransportNeuralOperatorforSo.md
generated_at: 2026-08-11 12:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MoNo, a multiscale optimal transport neural operator that solves PDEs on arbitrary geometries with stable latent‑space construction. The core innovation is CoTAP, which treats cross‑scale assignments as entropy‑regularized optimal transport problems to balance token usage and prevent collapse in deeper layers.

## Key Takeaways
- CoTAP resolves assignment imbalance by formulating adjacency projections as an entropy‑regularized optimal transport problem, ensuring each latent token receives a balanced number of observations.  
- The method constructs bidirectional projections across scales, which stabilizes information flow and mitigates token collapse in hierarchical neural operators.  
- MoNo achieves superior prediction performance while maintaining computational efficiency compared to prior state‑of‑the‑art neural operator baselines.

## Context
Neural operators have become a dominant approach for translating high‑dimensional spatial data into function predictions, especially in physics‑informed machine learning. However, existing designs often suffer from unstable latent assignments that degrade model reliability on complex geometries.

## Implications
MoNo’s balanced assignment mechanism offers a robust framework for deploying neural operators across diverse domains such as fluid dynamics and image processing, where reliable long‑range interactions are critical. Practitioners can leverage this stability to build scalable models without sacrificing accuracy or speed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09764v1)
