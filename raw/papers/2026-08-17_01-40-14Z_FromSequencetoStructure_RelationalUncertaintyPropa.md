---
title: From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents
published: 2026-08-17T01:40:14Z
authors: Zhengzhao Ma. Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun
url: http://arxiv.org/abs/2608.16002v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents

## Abstract
Reliable uncertainty quantification (UQ) is essential for deploying large language model (LLM) agents in complex interactive environments. Existing UQ methods largely rely on local signals, such as token probabilities, predictive entropy, or per-step confidence, and therefore overlook the long-range dependencies through which errors accumulate across an execution trajectory. As a result, they may fail to identify agent failures whose causes originate several reasoning or interaction steps before the final answer. We propose RUPA (Relational Uncertainty Propagation for Agents), a trajectory-level UQ framework for LLM agents. RUPA represents an execution history as a directed trajectory graph in which reasoning states, tool interactions, and environment feedback are nodes connected by temporal and semantic dependency edges. It then propagates uncertainty over this graph to capture how execution risk accumulates and transfers across interaction steps. The propagated signal is combined with trajectory-level behavioral features and goal-alignment information to produce a confidence estimate for the full agent trajectory. We evaluate RUPA on representative agent benchmarks, including $τ$-2, Terminal-Bench-2, and GAIA, using 6 open-source LLMs spanning multiple model families. Experimental results show that RUPA consistently outperforms existing UQ methods by providing more accurate uncertainty estimates, enabling earlier failure detection, and improving uncertainty-guided agent execution across diverse agent tasks. These results demonstrate that explicitly modeling relational dependency is crucial to reliable UQ for long-horizon LLM agents, providing a practical foundation for trustworthy agent execution.

## Metadata
- **Published**: 2026-08-17T01:40:14Z
- **Authors**: Zhengzhao Ma. Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16002v1)