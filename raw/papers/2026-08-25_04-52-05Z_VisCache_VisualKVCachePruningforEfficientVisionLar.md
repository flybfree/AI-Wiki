---
title: VisCache: Visual KV Cache Pruning for Efficient Vision Large Language Model Inference
published: 2026-08-25T04:52:05Z
authors: Lyuke Wang, Zhuo Li, Guangxu Zhu
url: http://arxiv.org/abs/2608.24063v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VisCache: Visual KV Cache Pruning for Efficient Vision Large Language Model Inference

## Abstract
While Vision Large Language Models (VLLMs) have achieved remarkable success in multimodal reasoning, their long-context inference remains prohibitively expensive due to the massive computation and memory overhead of visual Key-Value (KV) caches. Existing KV compression methods often apply uniform pruning across visual tokens and layers, leading to substantial information loss and degraded performance.To address this challenge, we propose \textbf{VisCache}, a plug-and-play framework for coarse-to-fine \textbf{Vis}ual KV \textbf{Cache} pruning without training, which consists of two synergistic stages. First, a lightweight VLM filters temporal redundancy by selectively forwarding semantically informative keyframes. Second, we introduce {PruneKV}, a surgical KV compression algorithm tailored to the attention dynamics of VLLMs. Unlike rigid pruning strategies, PruneKV adopts a parabolic layer-wise budget allocation together with an asymmetric update mechanism that selectively prunes keys while fusing values, thereby preserving critical contextual information. Extensive experiments demonstrate that VisCache substantially improves inference efficiency, achieving up to {2.35$\times$ speedup} and significant memory reduction while maintaining competitive performance with only {19--28\%} KV cache retention. VisCache consistently outperforms existing baselines, establishing a new Pareto frontier between efficiency and performance for long-context VLLM inference. Code is available at https://github.com/Wlklk/VisCache

## Metadata
- **Published**: 2026-08-25T04:52:05Z
- **Authors**: Lyuke Wang, Zhuo Li, Guangxu Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24063v1)