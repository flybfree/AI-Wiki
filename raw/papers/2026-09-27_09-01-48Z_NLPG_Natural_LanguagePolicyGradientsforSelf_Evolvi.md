---
title: NLPG: Natural-Language Policy Gradients for Self-Evolving Language Agents
published: 2026-09-27T09:01:48Z
authors: Xu Liu, WenZhang Wei, Jun Cao, Dehua Peng, Huan Chen, Zhipeng Gui, Huayi Wu
url: http://arxiv.org/abs/2609.33379v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NLPG: Natural-Language Policy Gradients for Self-Evolving Language Agents

## Abstract
Large language model agents increasingly rely on compound programs for retrieval, tool use, reasoning, and verification, yet their failures often arise from local procedural decisions. Existing reinforcement-learning and prompt-optimization approaches typically rely on scalar rewards or repeatedly modify entire prompts, making it difficult to capture and reuse procedural improvements while preserving a frozen agent. To address this problem, We propose Natural-Language Policy Gradients (NLPG), an external policy-memory method for improving a fixed agent without changing its model parameters or program structure. NLPG diagnoses execution traces, propagates downstream feedback backward through the module graph, and converts recurring failures into route-local natural-language corrections that are aggregated into bounded policy updates for subsequent executions. Across six benchmarks covering memory, reasoning, instruction following, and evidence verification, NLPG also outperforms the strongest listed baseline for each benchmark by 8.71 percentage points on average. These results provide evidence that evaluated procedural experience can be transformed into local and interpretable policy updates, enabling continual improvement of frozen agents.

## Metadata
- **Published**: 2026-09-27T09:01:48Z
- **Authors**: Xu Liu, WenZhang Wei, Jun Cao, Dehua Peng, Huan Chen, Zhipeng Gui, Huayi Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33379v1)