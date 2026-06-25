---
title: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
url: http://arxiv.org/abs/2606.26091v1
type: paper-summary
date: 2026-06-24
source_paper: 2026-06-24_17-59-02Z_On_PolicySelf_DistillationwithSampledDemonstration.md
generated_at: 2026-06-24 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces on-policy self-distillation using sampled demonstrations and shows it improves pass@1 accuracy but reduces rollout diversity. It finds that the teacher’s feedback is biased by the chosen correct rollout, flattening performance curves beyond a point. The analysis reveals that optimal self‑distillation can amplify probability gaps between rollouts.

## Key Takeaways
- The method uses a single model as both teacher and student, conditioning on a sampled correct rollout to generate token‑level feedback.
- This creates compounding biases that tilt the base distribution, causing fewer diverse rollouts to be generated despite high accuracy.
- As a result, pass@k curves flatten because generating more rollouts no longer yields better performance.

## Context
Self‑distillation is an emerging technique for fine‑tuning large language models without external data. The paper’s analysis highlights how design choices in the teacher can unintentionally degrade model diversity. This matters as diverse strategies are crucial for real‑world tasks that require varied solutions.

## Implications
For practitioners, the findings warn against relying solely on self‑distillation for robust generation. Industries should consider alternative methods that preserve rollout diversity when training or fine‑tuning models. The trade‑off between accuracy and diversity underscores the need for careful evaluation of model behavior beyond single metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.26091v1)
