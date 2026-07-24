---
title: ReGuide: From Test-Time Guidance to Self-Improving Diffusion Policies
url: http://arxiv.org/abs/2606.28939v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-06-27_14-23-21Z_ReGuide_FromTest_TimeGuidancetoSelf_ImprovingDiffu.md
generated_at: 2026-07-23 23:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
ReGuide proposes a self‑improving diffusion policy that uses test‑time guidance to generate corrective rollouts and then absorbs those successes back into the model. The framework improves success rates on several benchmark tasks by up to seven times compared with baseline behavior cloning, showing that guided recovery data can be reused for fine‑tuning or full retraining.

## Key Takeaways
- ReGuide treats successful guided rollouts as reusable on‑policy recovery data, allowing the policy to improve without extra exploration. 
- The method limits guidance to drifted but recoverable states using phase‑specific latent targets, preventing unnecessary correction of already correct trajectories. 
- Fine‑tuning (ReGuide‑FT) or full retraining (ReGuide‑FS) on the augmented dataset can be composed iteratively, yielding cumulative gains.

## Context
Diffusion policies are widely used for generative tasks but struggle with covariate shift between training and test environments. Current solutions either require costly expert corrections or discard corrected trajectories after use, limiting practical deployment.

## Implications
For practitioners, ReGuide offers a cost‑effective way to boost model performance in real‑world settings where data drift is inevitable. The approach could be integrated into automated pipelines that continuously adapt policies without manual retraining cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.28939v1)
