---
title: Receiver-Conditioned Latent Communication gives 94% CacheBack
published: 2026-09-25T22:20:08Z
authors: Maximillian Rossi, Prajwal Raghunath, Haoqing Xuan, Yusen Zhang, Eugene Wu
url: http://arxiv.org/abs/2609.32046v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Receiver-Conditioned Latent Communication gives 94% CacheBack

## Abstract
Multi-agent systems distribute large contexts across agents that communicate to solve a task. Text messages are compact but require decoding and may omit evidence the receiving agent needs. Recent latent communication instead transfers KV caches. This avoids text generation and can improve accuracy and latency. However, a full KV cache grows linearly with both the context an individual agent processes, and the number of agents that coordinate together. This raises memory and context costs, often far exceeding available GPU resources and context window sizes. Our key observation is that agents need only send what the receiving agent requires for its local task -- which we call receiver-conditioned communication. The receiver agent passes the sender a small description of its information needs, which serves to filter and compress the sender agent's KV cache. CacheBack is a simple, robust, training-free instance of receiver conditioning based on the sender's attention weights. On FanOutQA, CacheBack with Qwen 3 removes 75% of the state the agent would otherwise receive, improving accuracy by 14.7 percentage points and reducing median task-completion latency by 3.2x relative to text communication. We show comparable improvements across model families that span dense Transformers, Mamba-attention hybrids, and sliding-window attention.

## Metadata
- **Published**: 2026-09-25T22:20:08Z
- **Authors**: Maximillian Rossi, Prajwal Raghunath, Haoqing Xuan, Yusen Zhang, Eugene Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32046v1)