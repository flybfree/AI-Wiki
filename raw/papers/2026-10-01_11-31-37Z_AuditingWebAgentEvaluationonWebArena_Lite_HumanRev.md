---
title: Auditing Web Agent Evaluation on WebArena-Lite: Human Review of Outcomes and Trajectories
published: 2026-10-01T11:31:37Z
authors: Chengguang Gan, Zimeng He, Yoshihiro Tsujii, Ken-ichiro Kobayashi, Hiroki Itoh, Kotaro Funakoshi
url: http://arxiv.org/abs/2610.01491v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Web Agent Evaluation on WebArena-Lite: Human Review of Outcomes and Trajectories

## Abstract
Web agents are an important application of large language models, yet their evaluation often depends on rule based or language model evaluators that inspect only the final outcome. Human verification of task completion and detailed analysis of failed trajectories remain limited. We audit all 165 WebArena Lite tasks under six evaluation conditions built from GPT 5.5 and an untrained Qwen3.5 9B model. The audit retains the original score, corrects false negatives from the automatic evaluator, identifies the first consequential error, and examines progress across the trajectory. We also study a Memory and Analysis Support Mechanism (MASM), which maintains explicit execution state, and Guide Text, which provides task relevant procedural guidance. Across four GPT 5.5 settings, human review recovers 5.45 to 8.49 percentage points of success missed by the evaluator. With a 25 step budget, Guide Text raises corrected success with MASM from 34.55% to 38.18%. On the untrained Qwen3.5 9B model, MASM raises the evaluator score from 13.90% to 18.80%. Review of 102 failed GPT 5.5 trajectories reveals frequent scrolling loops, unfinished exploration, premature answers, invalid actions, and incomplete form workflows. Step level evidence further shows that substantial early progress can coexist with a final failure. These results show why final scores alone provide an incomplete account of web agent behavior and motivate human grounded, trajectory aware verification.

## Metadata
- **Published**: 2026-10-01T11:31:37Z
- **Authors**: Chengguang Gan, Zimeng He, Yoshihiro Tsujii, Ken-ichiro Kobayashi, Hiroki Itoh, Kotaro Funakoshi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01491v1)