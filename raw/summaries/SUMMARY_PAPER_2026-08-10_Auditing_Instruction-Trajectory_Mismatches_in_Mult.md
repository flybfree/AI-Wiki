---
title: Auditing Instruction-Trajectory Mismatches in Multimodal Robot Demonstrations
url: http://arxiv.org/abs/2608.07895v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_03-43-58Z_AuditingInstruction_TrajectoryMismatchesinMultimod.md
generated_at: 2026-08-10 22:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a training‑free auditing method called Multimodal Probabilistic Fusion (MMPF) to detect Instruction‑Trajectory Mismatches (ITMs), where robot trajectories are correct but paired with the wrong language instruction. Across several benchmarks, MMPF outperforms existing approaches in detecting and correcting these mismatches, and it also improves downstream policy learning when language is needed for task disambiguation.

## Key Takeaways
- MMPF treats each modality as an expert, estimating a task‑label distribution from local neighborhood agreement and global prototype similarity.  
- The framework fuses modalities using predictive‑entropy weighting in a product of experts, enabling robust detection even when individual modalities are noisy.  
- Experiments show that auditing with MMPF yields higher overall ITM detection accuracy and better label correction than relabeling or filtering demonstrations.

## Context
Instruction‑Trajectory Mismatches pose a subtle failure mode for multimodal robot demonstration datasets, which can mislead vision‑language‑action policies by associating incorrect language with valid actions. Detecting such mismatches is crucial because they may corrupt the learned language‑behavior mapping without obvious rollout failures.

## Implications
For AI practitioners, MMPF offers an automated way to keep multimodal training data trustworthy, reducing downstream errors and improving robot performance in real‑world settings where language guidance is essential. This method also highlights a trade‑off between filtering demonstrations and relabeling, guiding efficient data curation strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07895v1)
