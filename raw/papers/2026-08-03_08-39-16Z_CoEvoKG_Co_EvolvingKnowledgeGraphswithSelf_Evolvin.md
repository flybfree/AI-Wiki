---
title: CoEvoKG: Co-Evolving Knowledge Graphs with Self-Evolving Search Agents
published: 2026-08-03T08:39:16Z
authors: Zhaoyang Li, Zenghuang Fu, Qiuyuan Ai, Ping Jiang, Haoyu Wu, Minghui Wu, Chenxu Zhao, Jie Song, Guannan He
url: http://arxiv.org/abs/2608.01904v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoEvoKG: Co-Evolving Knowledge Graphs with Self-Evolving Search Agents

## Abstract
Large language models can improve with reinforcement learning for search agents, yet existing self play agents repeatedly generate tasks while discarding the knowledge gained during successful searches. We introduce CoEvoKG, a framework that turns a   knowledge graph into both a source of verifiable training tasks and a persistent evidence memory for agent evolution. CoEvoKG jointly trains a task generator and a search agent: the generator creates multihop questions from entity chains sampled   from the knowledge graph, while the agent learns from rewards for answer correctness and search trajectories whose entity paths are supported by graph evidence. When a search succeeds, CoEvoKG verifies and deduplicates the retrieved evidence, then   writes it back to the corresponding graph nodes and edges. Future rounds reuse this enriched graph for task generation and reward computation, closing the loop between model self evolution and knowledge accumulation. Experiments on six QA benchmarks   (NQ, TriviaQA, PopQA, HotpotQA, 2WikiMultiHopQA, and Bamboogle) with three backbone models show that CoEvoKG improves macro average accuracy over the corresponding base models by +11.2, +10.1, and +11.6 points on Qwen2.5-3B-Instruct,   Qwen2.5-7B-Instruct, and Llama-3.1-8B-Instruct, respectively. Under matched training budgets, CoEvoKG further improves over competitive self play baselines and RL baselines for search agents by +2.6 to +3.7 macro average points across the three   backbones. Code is available at https://github.com/lazzy1225/CoEvoKG.

## Metadata
- **Published**: 2026-08-03T08:39:16Z
- **Authors**: Zhaoyang Li, Zenghuang Fu, Qiuyuan Ai, Ping Jiang, Haoyu Wu, Minghui Wu, Chenxu Zhao, Jie Song, Guannan He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01904v1)