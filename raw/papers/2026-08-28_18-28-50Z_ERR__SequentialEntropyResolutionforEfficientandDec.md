---
title: ERR+: Sequential Entropy Resolution for Efficient and Decisive LLM Reasoning
published: 2026-08-28T18:28:50Z
authors: Xin Jiang, Minhao Wang, Wen Wu, Zhentao Xie, Shangheng Du, Jinxin Shi, Jiabao Zhao
url: http://arxiv.org/abs/2608.28771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ERR+: Sequential Entropy Resolution for Efficient and Decisive LLM Reasoning

## Abstract
Large reasoning models achieve strong performance on complex tasks by generating extended chain-of-thought (CoT) traces via reinforcement learning with verifiable rewards (RLVR). While current RLVR methods have achieved strong results with correctness-based reward signals, they provide limited guidance on the quality of the reasoning process itself, leaving the internal reasoning structure largely unoptimized. Through empirical analysis across multiple model families, we identify a consistent pattern: correct reasoning trac es exhibit more frequent and larger token-level entropy drops within the thinking phase than incorrect ones. We propose ERR+, a two-phase RLVR framework grounded in this observation. The first phase trains with the Entropy Relief Reward (ERR), a bonus proportional to cumulative token-level entropy drops in the thinking phase, log-normalized by response length. Unlike prior methods that suppress entropy, ERR rewards the resolution of uncertainty while leaving exploratory high-entropy states unconstrained. The second phase introduces the Robust Relative Efficiency Reward, which scores each response's length against co-generated peers via a $\tanh$-transformed within-group $z$-score. We provide a formal analysis showing that joint optimization of the two objectives induces gradient conflict in early training, motivating the sequential design . Experiments on five datasets demonstrate consistent improvements in both accuracy and response conciseness across model backbones. Our code is available at https://github.com/XrkArul/err_response

## Metadata
- **Published**: 2026-08-28T18:28:50Z
- **Authors**: Xin Jiang, Minhao Wang, Wen Wu, Zhentao Xie, Shangheng Du, Jinxin Shi, Jiabao Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28771v1)