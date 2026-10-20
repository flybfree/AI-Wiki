---
title: Ask Less, Ask Better: Allocating User Attention in Proactive LLM Agents with Interruption Budgets
published: 2026-10-17T03:23:49Z
authors: Xuanming Zhang, Amir H. Rezaeian, Miguel Ballesteros, Weiyi Sun, Werner Geyer, Lydia B. Chilton, Zhou Yu, Yassine Benajiba, Dan Roth
url: http://arxiv.org/abs/2610.24411v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Ask Less, Ask Better: Allocating User Attention in Proactive LLM Agents with Interruption Budgets

## Abstract
LLM agents can ask clarifying questions to complete tasks, but answering each question demands users' time and effort. Existing evaluations typically measure this burden by counting questions, treating necessary and avoidable questions equally. We propose an evaluation protocol that distinguishes how often agents ask from how well they ask. An interruption budget limits the number of questions, while a user-attention cost charges extra for questions that are hard to read or not worth asking, as rated by a human-validated LLM judge. Beyond question counts, this cost captures perceived effort: on conversation pairs with the same number of questions, human annotators agreed with the cost on which conversation required more effort 75% of the time. Across eight LLMs and four customer-service domains, limiting agents to one to three questions reduces user-attention cost by 36-73% while keeping 86-94% of the task reward they earn with unlimited questions. At the same budget, reviewing each question against the memory of users' earlier answers cuts attention cost by another 13% with little reward loss and yields more valuable questions. Models also differ sharply in how well they ask: at the same user-attention cost, the most efficient models gain more than twice as much reward from their questions as the others. These results show that asking less and asking better are distinct goals, and that evaluations of proactive agents should measure both.

## Metadata
- **Published**: 2026-10-17T03:23:49Z
- **Authors**: Xuanming Zhang, Amir H. Rezaeian, Miguel Ballesteros, Weiyi Sun, Werner Geyer, Lydia B. Chilton, Zhou Yu, Yassine Benajiba, Dan Roth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24411v1)