---
title: RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs
published: 2026-08-29T13:36:36Z
authors: Yuwei Lou, Hao Hu, Yuzhou Jiang, Zongfei Zhang, Liang Wang, Jincai Liu, Jidong Ge, Xianping Tao
url: http://arxiv.org/abs/2608.29263v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs

## Abstract
Large Language Models (LLMs) often suffer from hallucination and struggle with complex reasoning tasks requiring multi-hop domain knowledge. While integrating Knowledge Graphs (KGs) provides a structured and verifiable information source, current KG-enhanced LLM paradigms usually rely on single-agent path extraction and fixed prompting, lacking adaptability and facing huge search spaces. To address these challenges, we propose RACER, a Reinforced Agent Collaboration framework for Explainable Reasoning on knowledge graphs. RACER employs a semantic-aware action pruning and teacher-guided reinforcement learning mechanism to efficiently extract high-quality reasoning pathways from large-scale KGs. Furthermore, to mitigate single-path generation pitfalls, we introduce a cross-task accumulated shared memory graph paired with an attention-driven multi-path knowledge refinement module. Finally, RACER orchestrates these components through a four-role multi-agent collaboration system (GraphAgent, TemplateAgent, AnswerAgent, and CriticAgent) to dynamically refine prompts and evaluate answers. Extensive experiments on CommonsenseQA and OpenBookQA datasets demonstrate that RACER significantly outperforms state-of-the-art KG-enhanced LLM baselines with an average improvement of 5\%, offering robust and highly interpretable reasoning capabilities.

## Metadata
- **Published**: 2026-08-29T13:36:36Z
- **Authors**: Yuwei Lou, Hao Hu, Yuzhou Jiang, Zongfei Zhang, Liang Wang, Jincai Liu, Jidong Ge, Xianping Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29263v1)