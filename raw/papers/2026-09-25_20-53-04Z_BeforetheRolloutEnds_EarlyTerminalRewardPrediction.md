---
title: Before the Rollout Ends: Early Terminal Reward Prediction for Long-horizon Coding Agents
published: 2026-09-25T20:53:04Z
authors: Jihan Yao, Sihan Zeng, Shangbin Feng, Zhiyuan Fan, Banghua Zhu, Yulia Tsvetkov
url: http://arxiv.org/abs/2609.31995v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Before the Rollout Ends: Early Terminal Reward Prediction for Long-horizon Coding Agents

## Abstract
Long-horizon coding agents receive verifiable rewards only after completing expensive sequences of tool calls. This increases inference cost, amplifies early wrong hypotheses, and can lead to sparse terminal reward and unstable training. We introduce Contextual Early Reward (CER), which predicts terminal reward through behavioral evidence in a trajectory prefix. CER synthesizes adaptive rubrics specific to the current task and stage through experiences summarized from related historical tasks. In test-time scaling on SWE-bench Verified, CER improves RM@8 over the strongest baseline by 4.2 percentage points (pp) on Nemotron 3 Ultra and 2.0 pp on Qwen 3.6 27B; on Nemotron, it takes only 15.3% tokens to match the best baseline performance. In RL training experiments, CER exceeds full-rollout TMax by 1.9 pp while using 52.7% fewer online policy-and-judge tokens. Together, CER provides an interpretable, efficient, and dense evaluation method for long-horizon coding agents.

## Metadata
- **Published**: 2026-09-25T20:53:04Z
- **Authors**: Jihan Yao, Sihan Zeng, Shangbin Feng, Zhiyuan Fan, Banghua Zhu, Yulia Tsvetkov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31995v1)