---
title: SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation
url: http://arxiv.org/abs/2608.05970v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_12-46-13Z_SkillMemo_Expert_guidedSkillMemoryFrameworkforComp.md
generated_at: 2026-08-06 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SkillMemo, a framework that decomposes long‑horizon robotic manipulation demonstrations into latent atomic skills and stores them in a dynamic episodic memory bank to improve compositional generalization. By integrating skill‑level features with the model’s gating distribution, SkillMemo enhances both Diffusion Policy and Vision‑Language‑Action backbones, achieving state‑of‑the‑art performance on benchmark tasks.

## Key Takeaways
- The MoE segmentation module implicitly partitions trajectories into distinct skill primitives via learned gating coefficients.  
- A compact episodic memory bank stores key‑value pairs representing these skills for fast retrieval during inference.  
- Experiments show SkillMemo consistently improves DP and VLA models, outperforming the baseline π0.5 and demonstrating strong compositional generalization to unseen tasks.

## Context
In embodied AI, large‑scale trajectory datasets remain scarce, limiting the ability of vision‑language‑action systems to generalize across diverse manipulation tasks. This work addresses that bottleneck by providing a memory‑driven mechanism that learns reusable skill structures without requiring massive labeled data.

## Implications
For robotics developers, SkillMemo offers a practical way to augment existing models with learned primitives, reducing reliance on exhaustive dataset collection. Industries can leverage this framework to create adaptable humanoid robots capable of performing complex tasks from limited demonstrations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05970v1)
