---
title: Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning
published: 2026-07-22T18:06:15Z
authors: Jian Hu, Huiying Li, Hao Zhang, Binfeng Xu, Yifan Zhang, Shaokun Zhang, Hemil Desai, Michael Demoret, Pavlo Molchanov, Jan Kautz, Yi Dong
url: http://arxiv.org/abs/2607.21653v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning

## Abstract
Agentic reinforcement learning research is constant algorithm modification, new estimators, new pipeline stages, new rollout schemes, and in mainstream frameworks each change threads through layers of trainer, distributed backend, and rollout glue: the cost lands on the researcher at every iteration. Molt is a PyTorch-native training framework built to keep that cost small: a codebase compact and clean enough for a researcher to hold in their head, and for an AI coding assistant to read and reason about in its entirety, so the algorithm flow can be traced and changed end to end. The agent is an ordinary program, and one asynchronous loop trains multimodal and mixture-of-experts policies while never training on a token it did not generate, consistent in tokens, policy versions, and model semantics. Leanness does not cost performance: under a matched, fully asynchronous protocol, Molt is statistically comparable to a state-of-the-art Megatron-based stack. Molt is open source and provides recipes and containers at https://github.com/NVIDIA-NeMo/labs-molt.

## Metadata
- **Published**: 2026-07-22T18:06:15Z
- **Authors**: Jian Hu, Huiying Li, Hao Zhang, Binfeng Xu, Yifan Zhang, Shaokun Zhang, Hemil Desai, Michael Demoret, Pavlo Molchanov, Jan Kautz, Yi Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21653v1)