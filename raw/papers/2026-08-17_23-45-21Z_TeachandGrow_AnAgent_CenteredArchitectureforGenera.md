---
title: Teach and Grow: An Agent-Centered Architecture for General Robot Learning
published: 2026-08-17T23:45:21Z
authors: Chang Nie, Zhe Liu, Hesheng Wang
url: http://arxiv.org/abs/2608.17209v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Teach and Grow: An Agent-Centered Architecture for General Robot Learning

## Abstract
End-to-end vision-language-action (VLA) and world-action models offer an elegant route to general-purpose robotics, but their reliability is bounded by validated physical coverage. When an unfamiliar object, sensor, embodiment, or contact falls outside that coverage and no validated fallback exists, correcting the failure requires new robot data, a policy update, and regression testing. This recurring burden is the retraining tax. Unlike text, embodied data must often be created by operating machines. We present Teach-and-Grow Learning (TGL), an agent-centered architecture for general robot learning. In its general form, a multimodal agent turns a few successful demonstrations into reusable Skill Blocks: closed-loop behaviors for meaningful subgoals. In a new scene, the agent grounds and composes these blocks, selects learned or geometric tools, observes the physical outcome, and revises the route when execution departs from intent. A Skill Library stores executable behavior, while structured Experience Memory carries forward success, failure, and repair. New tasks are acquired without task-specific policy retraining. Our LIBERO evaluation attains state-of-the-art performance; controlled studies expose skill induction, persistent reuse, and agent-directed adaptation. Finally, we propose the Teach-and-Grow scaling-law hypothesis: if X denotes effective reusable experience, future-task error and teaching demand should approach irreducible floors as power laws in X. The architecture therefore treats deployment as a period of continued learning, in which one task can make the next easier.

## Metadata
- **Published**: 2026-08-17T23:45:21Z
- **Authors**: Chang Nie, Zhe Liu, Hesheng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17209v1)