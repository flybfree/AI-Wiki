---
title: Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents
published: 2026-09-13T05:17:37Z
authors: Yuanyi Song, Yukai Wang, Xinbei Ma, Zhihui Fu, Jianghao Lin, Weiwen Liu, Jun Wang, Huarong Deng, Yong Yu, Weinan Zhang
url: http://arxiv.org/abs/2609.16053v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents

## Abstract
Long-term memory is essential for LLM-based agents operating over extended interactions. Existing memory systems primarily update memory when new information arrives, treating retrieval as the endpoint of memory access rather than a driver of memory evolution. Consequently, retrieval feedback is rarely exploited to reorganize memory for future access continuously. Moreover, most existing approaches rely on predefined memory structures together with fixed retrieval pipelines, limiting the agent's ability to organize and evolve its own memory autonomously. Inspired by memory reconsolidation in cognitive neuroscience, we propose \textbf{REALM}, a \textbf{r}econsolidation-\textbf{e}volution \textbf{a}gentic \textbf{l}ong-term \textbf{m}emory framework. It models long-term memory as a continual lifecycle by autonomously organizing memories into a heterogeneous cognitive graph, retrieving evidence via adaptively composed graph-search atoms, and continually reconsolidating memories based on retrieval feedback. REALM achieves an average accuracy of 75.97\% on LoCoMo and 65.11\% on LongMemEval, outperforming the strongest baselines by 7.17 and 1.31 points respectively. Ablation studies confirm that memory reconsolidation consistently boosts performance, with further analyses revealing that it progressively reorganizes related memory units into more coherent local structures for collective evidence recall and utilization during reasoning. These results suggest that retrieval-driven memory reconsolidation provides an effective mechanism for continually evolving long-term memory in LLM agents.

## Metadata
- **Published**: 2026-09-13T05:17:37Z
- **Authors**: Yuanyi Song, Yukai Wang, Xinbei Ma, Zhihui Fu, Jianghao Lin, Weiwen Liu, Jun Wang, Huarong Deng, Yong Yu, Weinan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16053v1)