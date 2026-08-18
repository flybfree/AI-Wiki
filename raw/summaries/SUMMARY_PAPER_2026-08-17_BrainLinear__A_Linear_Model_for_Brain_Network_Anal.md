---
title: BrainLinear: A Linear Model for Brain Network Analysis in Sparse Tangent Subspaces
url: http://arxiv.org/abs/2608.15266v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_14-57-48Z_BrainLinear_ALinearModelforBrainNetworkAnalysisinS.md
generated_at: 2026-08-17 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BrainLinear, a lightweight geometry-aware model that extracts disease-relevant connectivity patterns from functional connectomes. Experiments on ABIDE and ADNI show it matches or exceeds GNN and Transformer baselines while reducing computational cost dramatically.

## Key Takeaways
- BrainLinear maps each connectivity matrix to a shared tangent space centered at the Fréchet mean, preserving subject-specific deviations without full matrix representation.
- It scores ROI-pair tangent directions by classification contribution and disease-control difference, selecting only Top-K directions for compact representation.
- The model achieves up to 3.54 percentage point AUC improvement over the best baseline while cutting runtime and GPU memory usage by 84% and 68% respectively.

## Context
Current brain network analysis relies on heavyweight graph neural networks that process massive connectivity matrices, leading to high computational demands and limited interpretability. This work demonstrates that geometry-aware linear models can capture meaningful patterns with far less overhead, aligning with the push for efficient AI in neuroimaging.

## Implications
For researchers, BrainLinear offers a practical tool to uncover interpretable connectivity signatures without sacrificing performance. Clinically, it enables faster screening of disease-relevant networks, potentially accelerating diagnostic pipelines and reducing resource costs in large-scale studies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15266v1)
