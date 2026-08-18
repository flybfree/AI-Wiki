---
title: Dear Algo: A Precision-First Agentic Intent Layer for Unified Search and Recommendation
published: 2026-08-16T17:59:12Z
authors: Rui Wang, Jiazhou Wang, Zheng Wei, Chenglin Lu, Fangcheng Sun, Ivy Sun, Jin Sun, Hui Geng, Lillian Zhang, Chao Yang, Lei Chen, Shahin Sefati, Reem Helou, Joe Zhou, Babak Shakibi, Yiyi Pan, Bi Xue, Hong Yan, Shujian Bu
url: http://arxiv.org/abs/2608.15877v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dear Algo: A Precision-First Agentic Intent Layer for Unified Search and Recommendation

## Abstract
Search and recommendation serve a shared discovery objective but encode intent differently. We study this boundary through Dear Algo on Threads, a deployed product where open-ended requests such as \emph{more NBA news} or \emph{less politics} steer subsequent feed recommendations rather than return a one-shot result list. Its agentic intent layer compiles explicit, inferred, negative, and compound intent into a grounded executable plan, then invokes conventional retrieval and optional semantic or multimodal reranking. The layer shares an intent-to-retrieval contract without requiring one model or serving path across search-like and recommendation-like modes.   We evaluate Dear Algo under a precision-first objective. In a blinded audit of 300 public request-item pairs (296 evaluable), a strict categorical LLM-as-a-judge gate achieved 94.4\% exact-Relevant precision [88.8\%, 98.9\%]. Across 72 normalized request clusters, the full configuration produced 7.73 judge-qualified candidates per 20 slots versus 6.61 for an LLM-derived-query baseline, a gain of 1.11 [0.12, 2.12]. In a candidate-randomized serving-path study restricted to the reranker path's first 72 eligible hours, the user-weighted judge-Irrelevant share among judged admissions was 2.80\% versus 4.78\% off (-1.97 points [-3.02, -0.94]), while Exact-Relevant share was 2.24 points higher [0.08, 4.41].   Together, these studies show how explicit natural-language intent can be carried into feed recommendation under a precision-first evaluation framework

## Metadata
- **Published**: 2026-08-16T17:59:12Z
- **Authors**: Rui Wang, Jiazhou Wang, Zheng Wei, Chenglin Lu, Fangcheng Sun, Ivy Sun, Jin Sun, Hui Geng, Lillian Zhang, Chao Yang, Lei Chen, Shahin Sefati, Reem Helou, Joe Zhou, Babak Shakibi, Yiyi Pan, Bi Xue, Hong Yan, Shujian Bu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15877v1)