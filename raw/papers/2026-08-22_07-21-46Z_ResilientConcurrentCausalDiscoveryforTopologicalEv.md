---
title: Resilient Concurrent Causal Discovery for Topological Event Sequences
published: 2026-08-22T07:21:46Z
authors: Jiyu Tian, Junhao Dong, Mingchu Li, Lingling Fang, Liming Chen, Andreas Holzinger, Zheng Yan, Yew Soon Ong
url: http://arxiv.org/abs/2608.21815v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Resilient Concurrent Causal Discovery for Topological Event Sequences

## Abstract
Causal discovery on topological event sequences is crucial for ensuring the reliability of networks. However, existing methods struggle to capture the complex causal relationships arising from concurrent events and lack robustness to incomplete event sequences. To address these issues, we propose a resilient concurrent causal discovery method, termed RCCD, enabling robust learning of causal graphs from topological event sequences. Specifically, we first introduce an influence-aware hyperedge causal attention mechanism, which incorporates event duration into the embedding representation, aggregates concurrent event features via hyperedge causal convolution, and injects network prior knowledge to capture the complex many-to-one causal interactions. Furthermore, we design a masked-based alternating causal optimization framework, which forces the model to recover masked event types based on context through self-supervised mask reconstruction, thereby enhancing the resilience of the predictor to missing data. To validate the effectiveness of our method, we conduct extensive experiments on both simulated and real-world telecommunication network datasets. Experimental results demonstrate that the proposed method significantly outperforms existing state-of-the-art methods in both accuracy and robustness, making it more suitable for real-world telecommunication network environments.

## Metadata
- **Published**: 2026-08-22T07:21:46Z
- **Authors**: Jiyu Tian, Junhao Dong, Mingchu Li, Lingling Fang, Liming Chen, Andreas Holzinger, Zheng Yan, Yew Soon Ong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21815v1)