---
title: SkillCore: Internalizing Generalizable Skills via Scaffolding-Removed Fine-Tuning
published: 2026-11-24T09:23:45Z
authors: Yi Liu, Changqing Ai, Peijie Dong, Xiankun Lin, Yongkang Yang, Zhezheng Hao, Xilin Xia, Hande Dong, Qiang Lin, Qiang Xu
url: http://arxiv.org/abs/2611.32246v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillCore: Internalizing Generalizable Skills via Scaffolding-Removed Fine-Tuning

## Abstract
Runtime skills can improve agents' problem-solving capabilities by providing procedural guidance for tasks such as code review and debugging. However, these benefits reach only a minority of users, as most do not proactively invoke skills in practice. We argue that such generalizable procedures should become part of the model's capabilities rather than remain optional external add-ons, making them directly available without explicit skill loading. To this end, we present SkillCore, a data pipeline and supervised fine-tuning recipe for internalizing generalizable skills. We transform real agent trajectories by removing skill-loading scaffolding while preserving the task context and subsequent agent actions, thereby supervising direct execution without external skill content. To preserve access to task-specific skills that provide genuinely external information, we mix these scaffold-removed trajectories with a small proportion of skill-native trajectories that preserve supervision for skill invocation. On a held-out skill-free evaluation, SkillCore improves task completion quality over the base Qwen3-8B and Qwen2.5-72B models by 54.4% and 24.8%, respectively, while preserving task-specific skill invocation on a separate probe and general coding performance on SWE-bench Verified.

## Metadata
- **Published**: 2026-11-24T09:23:45Z
- **Authors**: Yi Liu, Changqing Ai, Peijie Dong, Xiankun Lin, Yongkang Yang, Zhezheng Hao, Xilin Xia, Hande Dong, Qiang Lin, Qiang Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.32246v1)