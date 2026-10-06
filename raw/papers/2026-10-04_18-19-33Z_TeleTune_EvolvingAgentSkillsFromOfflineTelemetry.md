---
title: TeleTune: Evolving Agent Skills From Offline Telemetry
published: 2026-10-04T18:19:33Z
authors: Justin Chih-Yao Chen, Elias Stengel-Eskin, Yan Chen, Pol Llado, Scott Counts, Mohit Bansal, Benjamin Van Durme, Harsh Jhamtani, Gaurav Verma
url: http://arxiv.org/abs/2610.05437v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TeleTune: Evolving Agent Skills From Offline Telemetry

## Abstract
Computer-use agents need to capture procedural knowledge of how people use software. User telemetry offers a scalable source of this knowledge. However, learning reusable skills from these logs requires addressing three challenges: (1) Goal Underspecification, since logs do not record the goal behind each action; (2) Non-Replayability, since past activity cannot be replayed to evaluate skill updates; and (3) Interleaved Trajectories, since logs may mix several tasks without marking their boundaries. To address these, we introduce TeleTune, a framework for learning a textual skill library from offline logs without recorded goals, cannot be replayed during optimization, and may interleave tasks. TeleTune uses action-prediction errors on logged trajectories to propose library edits and keep only those that improve held-out action-prediction accuracy, which we call skill-guided progress. The learned workflows also enable retrieval of demonstrations that cover the subgoals of a new task. At test time, the agent is provided with the learned library and the workflow-based retrieved demonstrations. Experiments on WorkArena and Online-Mind2Web show that TeleTune outperforms random retrieval, Agent Workflow Memory (AWM), and their combination. We find that the best baseline varies by setting, whereas TeleTune achieves average success rates of 77.1% and 80.6%, respectively, improving over the strongest baseline on each benchmark by 6.7% and 7.7%. Under the heaviest perturbation of the WorkArena training data,TeleTune keeps the highest average success rate at 68.5%, 6.3% above the strongest baseline. Our analyses show (1) skill optimization and workflow-based retrieval are complementary, (2) optimizing on fixed logs costs 5 to 75 times fewer tokens than validating the same edits with live episodes, (3) skill-guided progress tracks the live success rate.

## Metadata
- **Published**: 2026-10-04T18:19:33Z
- **Authors**: Justin Chih-Yao Chen, Elias Stengel-Eskin, Yan Chen, Pol Llado, Scott Counts, Mohit Bansal, Benjamin Van Durme, Harsh Jhamtani, Gaurav Verma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05437v1)