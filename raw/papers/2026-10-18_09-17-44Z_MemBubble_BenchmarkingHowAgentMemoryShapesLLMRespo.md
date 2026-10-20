---
title: MemBubble: Benchmarking How Agent Memory Shapes LLM Response Diversity
published: 2026-10-18T09:17:44Z
authors: Jiajun Tan, Fei Sun, Xinyu Ma, Shixuan Zhang, Du Su, Qi Cao, Daiting Shi, Huawei Shen, Xueqi Cheng
url: http://arxiv.org/abs/2610.25127v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemBubble: Benchmarking How Agent Memory Shapes LLM Response Diversity

## Abstract
Memory serves as the core component of LLM-based agents, enabling personalized responses via extracting and using user preferences from past interactions. However, its use may reduce response diversity, thereby narrowing the range of information available to users. Existing evaluations rely largely on synthetic interactions and cover few memory systems, leaving the effects of memory on response diversity insufficiently evaluated in real-world scenarios. We introduce MemBubble, a benchmark of 1000 instances built on preferences extracted from real user-assistant conversations. To measure the extent to which memory concentrates response distributions, we construct test queries in scenarios distinct from user preferences while preserving topical relevance through shared preference categories. Across multiple LLMs and memory mechanisms, entropy decreases by 34.7% on average compared with directly providing the full interaction history, highlighting the important role of memory processing in diversity loss. We also explore simple user-side interventions and changes in information availability but find that these do not effectively close the diversity gap. Our findings highlight the need to consider preserving diversity and user access to information alongside improvements in personalization when designing and using agent memory systems.

## Metadata
- **Published**: 2026-10-18T09:17:44Z
- **Authors**: Jiajun Tan, Fei Sun, Xinyu Ma, Shixuan Zhang, Du Su, Qi Cao, Daiting Shi, Huawei Shen, Xueqi Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25127v1)