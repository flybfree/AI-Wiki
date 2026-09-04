---
title: Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning
url: http://arxiv.org/abs/2609.03667v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_11-04-23Z_Out_of_DistributionGeneralisationwithSequenceModel.md
generated_at: 2026-09-03 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates zero‑shot task generalisation in offline multi‑agent reinforcement learning by analysing how sequence models handle varying observation and action spaces across tasks. It finds that increasing the diversity of training tasks is more important than simply enlarging dataset size, achieving a 3.2× mean improvement on held‑out test tasks.

## Key Takeaways
- The dominant factor for robust zero‑shot transfer is scaling task diversity rather than dataset size.
- Multi‑task sequence models outperform single‑task approaches and strong behaviour cloning baselines across four environments.
- Varying agent counts within tasks further enhances generalisation performance.

## Context
Offline multi‑agent reinforcement learning struggles to apply learned policies to unseen tasks, limiting practical deployment. This work addresses a core gap by providing empirical evidence on how task diversity influences zero‑shot transfer in sequence models.

## Implications
Practitioners should prioritize generating diverse training distributions with different agent counts when building generalisable MARL agents. The findings offer a scalable roadmap for improving offline MARL performance and reducing reliance on extensive online data collection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03667v1)
