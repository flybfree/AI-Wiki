---
title: VRL-Bench: Benchmarking agents on computer control tasks under finite trial budgets
published: 2026-09-11T03:54:02Z
authors: Yu Bai, Yukai Miao, Dawei Wang, Li Chen, Yanyu Ren, Yuqian Shi, Dan Li, Ying Xiong, Chengqiu Tan, Run Zhou, Li Li
url: http://arxiv.org/abs/2609.12404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VRL-Bench: Benchmarking agents on computer control tasks under finite trial budgets

## Abstract
Learning from trial and error is a promising way to improve language agents on complex tasks such as computer control. Reflexion introduced verbal reinforcement learning, which turns failed trials into text that guides later attempts without updating model parameters. We introduce VRL-Bench, a harness for fair evaluation of trial-and-error learning under finite trial budgets. Across three models on MiniWoB and WebShop, we evaluate updates from several prominent verbal-memory methods spanning Reflexion and later work: each improves observed success over memory-free retry in some settings but reduces it in others. Replay experiments show that using reflection can reduce success rates, revealing a trade-off between exploiting experience and continued exploration. We propose VEX$^2$, a verbal exploration--exploitation scheduler that uses a language model to jointly select policies and allocate the remaining trial budget. VEX$^2$ is the only evaluated update to achieve positive observed success-rate gains over retry in all six settings.

## Metadata
- **Published**: 2026-09-11T03:54:02Z
- **Authors**: Yu Bai, Yukai Miao, Dawei Wang, Li Chen, Yanyu Ren, Yuqian Shi, Dan Li, Ying Xiong, Chengqiu Tan, Run Zhou, Li Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12404v1)