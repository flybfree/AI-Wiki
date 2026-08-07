---
title: D-CLOT: Double Closed Loop Optimal Transport for Unsupervised Action Segmentation
url: http://arxiv.org/abs/2608.05877v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_10-59-28Z_D_CLOT_DoubleClosedLoopOptimalTransportforUnsuperv.md
generated_at: 2026-08-06 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes D-CLOT, a double closed loop optimal transport method for unsupervised action segmentation that addresses representation-prototype inconsistency. It improves over CLOT by re-estimating action prototypes from refined frame embeddings and using a graph-constrained module to preserve local geometry. The improvements are consistent across both variants, showing robustness of the refinement mechanisms.  

## Key Takeaways  
- The representation-prototype inconsistency, where prototypes evolve only via pseudo-label loss while frame geometry remains unchanged, is identified as a bottleneck for ambiguous transitions and short actions.  
- A graph-constrained module regularizes OT-refined representations by preserving encoder output neighborhood geometry, providing a stable reference for prototype updates.  
- Prototype refinement via k-means or OT barycenters, anchored to the stabilized geometry, yields assignment-aware updates that improve segment-level quality.  

## Context  
Unsupervised action segmentation is crucial for video analysis without labeled data, yet existing methods struggle with rare or ambiguous actions. Optimal transport offers a principled way to learn semantic similarity but lacks geometric consistency. These gains highlight a promising direction for scalable video understanding systems that rely on learned similarity metrics.  

## Implications  
This baseline on Assembly101 demonstrates that unsupervised refinement can significantly boost performance, offering practitioners a template for label-free segmentation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05877v1)
