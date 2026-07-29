---
title: Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control
published: 2026-07-28T06:38:16Z
authors: Jiaxin Bai, Jiaxuan Xiong
url: http://arxiv.org/abs/2607.25337v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control

## Abstract
Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space rather than reconstructing pixels, making them a natural backbone for latent model predictive control from offline demonstration logs. JEPA-style training optimizes short-horizon latent prediction, whereas planning requires a multi-step ranking of imagined futures by goal progress. Prior JEPA planners often inherit that ranking from embedding geometry, typically latent Euclidean distance, which arises as a byproduct of representation learning rather than as a progress cost mined from the logs. We propose temporal-distance JEPA (TD-JEPA), which retains the LeWM encoder--predictor backbone and mines a directed temporal cost from reward-free trajectories: same-trajectory step order supplies positive targets, cross-trajectory pairs act as heuristic negatives, and a rollout-consistency term matches the planner horizon. The mined supervision serves two roles: as the deployed planning cost when progress is topological, and as a representation signal that improves Euclidean planning when contact geometry dominates. Under locked evaluation, deploying the mined cost raises Two-Room success to 100.0% versus LeWM's 97.4%, while shared Euclidean planning on the same temporally trained checkpoint raises OGB-Cube by 14.2 points over LeWM and improves Push-T. Against LeWM and the concurrent RC-aux baseline under locked evaluation, TD-JEPA matches or exceeds both methods on every environment. Ablations show that the directed head, cross-trajectory negatives, and rollout consistency each contribute. TD-JEPA narrows the train--plan gap for JEPA world-model planners by discovering temporal progress structure in offline logs and co-designing cost form with plan-time deployment. Code is available at https://github.com/HKBU-KnowComp/TD-JEPA.

## Metadata
- **Published**: 2026-07-28T06:38:16Z
- **Authors**: Jiaxin Bai, Jiaxuan Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25337v1)