---
title: A Wrong Turn Does Not Ruin the Journey: Deviation-Guided Skill Self-Evolution for LLM Agents
published: 2026-09-24T07:31:00Z
authors: Yichun Feng, Jiawei Wang, Haozhe Sun
url: http://arxiv.org/abs/2609.29154v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Wrong Turn Does Not Ruin the Journey: Deviation-Guided Skill Self-Evolution for LLM Agents

## Abstract
Large language model agents increasingly rely on natural-language skills to solve complex tool-use tasks. However, such tasks often admit multiple valid solution paths, making it inappropriate to improve skills by forcing failed trajectories to match a fixed successful trajectory. Moreover, failed trajectories are rarely entirely wrong: an agent may first collect useful evidence and make meaningful progress, but later deviate into an erroneous suffix. We therefore argue that skill self-evolution should identify where productive problem solving begins to break down, rather than reflect coarsely over the entire failure. Based on this insight, we propose SkillPivot, a deviation-point-guided framework for skill self-evolution. SkillPivot detects the transition from a useful prefix to an erroneous suffix using execution validity, goal progress, and action diversity. A stronger teacher then continues from the same prefix and produces a successful alternative under the same interaction history. By contrasting the student's failed suffix with the teacher's successful suffix, SkillPivot generates localized skill updates while preserving already effective guidance. Experiments on ToolQA, LogicBench, and WildClawBench show that SkillPivot consistently outperforms competing skill-evolution methods, improves multiple agent models, and produces compact, transferable skill updates.

## Metadata
- **Published**: 2026-09-24T07:31:00Z
- **Authors**: Yichun Feng, Jiawei Wang, Haozhe Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29154v1)