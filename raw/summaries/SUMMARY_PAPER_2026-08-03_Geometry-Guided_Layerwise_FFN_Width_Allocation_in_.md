---
title: Geometry-Guided Layerwise FFN Width Allocation in Transformers
url: http://arxiv.org/abs/2608.02064v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_11-08-58Z_Geometry_GuidedLayerwiseFFNWidthAllocationinTransf.md
generated_at: 2026-08-03 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a geometry‑guided method for allocating width across layers of feed‑forward networks in Transformers based on forward‑pass measurements. It uses geometric metrics such as Gromov‑Wasserstein distortion and persistent homology to estimate layer behavior and then optimizes width under a fixed budget. The experiments show that normalized geometric work often front‑loads capacity, improving validation loss compared with uniform or cosine schedules.

## Key Takeaways
- Normalized Euclidean work is predominantly front‑loaded across layers, indicating early layers benefit most from larger widths.
- Gromov‑Wasserstein distortion correlates more strongly with perturbation‑based layer sensitivity than finite‑sample topological estimates.
- At 440M parameters the geometry‑based allocation outperforms both uniform width and a cosine taper by a substantially larger margin.

## Context
Transformer feed‑forward layers dominate model size, yet their widths are typically fixed, limiting parameter efficiency. Recent work explores dynamic allocation to match computational resources with actual layer complexity. This study advances that line of inquiry by grounding decisions in observable geometric properties of token representations.

## Implications
Dynamic width scheduling can reduce memory and compute costs while preserving performance, offering a path toward more scalable language models. Practitioners may adopt these geometry‑based schedules to fine‑tune large pretrained systems without retraining from scratch.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02064v1)
