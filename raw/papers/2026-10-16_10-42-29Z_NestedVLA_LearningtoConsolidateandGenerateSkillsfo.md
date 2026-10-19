---
title: NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models
published: 2026-10-16T10:42:29Z
authors: Guodong Du, Wanyu Lin
url: http://arxiv.org/abs/2610.23271v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models

## Abstract
Vision--Language--Action (VLA) models promise generalist robotic agents, yet consolidating skills learned across heterogeneous tasks and environments remains difficult: training data is fragmented across platforms, joint multi-task training suffers from interference, and model merging tends to introduce parameter conflicts or require architectural changes. We instead advocate a paradigm in which skills are first learned independently and then consolidated post hoc. To this end, we propose NestedVLA, which replaces parameter aggregation with parameter generation: a nested hypernetwork, conditioned on the target task, synthesizes task-adaptive action-expert parameters that compose with a frozen base VLA. Task-specific compressed VLM residuals are retained separately. This formulation enables flexible task-conditioned skill reuse while mitigating interference. Across three RL benchmarks (MetaWorld, ManiSkill, CALVIN), NestedVLA outperforms the strongest model-merging baseline by 41 pp on average, matches per-task fine-tuning within 1 pp on ManiSkill, and substantially closes the gap on CALVIN, pointing toward a storage-efficient route to skill consolidation. Code is available at https://github.com/WanyuGroup/NeurIPS2026-NestedVLA.

## Metadata
- **Published**: 2026-10-16T10:42:29Z
- **Authors**: Guodong Du, Wanyu Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23271v1)