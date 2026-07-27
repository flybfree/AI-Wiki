---
title: Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents
url: http://arxiv.org/abs/2607.22157v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_10-01-00Z_LearningontheJob_ContinualLearningfromDeploymentFe.md
generated_at: 2026-07-26 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a continual learning framework that extracts feedback from frozen AI agents to improve performance without retraining the model. By converting each episode’s outcome verdict and correction into retrievable natural‑language rules stored in an external memory, the system can adapt its behavior over time. Experiments on the τ‑bench banking domain show that learning from a single‑bit verdict boosts success rates by 1.6× compared to static retrieval, while corrections raise it to 2.6× and enable solving tasks previously unsolvable.

## Key Takeaways
- The system learns from one‑bit outcome verdicts, achieving a 1.6× improvement over baseline static RAG.
- Learning from after‑the‑fact corrections yields a 2.6× boost and unlocks 22 previously unsolvable tasks.
- Memory accumulation transfers between models, each outperforming its own no‑memory baseline.

## Context
AI agents often freeze weights at deployment, missing learning opportunities; this work shows feedback can be harnessed to improve behavior over time. The approach leverages external memory to store distilled rules, enabling continual adaptation without model updates.

## Implications
Provides scalable continual learning for deployed systems, especially for organizations with data sovereignty constraints using open‑weights models. Practitioners can integrate feedback into existing pipelines to enhance performance and unlock new capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22157v1)
