---
title: Weak-to-Strong On-Policy Distillation
url: http://arxiv.org/abs/2607.26246v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_20-31-48Z_Weak_to_StrongOn_PolicyDistillation.md
generated_at: 2026-07-29 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Weak-to-Strong On-Policy Distillation (W2S-OPD) which improves a student model by using multiple weaker teacher models to create a proxy teacher in logit space. The student distills from this proxy, achieving performance that surpasses the original domain teacher and continues improving even with only weak supervision sources.

## Key Takeaways
- W2S-OPD builds a proxy teacher from contrast pairs of smaller models by extracting their logit differences, which isolates capability direction without requiring larger teachers.
- The student then minimizes per-token reverse KL on its own rollouts to align with the proxy teacher, yielding stronger performance than standard OPD.
- Different contrast types (post-RL vs pre-RL, scale vs hint) produce distinct signals: reasoning frameworks, solving procedures, or instance-level solutions.

## Context
On-policy distillation is a key technique for transferring knowledge across large language models, but current methods rely on unavailable larger teachers. W2S-OPD addresses this limitation by leveraging cheap, smaller models to generate effective teacher signals, making high-quality transfer feasible at student scale.

## Implications
This approach enables practitioners to achieve state-of-the-art results without costly training of larger models, democratizing access to advanced capabilities. It also highlights the importance of isolating specific skill directions in model training for targeted improvement.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26246v1)
