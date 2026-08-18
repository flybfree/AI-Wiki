---
title: Ask to Be Sure: Informative Interactions for Confident Multi-Turn LLM Recommendation
published: 2026-08-16T22:14:12Z
authors: Cedar Site Bai, Duanshun Li, Zhenyu Liao, Sheikh Sarwar, Huiyuan Chen, Yuan Chen, Changhe Yuan, Haiyang Zhang, Qilin Qi
url: http://arxiv.org/abs/2608.15949v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Ask to Be Sure: Informative Interactions for Confident Multi-Turn LLM Recommendation

## Abstract
Recent advances in large language models (LLMs) have enabled their use as conversational recommender systems (CRS), demonstrating strong recommendation accuracy and natural dialogue. However, guiding multi-turn interactions to elicit user preferences effectively remains challenging. Existing approaches either use separate reinforcement learning agents with templated interactions or optimize for interactivity judged by another LLM, without measuring how much useful information is actually gained. We propose a new approach that quantifies the effectiveness of each interaction by the reduction in the assistant's uncertainty, measured via entropy over recommendations. We apply this entropy reduction as a reward---without relying on ground-truth recommendations, which are often unavailable in real-world scenarios---to fine-tune the LLM, enabling strategic interaction generation. Empirical results with supervised fine-tuning (SFT) and direct preference optimization (DPO) on the INSPIRED and ReDial datasets show that our method improves both recommendation quality and conversational efficiency.

## Metadata
- **Published**: 2026-08-16T22:14:12Z
- **Authors**: Cedar Site Bai, Duanshun Li, Zhenyu Liao, Sheikh Sarwar, Huiyuan Chen, Yuan Chen, Changhe Yuan, Haiyang Zhang, Qilin Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15949v1)