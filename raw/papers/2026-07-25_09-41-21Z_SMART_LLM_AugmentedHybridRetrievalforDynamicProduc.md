---
title: SMART: LLM-Augmented Hybrid Retrieval for Dynamic Product Ads
published: 2026-07-25T09:41:21Z
authors: Congfei Zhang, Jingxiao Ma, Xiaodong Liu, Hsiang-wei Chao, Siman Wang, Ge Liu, Shantanu Aggarwal, Vincent Zhang, Meghana Missula, Rachel Liao, Zichu Li, Xiao Bai, Yunzhi Zhou, Yajun Wang, Zhe Liu, Jinchao Li, Yu Zhang
url: http://arxiv.org/abs/2607.23121v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SMART: LLM-Augmented Hybrid Retrieval for Dynamic Product Ads

## Abstract
Dynamic Product Ads (DPA) require retrieving relevant items from multi-million product catalogs, balancing two competing objectives: retargeting (re-surfacing known interests) and prospecting (discovering new categories). While Large Language Models (LLMs) capture semantic intent better than traditional embedding models, deploying them at scale introduces prohibitive inference costs and lexical mismatch issues. Through controlled experiments on millions of users, we demonstrate a critical retrieval decomposition: rule-generated queries excel at retargeting on a lexical BM25 index, while LLM-generated queries excel at prospecting on a dense ANN index. Building on this, we propose SMART (SeMantic-aware Adaptive ReTrieval). To manage costs, a lightweight quality gate identifies coverage gaps in initial keyword results, adaptively routing only the ~10% of users who benefit from semantic prospecting to the LLM path. Offline evaluation demonstrates that this gated approach captures the bulk of semantic prospecting gains in Relevance Score while maintaining competitive re-targeting performance at a 90% reduction in LLM costs. Finally, in a 2-week online A/B test at Snap, SMART improved the ad conversion rate by +27.6% over a strong embedding-based baseline.

## Metadata
- **Published**: 2026-07-25T09:41:21Z
- **Authors**: Congfei Zhang, Jingxiao Ma, Xiaodong Liu, Hsiang-wei Chao, Siman Wang, Ge Liu, Shantanu Aggarwal, Vincent Zhang, Meghana Missula, Rachel Liao, Zichu Li, Xiao Bai, Yunzhi Zhou, Yajun Wang, Zhe Liu, Jinchao Li, Yu Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23121v1)