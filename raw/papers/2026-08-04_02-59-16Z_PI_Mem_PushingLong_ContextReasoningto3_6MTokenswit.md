---
title: PI-Mem: Pushing Long-Context Reasoning to 3.6M Tokens with Parallel-Iterative Memory
published: 2026-08-04T02:59:16Z
authors: Dawei Liu, Haixu Song, Shuang Cheng, Shijie Wang, Haozheng Hou, Kaifeng Liu, Ermo Hua, Zhonghang Yuan, Zhijie Zhong, Yuchen Fan, Biqing Qi, Bowen Zhou
url: http://arxiv.org/abs/2608.03048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PI-Mem: Pushing Long-Context Reasoning to 3.6M Tokens with Parallel-Iterative Memory

## Abstract
Long-context reasoning remains a critical bottleneck for large language models, as recent recurrent-memory approaches face two inherent challenges: sequential chunk-wise updates can overwrite early critical evidence with later irrelevant content, and serial inter-chunk dependencies limit parallelism and cause latency to increase with context length. To address these issues, we propose PI-Mem (Parallel-Iterative Memory), a mechanism that processes all chunks in parallel and iteratively refines a shared memory over a bounded number of turns. In each turn, PI-Mem reads all chunks in parallel conditioned on the current memory, selects new or complementary evidence from each chunk, and merges the selected evidence into a compact shared memory for the next turn. To discourage redundant turns, we optimize the workflow through reinforcement learning with an auxiliary turn-efficiency reward, enabling the model to adaptively exit once sufficient evidence has been accumulated. We evaluate PI-Mem with Qwen3.5-35B-A3B and Qwen2.5-7B on the HotpotQA benchmark across context lengths up to 3.6 million tokens and find that it outperforms the recurrent-memory baseline by +6.25 and +7.81 absolute points while achieving 6.1$\times$ and 2.1$\times$ inference speedups, respectively. These results demonstrate that PI-Mem breaks the accuracy--efficiency trade-off in long-context reasoning and provides a scalable approach to complex multi-hop question answering over extremely long documents.

## Metadata
- **Published**: 2026-08-04T02:59:16Z
- **Authors**: Dawei Liu, Haixu Song, Shuang Cheng, Shijie Wang, Haozheng Hou, Kaifeng Liu, Ermo Hua, Zhonghang Yuan, Zhijie Zhong, Yuchen Fan, Biqing Qi, Bowen Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03048v1)