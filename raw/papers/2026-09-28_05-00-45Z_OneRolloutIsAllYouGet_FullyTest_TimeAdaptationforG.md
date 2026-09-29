---
title: One Rollout Is All You Get: Fully Test-Time Adaptation for GUI Agents
published: 2026-09-28T05:00:45Z
authors: Ziqiang Wang, Li Gu, Zhixiang Chi, Linlian Jiang, Zihuan Jiang, Linqiang Guo, Siobhan Reid, Zhi Liu, Yang Wang
url: http://arxiv.org/abs/2609.34321v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Rollout Is All You Get: Fully Test-Time Adaptation for GUI Agents

## Abstract
GUI agents are deployed with frozen weights and discard everything they experience on the job. Existing ways to update an agent's weights assume something deployment withholds: ground truth, rollouts beyond the single attempt (retries, samples, practice runs), or a learning phase other than deployment. Because GUI actions can be irreversible, a deployed agent gets one attempt per task occurrence, in arrival order, and every attempt counts. No ground truth is available at any point. We define fully test-time adaptation for GUI agents by these constraints and pair it with a minimal weight-space method, SOLO. Auxiliary models read each episode: a judge selects the episodes it deems successful, and a proposer-verifier pair relabels a failed episode's prefix with the subtask that prefix completed. Admitted episodes enter a short sliding window, and each admission updates a small adapter by top-K self-distillation on the agent's own predictions, provided the window holds a judged success. On recurring task streams built from WebArena, VisualWebArena and MobileWorld, SOLO improves on the frozen agent with both UI-TARS-7B and Qwen3-VL-8B, by three to six points of success rate, and exceeds two in-setting memory methods on the web streams.

## Metadata
- **Published**: 2026-09-28T05:00:45Z
- **Authors**: Ziqiang Wang, Li Gu, Zhixiang Chi, Linlian Jiang, Zihuan Jiang, Linqiang Guo, Siobhan Reid, Zhi Liu, Yang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34321v1)