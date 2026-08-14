---
title: SSPO: Structure-Aware Similarity-Weighted Preference Optimization for Neural Combinatorial Optimization
url: http://arxiv.org/abs/2608.12443v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_16-04-54Z_SSPO_Structure_AwareSimilarity_WeightedPreferenceO.md
generated_at: 2026-08-13 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SSPO, a structure‑aware similarity‑weighted preference optimization method for neural combinatorial optimization. It addresses two known issues: gradient signal polarization and baseline redundancy by using a leave‑one‑out baseline that scores all sampled solutions with a dissimilarity weight. Experiments on TSP, EFL, and JSP show consistent improvements over prior methods.

## Key Takeaways
- SSPO resolves gradient signal polarization by assigning higher weights to structurally distinct peers in the training set.  
- It eliminates baseline redundancy through a zero‑parameter, problem‑adaptive embedding that scores each solution based on similarity to the others.  
- The method yields consistent gains across TSP, EFL, and JSP benchmarks compared with anchor and uniform‑weight baselines.

## Context
Neural combinatorial optimization struggles to leverage the full diversity of co‑sampled solutions during training. Existing preference‑optimization approaches often ignore fine‑grained structural signals, limiting performance. SSPO’s approach offers a principled way to balance diverse inputs without extra parameters.

## Implications
For practitioners, SSPO provides a scalable framework that can be integrated into existing NCO pipelines with minimal overhead. Its practical deployment in JD.com’s facility‑location system demonstrates real‑world impact, encouraging broader adoption of structure‑aware training strategies across industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12443v1)
