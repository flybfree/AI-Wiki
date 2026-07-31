---
title: Kalman Meets Curriculum: Efficient Dynamic Prompt Selection for Adaptive RL Finetuning
url: http://arxiv.org/abs/2607.27610v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_02-55-02Z_KalmanMeetsCurriculum_EfficientDynamicPromptSelect.md
generated_at: 2026-07-30 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Kalman-Guided Prompt Selection (KGPS), a method that treats prompt difficulty as a dynamic latent state and uses a linear‑Gaussian state‑space model to estimate it during reinforcement learning finetuning. By coupling process noise with policy update magnitude, KGPS captures uncertainty when the policy changes, allowing prompts to be chosen adaptively without extra rollouts. Experiments show KGPS reduces rollout usage by up to 83% and improves average performance by 0.12 points across several reasoning benchmarks.

## Key Takeaways
- KGPS models each prompt’s success rate in logit space with a linear‑Gaussian state‑space model, where process noise reflects the size of policy updates, so uncertainty rises when the policy shifts dramatically.  
- The Kalman filter maintains a calibrated Gaussian posterior over prompt difficulty, enabling selection that maximizes expected training utility and naturally revisits uncertain prompts.  
- The approach is fully online, requiring no additional rollouts beyond standard RL finetuning, and consistently outperforms evaluation‑based and stationary prediction baselines.

## Context
RL finetuning of large language models benefits from selecting prompts that match the model’s current reasoning capability, but existing methods either rely on costly evaluations or assume difficulty does not change during training. KGPS bridges this gap by treating prompt selection as a state‑estimation problem, aligning with the field’s push toward efficient, adaptive learning pipelines.

## Implications
For practitioners, KGPS offers a scalable way to fine‑tune LLMs without sacrificing compute resources, potentially lowering costs in large‑scale deployment. The method also provides insights into how policy dynamics affect prompt difficulty, informing future research on adaptive RL and curriculum design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27610v1)
