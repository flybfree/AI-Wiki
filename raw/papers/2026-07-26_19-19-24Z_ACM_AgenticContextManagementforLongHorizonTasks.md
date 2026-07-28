---
title: ACM: Agentic Context Management for Long Horizon Tasks
published: 2026-07-26T19:19:24Z
authors: Xiaochuan Li, Ryan Ming, Meng Chu, Shuai Shao, Rong Jin, Chenyan Xiong
url: http://arxiv.org/abs/2607.23809v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ACM: Agentic Context Management for Long Horizon Tasks

## Abstract
Agentic tasks are inherently long-horizon and multi-turn, constantly accumulating context through interactions with the environment. Existing context compression methods inevitably incur information loss and are triggered by rigid heuristic rules, leaving them misaligned with the agent's evolving reasoning focus. We propose Agentic Context Management (ACM), a framework that equips agents with purpose-built context editing tools for lossless context management. Inspired by the interaction between short-term and long-term human memory, the agent autonomously decides when to compress its context, offloads discarded content to an external memory system, and queries it on demand for later retrieval. Building on this framework, we further develop a post-training pipeline that constructs high-quality demonstrations of context management and improves model performance on both agentic search and coding tasks. Further analysis reveals that effective context management reduces peak token pressure, enables extended explorations, and yields more consistent solutions across independent trials. Code, data, and model checkpoints are available at https://github.com/lixiaochuan2020/agentic-context-management.

## Metadata
- **Published**: 2026-07-26T19:19:24Z
- **Authors**: Xiaochuan Li, Ryan Ming, Meng Chu, Shuai Shao, Rong Jin, Chenyan Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23809v1)