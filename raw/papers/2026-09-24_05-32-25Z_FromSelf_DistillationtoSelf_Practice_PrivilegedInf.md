---
title: From Self-Distillation to Self-Practice: Privileged Information for Multi-Turn Agents
published: 2026-09-24T05:32:25Z
authors: Xingyu Su, Abhishek Kumar, Qing Ping, Youzhi Luo, Jonathan Buck, Zach Zhang, Subramanian Chidambaram, Vinayak Arannil
url: http://arxiv.org/abs/2609.29051v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Self-Distillation to Self-Practice: Privileged Information for Multi-Turn Agents

## Abstract
On-policy self-distillation (OPSD) has become a popular recipe for post-training LLM agents. It supervises the agent model at the token level with a stronger teacher view of the same model, obtained by conditioning on privileged information (PI). In this work, we show that in multi-turn agents, this paradigm teaches the student to act with confidence but without the information behind it. The trained agent behaves as if it had privileged information it never observed, and its performance falls well short of plain RL, in the worst case below the untrained base model. Therefore, we propose Privileged Self-Practice (PSP), which keeps the PI and moves it from the loss to the sampler. When the student's rollouts on a task mostly fail, we inject a short per-task instruction written by an analyzer model, sample the task again with the instruction in context, and train on the result with an unchanged GRPO objective. The privileged information stays in the prompt and never enters the loss. Across AppWorld and SWE-bench Verified, with three different student models, PSP obtains the best average score in every setting and is the only method that consistently outperforms plain GRPO, improving task-goal completion by up to 65% on AppWorld and the resolved rate by up to 61% on SWE-bench Verified.

## Metadata
- **Published**: 2026-09-24T05:32:25Z
- **Authors**: Xingyu Su, Abhishek Kumar, Qing Ping, Youzhi Luo, Jonathan Buck, Zach Zhang, Subramanian Chidambaram, Vinayak Arannil
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29051v1)