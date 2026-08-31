---
title: Beyond Task-Only Matching: Personalized Skill Routing with Counterfactual Evaluation
published: 2026-08-28T11:55:56Z
authors: Tianle Wang, Yanghe Zou, Xiang Liu, Ziyao Huang, Chenchen Fu, Weiwei Wu
url: http://arxiv.org/abs/2608.28241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Task-Only Matching: Personalized Skill Routing with Counterfactual Evaluation

## Abstract
The rapid expansion of reusable skill repositories makes skill routing a critical capability for large language model (LLM) agents. Existing methods treat routing as task-only semantic matching. However, when users with incompatible constraints issue an identical request, this assumption conflates task relevance with skill suitability: a task-only router can select a semantically plausible skill that is unsuitable for the requesting user. To expose this failure mode, we formulate \textit{personalized skill routing} as profile-conditioned retrieval, in which relevance depends jointly on the task and the user profile. We first introduce a profile-counterfactual benchmark, in which the task is held fixed while changes in the user profile induce changes in the reference skill. We further construct paired counterfactual supervision and propose SkillFeed, a progressive retrieve-and-rerank framework that first establishes task--skill alignment and then learns profile-conditioned discrimination. By retrieving body-level evidence and reranking semantically similar but profile-conflicting candidates, SkillFeed identifies skills that satisfy both task requirements and user constraints. On SkillFeed-Bench, SkillFeed attains 75.1\% top-1 retrieval accuracy, a 23.1-point improvement over the corresponding pretrained routing baseline. Adding profile conditioning yields a 35.1-point gain on queries where user profile changes the reference skill. This contrast shows that user profiles are most consequential precisely when they change skill suitability. Our website is publicly available at http://www.aiskillfeed.com .

## Metadata
- **Published**: 2026-08-28T11:55:56Z
- **Authors**: Tianle Wang, Yanghe Zou, Xiang Liu, Ziyao Huang, Chenchen Fu, Weiwei Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28241v1)