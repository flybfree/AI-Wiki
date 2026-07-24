---
title: Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning
published: 2026-07-20T19:58:32Z
authors: Jia Ao Sun, Hao Yu, Fengran Mo, Zhan Su, Yuchen Hui, Bang Liu, Jian-Yun Nie
url: http://arxiv.org/abs/2607.18481v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning

## Abstract
Knowledge graph question answering (KGQA) requires navigating from topic entities to an answer several relations away. Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy. We present Search-on-Graph-R1 (\sogrone{}), which internalizes this navigation into a compact 8B model through supervised fine-tuning (SFT) followed by reinforcement learning (RL). Our central idea is to scaffold a frontier teacher with each question's gold SPARQL query, so the teacher traverses a known answer-bearing path with a live \texttt{Search} tool rather than having to discover the path itself. Since every call executes against a live Freebase server, the resulting trajectories are grounded in the knowledge graph by construction. On WebQSP, CWQ, and GrailQA, \sogrone{} at 8B surpasses every frozen frontier-LLM system in our comparison and posts the strongest results on CWQ of any system we compare against. It does so using no auxiliary module at inference and no LLM judge during training. Isolating each training stage shows that SFT and RL contribute complementary gains, our approach transfers across model families, and RL learns to reach answers in fewer \texttt{Search} calls than its SFT initialization.

## Metadata
- **Published**: 2026-07-20T19:58:32Z
- **Authors**: Jia Ao Sun, Hao Yu, Fengran Mo, Zhan Su, Yuchen Hui, Bang Liu, Jian-Yun Nie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18481v1)