---
title: Scaling Scientific Discovery Environments for Turn-Level Agentic RL
published: 2026-07-31T03:34:39Z
authors: Yucheng Xu, Keyi Zhang, Yuyang Yu, Min Zhang, Shiyuan Meng, Pei Chu, Zhongying Tu
url: http://arxiv.org/abs/2607.28990v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Scientific Discovery Environments for Turn-Level Agentic RL

## Abstract
Large language model agents have shown promising capabilities in data-driven scientific discovery tasks, where an agent interacts with an execution environment and produces a statistical claim. Long-horizon scientific analysis remains constrained by the lack of process supervised environments over real-world scientific data. This paper introduces SciDisco, a scalable framework for training Scientific Discovery agents in process-verifiable environments. SciThèque compiles hypotheses, datasets, hidden evidence graphs, and verifiers into task environments where analytical progress can be checked during interaction. DAG-grounded trajectory synthesis uses these environments to construct verifier-filtered multi-turn demonstrations. DiscoPO then uses the environment as the source of training signal, assigning turn-level credit to actions that produce verifiable analytical evidence. Experiments show that SciDisco-14B reaches state-of-the-art on hypothesis-driven scientific data analysis benchmarks.

## Metadata
- **Published**: 2026-07-31T03:34:39Z
- **Authors**: Yucheng Xu, Keyi Zhang, Yuyang Yu, Min Zhang, Shiyuan Meng, Pei Chu, Zhongying Tu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28990v1)