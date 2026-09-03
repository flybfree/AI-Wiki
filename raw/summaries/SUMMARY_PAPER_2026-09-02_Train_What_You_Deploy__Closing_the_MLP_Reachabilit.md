---
title: Train What You Deploy: Closing the MLP Reachability Gap in Low-Rank Clone Distillation
url: http://arxiv.org/abs/2609.02006v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_02-32-14Z_TrainWhatYouDeploy_ClosingtheMLPReachabilityGapinL.md
generated_at: 2026-09-02 21:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses a mismatch between the weights a compressed student can deploy and those it can learn during training in low‑rank clone distillation. By aligning training with the full deployed matrix, the authors recover unused linear degrees of freedom without changing inference shape or FLOPs. Their method yields up to 10.45% accuracy improvement over baseline compressions while keeping token efficiency high.

## Key Takeaways
- The student’s deployment and its trainable weight family are initially misaligned, leaving a large portion of the deployed matrix’s independent linear degrees of freedom unreachable during training.
- Two mergeable realizations (Dense‑LRC and CORE‑LRC) collapse to a single deployed weight, preserving parameter count while expanding the reachable set.
- The approach recovers capacity: average gains of +2.36, +2.71, +10.45% over plain LRC baselines across three teachers, with the largest gain on Qwen.

## Context
Low‑rank clone distillation is a common technique for compressing large language models while preserving performance. Traditional methods often train only a subset of the teacher’s weights, leaving much of the deployed model’s capacity unused and underutilized.

## Implications
This work shows that training should match deployment to fully exploit compressed models, reducing waste in both parameters and compute. Practitioners can achieve higher accuracy with smaller student models, accelerating deployment and lowering resource costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02006v1)
