---
title: MemAgent: Learning to Manage Heterogeneous Memory Providers for LLM Agents
published: 2026-09-26T12:04:31Z
authors: Yongxian Wei, Yilin Zhao, Runxi Cheng, Xinrui Chen, Chun Yuan, Yaoru Wang, Jiahong Yan, Dian Li
url: http://arxiv.org/abs/2609.32521v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemAgent: Learning to Manage Heterogeneous Memory Providers for LLM Agents

## Abstract
Current agents remain largely stateless across tasks, limiting their ability to continually improve from prior interactions and making memory essential for long-horizon agentic behavior. Existing memory methods seek to reuse past experience, but most rely on a single memory representation (e.g., trajectories, reflections, skills, structured knowledge) whose effectiveness varies across task distributions. Rethinking this design space, we evaluate 13 memory methods and find that no single method generalizes across benchmarks, revealing the potential of managing heterogeneous memory providers. We formulate agent memory as a routing problem in which a memory agent decides which memory provider to retrieve from, whether to inject short-term memory, and which providers should store the resulting experience. Based on this perspective, we propose MemAgent, featuring a content-aware routing architecture and a training-data synthesis pipeline. The routing architecture combines content-aware probing before retrieval, short-term memory gating during execution, and selective multi-provider storage, while the training pipeline synthesizes phase-specific supervision for routing decisions. Across GAIA, WebWalkerQA, and xBench-DS, MemAgent improves average accuracy by 10.0% and outperforms every individual memory method across all three benchmarks. These gains come with less than 0.3% routing overhead and a 12% reduction in average task steps.

## Metadata
- **Published**: 2026-09-26T12:04:31Z
- **Authors**: Yongxian Wei, Yilin Zhao, Runxi Cheng, Xinrui Chen, Chun Yuan, Yaoru Wang, Jiahong Yan, Dian Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32521v1)