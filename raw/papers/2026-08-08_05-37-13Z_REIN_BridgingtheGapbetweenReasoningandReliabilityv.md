---
title: REIN: Bridging the Gap between Reasoning and Reliability via Reflection and Abstention Alignment
published: 2026-08-08T05:37:13Z
authors: Zhengze Huang, Luyang Yu, Di Hong, Xinzhe Huang, Wanyu Lin, Zhixuan Chu, Zhan Qin, Tianhang Zheng
url: http://arxiv.org/abs/2608.07931v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REIN: Bridging the Gap between Reasoning and Reliability via Reflection and Abstention Alignment

## Abstract
Large reasoning models (LRMs) are prone to hallucination, which undermines their reliability and poses challenges for safe deployment. Hallucinations in LRMs arise from two distinct failure sources: reasoning hallucination, where flawed inference steps propagate to an incorrect conclusion, and knowledge hallucination, where the model lacks the requisite factual knowledge to answer the query. To address reasoning hallucination, we propose REIN, an alignment framework that trains LRMs to produce a structured reasoning sequence, $\texttt{<think>} $$\rightarrow$ $\texttt{<reflection>} $$\rightarrow$ $\texttt{<answer>}$, enabling explicit self-reflection before committing to a final answer. To address knowledge hallucination, REIN introduces a reward mechanism that encourages explicit abstention (e.g., "I don't know") when none of the sampled reasoning chains yields a correct answer, allowing the model to refrain from unsupported predictions. Extensive evaluations on mathematical and commonsense reasoning benchmarks show that REIN consistently improves selective accuracy, reduces incorrect-but-self-endorsed responses, and maintains high coverage compared with competitive baselines. Notably, REIN achieves these gains within a single forward pass, without requiring process supervision, inference-time controllers, external search, or multi-round critiques. Experiments on multiple backbones show that REIN reduces the hallucination proxy by $58\sim72\%$ relative to the base models while maintaining $86\sim91\%$ average coverage, and improves selective accuracy on attempted questions by $6.6\sim14.2\%$.

## Metadata
- **Published**: 2026-08-08T05:37:13Z
- **Authors**: Zhengze Huang, Luyang Yu, Di Hong, Xinzhe Huang, Wanyu Lin, Zhixuan Chu, Zhan Qin, Tianhang Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07931v1)