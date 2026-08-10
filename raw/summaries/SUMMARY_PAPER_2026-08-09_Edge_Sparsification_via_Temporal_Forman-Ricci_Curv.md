---
title: Edge Sparsification via Temporal Forman-Ricci Curvature for Dynamic Graph Learning
url: http://arxiv.org/abs/2608.07158v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_12-26-15Z_EdgeSparsificationviaTemporalForman_RicciCurvature.md
generated_at: 2026-08-09 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TRicci, a network-curvature-inspired edge sparsification framework for dynamic graph learning that extends Forman-Ricci curvature to capture structural support, temporal recency and local competition. Experiments on transaction networks show 80% sparsification with 55.94% reduction in training/inference time while preserving predictive performance across nine tasks.

## Key Takeaways
- TRicci achieves approximately 80% edge removal, dramatically shrinking the graph size without harming downstream predictions.
- The framework reduces end-to-end training and inference time by an average of 55.94%, highlighting computational gains.
- Temporal curvature is shown to preserve predictive temporal-structural information under such aggressive sparsification.

## Context
Temporal graph learning aims to model evolving networks where edges appear, disappear or change weight over time. Conventional methods struggle with dense graphs due to high memory and compute costs, limiting scalability to real-world applications like finance and social media.

## Implications
This work demonstrates that curvature-based sparsification can be a viable strategy for large-scale temporal data, enabling faster inference and lower resource usage. Practitioners can adopt TRicci to build efficient models without sacrificing accuracy, fostering broader adoption in industry where real-time performance is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07158v1)
