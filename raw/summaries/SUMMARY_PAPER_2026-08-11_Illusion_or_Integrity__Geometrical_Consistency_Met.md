---
title: Illusion or Integrity? Geometrical Consistency Metric for AIGC Video Quality Evaluation
url: http://arxiv.org/abs/2608.09594v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_13-28-07Z_IllusionorIntegrity_GeometricalConsistencyMetricfo.md
generated_at: 2026-08-11 12:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GeoCon‑Bench, a quantitative metric that assesses the geometric consistency of AI‑generated video sequences by measuring adherence to physical laws across frames. The benchmark evaluates global motion through translation estimation and homography fitting, reporting inlier ratios and geometric errors as proxies for fidelity to real‑world physics. Experiments on state‑of‑the‑art AIGC models show that GeoCon‑Bench reliably distinguishes high‑quality from low‑quality outputs.

## Key Takeaways
- The metric quantifies how well generated videos respect physical principles by fitting homographies or fundamental matrices to background correspondences, providing an objective measure of geometric consistency.  
- It captures global motion via translation estimation and reports complementary metrics such as inlier ratio and geometric error, enabling systematic comparison across different video quality levels.  
- The released dataset includes 20 scenes spanning six motion categories, offering a comprehensive benchmark for evaluating AIGC video generation.

## Context
The rapid advancement of AI‑driven video creation has outpaced existing evaluation tools that focus on visual harmony or textual alignment without probing physical realism. This gap hampers model optimization and limits trust in synthetic content. GeoCon‑Bench fills this void by introducing a physics‑aware assessment framework that aligns with the need for rigorous, reproducible quality metrics.

## Implications
For researchers, GeoCon‑Bench provides a standardized benchmark to guide improvements in motion synthesis and depth consistency. Industry practitioners can leverage it to evaluate and market AIGC video products, ensuring they meet realistic expectations of motion fidelity. The metric’s emphasis on geometric integrity could become a de facto standard for assessing synthetic media quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09594v1)
