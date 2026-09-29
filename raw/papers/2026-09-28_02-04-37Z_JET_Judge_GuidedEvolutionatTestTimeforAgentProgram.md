---
title: JET: Judge-Guided Evolution at Test Time for Agent Programs
published: 2026-09-28T02:04:37Z
authors: Yao Long Teng, Jiayi Cai, Bo An
url: http://arxiv.org/abs/2609.34126v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JET: Judge-Guided Evolution at Test Time for Agent Programs

## Abstract
An agent's executable program governs how it uses tools, processes observations, and responds to failures. Evolving this program at test time can help adaptation, but deciding which changes to retain is difficult when true rewards are unavailable. Execution traces provide evidence of agent behavior, yet interpreting that evidence requires a judge that remains useful as tasks and candidate programs change. We introduce Judge-Guided Evolution at Test Time (JET), which evolves an executable judge on labeled source trajectories, then freezes and transfers it to guide target-side program evolution. The judge supplies scores and diagnostic feedback without target evaluator access or model-weight updates. On unseen WebShop tasks, JET achieves approximately 13% higher mean reward than fixed-rubric guidance when evolution begins from an unevolved program (cold start) and 4% higher when it begins from one already optimized on source tasks (warm start), with a 36% relative improvement in cold-start exact success. An exact-judge control on PushT, where the judge reconstructs the scoring rule from observations, shows that without judge error, program search becomes the bottleneck. Analyses identify useful reward-prediction logic in the evolved code and show that better final selection alone cannot explain the gains. These results support executable judge transfer for program adaptation under evaluator-preserving task shifts.

## Metadata
- **Published**: 2026-09-28T02:04:37Z
- **Authors**: Yao Long Teng, Jiayi Cai, Bo An
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34126v1)