---
title: Towards Communication-Efficient Social Intelligence in Language Agents
published: 2026-09-28T17:57:16Z
authors: Linxiao Gong, Yijie Xu, Tianfu Wang, Yin Wu, Yili Wang, Xingbo Yao, Huizai Yao, Xilin Xia, Haowen Yang, Hui Xiong
url: http://arxiv.org/abs/2609.35749v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Communication-Efficient Social Intelligence in Language Agents

## Abstract
Socially intelligent language agents must negotiate, coordinate, and resolve conflicting preferences while respecting the time and attention of both participants. Balancing these demands is challenging because agents must convey enough to address a partner's constraints and advance their goals without adding words that do not help the interaction. In this paper, we propose Teacher-Assisted Communication Training (TACT) to improve social goal attainment while reducing communication cost, making interactions with agents more productive and less demanding. We first characterize communication efficiency in terms of action strategy and expression, whose effects extend beyond the current utterance to the partner's response and subsequent exchanges. We design TACT to revise student-generated actions, test the revisions through partner responses, and distill useful feedback into the student. An expression specialist removes unnecessary detail while preserving the intended action, while a strategy specialist proposes alternatives that may better address the partner's constraints. To determine which revision helps, TACT samples a partner response for each candidate and selects a teacher reference by balancing local goal support against action-token cost. That reference guides on-policy distillation on the student's own generation prefixes, allowing the student to act independently at deployment. We evaluate TACT on SOTOPIA and AgentSense. On SOTOPIA, it achieves the highest Goal among the evaluated methods on All and Hard while using substantially fewer target tokens than SFT+SDPO. On AgentSense, it improves goal success over the initial student while reducing target tokens and interaction messages.

## Metadata
- **Published**: 2026-09-28T17:57:16Z
- **Authors**: Linxiao Gong, Yijie Xu, Tianfu Wang, Yin Wu, Yili Wang, Xingbo Yao, Huizai Yao, Xilin Xia, Haowen Yang, Hui Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35749v1)