---
title: 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question Answering
url: http://arxiv.org/abs/2608.01185v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_12-11-51Z_3DZip_Spatial_AwareFeatureDiversity_GuidedTokenCom.md
generated_at: 2026-08-03 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces 3DZip, a three-stage token compression framework for 3D vision-language models that reduces the massive number of geometry‑aware tokens generated per scene while preserving spatial coherence. Experiments on three 3D question answering benchmarks show that 3DZip retains 94.7% of original performance with only 128 tokens and speeds up inference by a factor of 1.92.

## Key Takeaways
- coarse voxelization removes point‑level redundancy, significantly shrinking the token count before any further selection.
- anchor tokens are chosen based on feature‑space diversity using a Determinantal Point Process, ensuring a diverse set of representative tokens is retained.
- merging remaining tokens under spatial constraints preserves geometric coherence, preventing loss of relational information.

## Context
3D vision‑language models generate thousands of tokens per scene to support spatial reasoning, which incurs high computational and memory costs. Existing compression techniques depend on semantic relevance or attention mechanisms that ignore the structured nature of 3D token representations, leading to residual redundancy and imbalance at the object level.

## Implications
Efficient 3D VQA systems can now run on limited hardware without sacrificing accuracy, opening possibilities for real‑time applications such as autonomous navigation and augmented reality. Practitioners can adopt this framework to design scalable pipelines that balance speed, memory usage, and performance in large‑scale 3D reasoning tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01185v1)
