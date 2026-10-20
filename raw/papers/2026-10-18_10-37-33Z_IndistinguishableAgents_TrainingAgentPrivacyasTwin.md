---
title: Indistinguishable Agents: Training Agent Privacy as Twin-World Indistinguishability
published: 2026-10-18T10:37:33Z
authors: Jiaming He, Guanyu Hou, Yi Yu, Xudong Jiang
url: http://arxiv.org/abs/2610.25161v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Indistinguishable Agents: Training Agent Privacy as Twin-World Indistinguishability

## Abstract
LLM agents search, shop and send messages for their users, and every action is seen by some party. Existing privacy training rewards agents for not mentioning protected items, yet an observer can infer a private fact from what the agent does. Since an observer learns a fact only if its view changes with the fact, we propose \methodfull (\method), which trains on twin worlds that differ only in the private fact. A frozen distinguisher scores each observer's view by its log-likelihood ratio for the true world, and paired GRPO trains the agent on task success minus this ratio. We prove that this objective controls the Bayes success of every observer on every channel. On shopping and messaging tasks \method removes the leakage that disclosure judges and query-level rewards miss, while the agent still completes its tasks.

## Metadata
- **Published**: 2026-10-18T10:37:33Z
- **Authors**: Jiaming He, Guanyu Hou, Yi Yu, Xudong Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25161v1)