---
title: Harness Annealing: Learning to Act with Less External Control
published: 2026-10-01T07:35:39Z
authors: Yingxuan Yang, Huacan Chai, Ying Wen
url: http://arxiv.org/abs/2610.01235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harness Annealing: Learning to Act with Less External Control

## Abstract
Language agents rely on external harnesses to track state, organize workflows, and verify answers. Beyond providing tools and information, these harnesses supply control decisions about what to investigate, whether to revise, and when to stop. Training on successful harness-supported trajectories can improve task performance while leaving these decisions dependent on runtime intervention. We ask whether harness-supported experience can also teach the model to make these decisions, allowing the division of control to change as the model learns. We call this objective harness internalization: learning to assume specified control responsibilities while retaining task performance after the corresponding support is withdrawn. We introduce HARNESS ANNEALING TRAINING (HAT), which combines explicit control supervision with a curriculum over teacher trajectories collected under progressively weaker harnesses. Experiments with 9B and 35B models on SWE-QA and SWE-QA-Pro evaluate every checkpoint under four deployment harnesses. Selected annealed checkpoints operating with tools alone achieve scores close to those of their respective starting checkpoints deployed with the full harness. The benefits vary with model scale and deployment configuration, and further annealing does not uniformly improve performance. These findings suggest that harness-supported experience can help reduce the runtime control required by a trained agent.

## Metadata
- **Published**: 2026-10-01T07:35:39Z
- **Authors**: Yingxuan Yang, Huacan Chai, Ying Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01235v1)