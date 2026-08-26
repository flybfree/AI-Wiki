---
title: DeepRepoQA: Code Repository Question Answering with Deep Agent Exploration
published: 2026-08-25T08:26:31Z
authors: Weihan Peng, Yuling Shi, Yingwei Ma, Longfei Yun, Beijun Shen, Xiaodong Gu
url: http://arxiv.org/abs/2608.24221v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeepRepoQA: Code Repository Question Answering with Deep Agent Exploration

## Abstract
Answering developer questions about a software repository is a critical yet under-explored problem in software engineering. While existing repository understanding methods have advanced the field, they predominantly rely on surface-level code retrieval and lack the ability for deep reasoning over multiple files, complex software architectures, and grounding answers in long-range code dependencies. To address these limitations, we propose DeepRepoQA, a novel question answering (QA) framework for repository-level code understanding. DeepRepoQA builds on an agentic framework where LLM agents find answers through a systematic tree search over the repository structure. A Monte-Carlo Tree Search (MCTS) mechanism is employed to empower agents to dynamically search, navigate, and inspect code, enabling effective multi-hop reasoning over long-range code dependencies. Comprehensive experiments on the SWE-QA benchmark demonstrate substantial performance gains over strong baselines, validating the effectiveness of systematic MCTS-guided exploration for multi-hop repository reasoning.

## Metadata
- **Published**: 2026-08-25T08:26:31Z
- **Authors**: Weihan Peng, Yuling Shi, Yingwei Ma, Longfei Yun, Beijun Shen, Xiaodong Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24221v1)