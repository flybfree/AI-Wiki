---
title: RALI@iKAT 2026: Retrieval-aware User Profile Denoising via Personalized Conversational Dense Retrieval
published: 2026-10-13T03:59:13Z
authors: Yuchen Hui, Fengran Mo, Jia Ao Sun, Yuxing Tian, Wenhao Xu, Jian-Yun Nie
url: http://arxiv.org/abs/2610.17673v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RALI@iKAT 2026: Retrieval-aware User Profile Denoising via Personalized Conversational Dense Retrieval

## Abstract
Modern conversational information access systems continuously extract user information from conversations to build user profiles for personalized retrieval. As user profiles accumulate over time, they inevitably become noisy, making effective user profile denoising a fundamental challenge. Existing personalized conversational query reformulation methods rely on the black-box reasoning capability of LLMs to expand the original query with relevant user profile phrases, producing a verbose query for retrieval. Such rewrite-then-retrieve pipelines reduce user profile denoising to the explicit selection of profile phrases in the sparse token space, separating personalization from downstream relevance modeling. Consequently, they often fail to identify user information that is truly beneficial for retrieval.   To enable retrieval-aware user profile denoising, we propose Personalized Conversational Dense Retrieval (PCDR), which learns to jointly project the conversation history and user profile into a latent embedding space dedicated to retrieval. By inheriting the context denoising capability from conversational dense retrievers, PCDR requires only a handful of personalized relevance annotations for training. We evaluate PCDR on the iKAT 2026 tasks, where it serves as the core retrieval component of a conversational AI agent assisting users with complex information needs.

## Metadata
- **Published**: 2026-10-13T03:59:13Z
- **Authors**: Yuchen Hui, Fengran Mo, Jia Ao Sun, Yuxing Tian, Wenhao Xu, Jian-Yun Nie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17673v1)