---
title: AgentBrew: Offline Tool-Use Agent Learning from Raw Real-World Trajectories
published: 2026-09-05T03:04:23Z
authors: Zhiyi Lyu, Yewen Li, Longtao Zheng, Shengtian Yang, Lang Feng, Lei Feng, Peng Jiang, Kun Gai, Qingpeng Cai, Bo An
url: http://arxiv.org/abs/2609.05837v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentBrew: Offline Tool-Use Agent Learning from Raw Real-World Trajectories

## Abstract
LLM-based agents are increasingly deployed in real-world applications through tool-use APIs, yet training them for specific environments remains fundamentally difficult: real-world applications provide no pre-defined tasks or verifiers, no faithful simulators, and limited budget for large-scale environment interaction. In this paper, we propose \textbf{AgentBrew}, an offline training framework that learns effective tool-use policies from a single batch of raw interaction trajectories, without task verifiers or iterative on-policy rollouts. The agent first explores the target environment to collect a raw trajectory corpus without quality filtering. To extract training signal from this noisy corpus, \emph{retrospective task inference} reconstructs an aligned instruction for each trajectory based on its actual outcome, and \emph{PMI-Based credit assignment} decomposes the trajectory's total information about the inferred instruction into additive per-action credits via pointwise mutual information (PMI). These credits weight the policy training objective, amplifying informative actions while suppressing ineffective ones. On three real-world MCP applications (GitHub, Notion, PostgreSQL), AgentBrew improves Qwen3-32B by +8.7 Acc / +9.7 Score on average, surpassing Qwen3-235B (+2.3 / +4.4) and outperforming rejection sampling (+5.9 / +10.3). These results demonstrate that fine-grained offline learning can recover useful supervision from raw trajectories that filtering-based approaches would discard. The code is available at https://github.com/alphatogo/AgentBrew

## Metadata
- **Published**: 2026-09-05T03:04:23Z
- **Authors**: Zhiyi Lyu, Yewen Li, Longtao Zheng, Shengtian Yang, Lang Feng, Lei Feng, Peng Jiang, Kun Gai, Qingpeng Cai, Bo An
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05837v1)