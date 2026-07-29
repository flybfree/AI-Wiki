---
title: Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering
published: 2026-07-27T21:30:39Z
authors: Rushi Qiang, Changhao Li, Haotian Sun, Yuchen Zhuang, Chao Zhang, Bo Dai
url: http://arxiv.org/abs/2607.25090v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering

## Abstract
Machine learning engineering (MLE) tasks require long-horizon decision making over iterative solution debugging and refinement, under expensive and feedback-driven environment interactions. Developing and training a monolithic agent for such tasks is fundamentally challenging, as it must simultaneously manage extremely long and noisy contexts, explore vast solution spaces, and remain effective under limited model capacity and computational budgets. To address these challenges, we propose Matryoshka Agent, a unified hierarchical agent framework for complex long-horizon tasks. Matryoshka Agent decomposes agentic problem solving into a coordinated hierarchy of decision making and execution: a high-level Orchestrator maintains compact, long-horizon exploration states and issues strategic instructions, while lower-level Sub-Agents execute concrete solution attempts through direct environment interaction, mediated by standardized Tool interface. This design decouples strategic exploration from costly execution, substantially reducing the burden of long-context reasoning and enabling efficient iterative refinement. We further develop an efficient training paradigm for Matryoshka Agent. Experimental results on a broad range of MLE tasks with diverse model types and scales demonstrate that Matryoshka Agent is an effective and scalable paradigm for long-horizon MLE tasks and complex agentic problem solving. Notably, Matryoshka Agent enables Qwen3-4B-Instruct to reach Orchestrator performance comparable to o4-mini. Applying Matryoshka Agent to Qwen3-30B-Coder results in at most 36.7% relative performance gain.

## Metadata
- **Published**: 2026-07-27T21:30:39Z
- **Authors**: Rushi Qiang, Changhao Li, Haotian Sun, Yuchen Zhuang, Chao Zhang, Bo Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25090v1)