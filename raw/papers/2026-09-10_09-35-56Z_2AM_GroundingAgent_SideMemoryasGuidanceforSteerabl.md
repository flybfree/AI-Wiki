---
title: 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation
published: 2026-09-10T09:35:56Z
authors: Yutong Hu, Fengjiao Chen, Xuezhi Cao, Renaud Detry
url: http://arxiv.org/abs/2609.11308v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation

## Abstract
Long-horizon robot manipulation requires memory, but not necessarily inside the action policy. To address such tasks, current agentic systems often combine VLAs with planners and geometric tools, sometimes using additional depth or calibrated geometry. These systems confound attribution: gains may come from richer observations or alternative motor tools, while failures may stem from either the policy or an under-specified language interface. We isolate this question through a deliberately constrained design: less tool breadth, but greater interface bandwidth. 2AM makes a multimodal Agent the sole holder of task memory and a single RGB-based, episodically stateless Action Model the sole executor of task-relevant motion. The Agent compiles interaction history into subtask language and optional 2D grasp, place, and move hints that bind its physical intention at different time scales. To teach this steerability to the VLA, we augment demonstrations with structured hint labels and train under condition dropout, spatial noise, and temporal jitter to tolerate imperfect Agent outputs. On LIBERO-Mem, without depth, online geometry, or planner-based object motion, 2AM reaches 76.3% average completion, a 61.5-point improvement over the strongest reported baseline of 14.8%, together with 63.0% relaxed and 11.8% strict success. These results show that task memory can remain Agent-side. They further show that Action Model capability depends not only on what the policy has learned, but on how precisely the Agent can steer it.

## Metadata
- **Published**: 2026-09-10T09:35:56Z
- **Authors**: Yutong Hu, Fengjiao Chen, Xuezhi Cao, Renaud Detry
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11308v1)