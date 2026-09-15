---
title: Salesforce Koa: An Enterprise Language Model for Agentic Tool Use
published: 2026-09-14T05:30:28Z
authors: Zixiang Chen, Sufeng Niu, Yingchi Liu, Wenting Zhao, Akshara Prabhakar, Shubham Mehrotra, Bin Bi, Zhujun Lan, Katherine Tan, Mohammad Ramezanali, Tulika Manoj Awalgaonkar, Monojit Banerjee, Jielin Qiu, Shiva Kumar Pentyala, Zhepeng Cen, Anupam Tripathi, Ali Ziaei, Regunathan Radhakrishnan, Darvish Lee Shadravan, Shelby Heinecke, Sitaram Asur, Silvio Savarese, James Zhu, Phil Mui, Huan Wang
url: http://arxiv.org/abs/2609.15066v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Salesforce Koa: An Enterprise Language Model for Agentic Tool Use

## Abstract
We present Salesforce Koa, an enterprise language model built by post-training the open-weight Nemotron-3-Super-120B foundation model with reinforcement learning using Group Relative Policy Optimization (GRPO). Salesforce Koa is trained on public and synthetically generated data, with no customer data, to improve tool use and agentic capabilities while preserving strong general-purpose performance. Its distinctive component is a simulation-to-reward pipeline that expands workflow specifications into persona-conditioned multi-turn tasks with task-resolution rewards grounded in successful tool use for data-dependent requests. For enterprise domains, these specifications are written in Agent Script, Salesforce's declarative language for building Agentforce agents; for public tool-use domains, we synthesize the workflow structure directly. The same simulation and grounded-reward machinery drives GRPO across both. Across public tool-use, agentic-reasoning, and enterprise Customer Relationship Management (CRM) benchmarks, Salesforce Koa improves over its open-weight base, with the clearest gains on multi-turn tool use, and surpasses a strong proprietary baseline while remaining below the strongest frontier models. These results show that specification-driven reinforcement learning is a practical path to specializing open-weight foundation models for enterprise agentic tasks.

## Metadata
- **Published**: 2026-09-14T05:30:28Z
- **Authors**: Zixiang Chen, Sufeng Niu, Yingchi Liu, Wenting Zhao, Akshara Prabhakar, Shubham Mehrotra, Bin Bi, Zhujun Lan, Katherine Tan, Mohammad Ramezanali, Tulika Manoj Awalgaonkar, Monojit Banerjee, Jielin Qiu, Shiva Kumar Pentyala, Zhepeng Cen, Anupam Tripathi, Ali Ziaei, Regunathan Radhakrishnan, Darvish Lee Shadravan, Shelby Heinecke, Sitaram Asur, Silvio Savarese, James Zhu, Phil Mui, Huan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15066v1)