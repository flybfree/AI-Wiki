---
title: Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers
url: http://arxiv.org/abs/2609.01567v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-33-41Z_SelectiveAgentGuidanceviaEntropy_LearningAutonomou.md
generated_at: 2026-09-01 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SAGE, a method for learning autonomous reinforcement‑learning policies from Vision‑Language Models that act as costly and imperfect teachers. By querying the VLM only when uncertainty is high, SAGE distills guidance into a lightweight policy that outperforms both unguided RL and fixed VLM policies in several visual reasoning tasks.

## Key Takeaways
- SAGE queries the VLM only during training when the learner’s confidence is low, then uses those actions to improve its own policy.  
- The framework weights teacher guidance with environment‑derived advantages, allowing unreliable suggestions to be down‑weighted or ignored.  
- At evaluation, the learned policy can act without any VLM calls and often exceeds the performance of the original VLM teacher.

## Context
Vision‑Language Models are powerful but impractical as direct policies due to high query cost and lack of online learning. This work addresses the gap by showing that selective, entropy‑driven guidance can extract useful behavior from such models without constant interaction, aligning with trends toward efficient, self‑improving agents.

## Implications
For industry practitioners, SAGE offers a way to integrate costly vision expertise into reinforcement systems while minimizing real‑time VLM usage. Practitioners can adopt this approach to build scalable autonomous agents that leverage external knowledge only when needed, reducing latency and cost in deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01567v1)
