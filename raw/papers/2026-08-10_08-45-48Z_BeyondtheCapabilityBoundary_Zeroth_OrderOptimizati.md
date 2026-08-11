---
title: Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents
published: 2026-08-10T08:45:48Z
authors: Bingzhen Liu, Xiaomeng Fan, Yuwei Wu, Zhi Gao, Mingyang Gao, Chuanhao Li, Yunde Jia
url: http://arxiv.org/abs/2608.09292v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents

## Abstract
Self-evolving methods improve the capabilities of LLM agents by sampling trajectories from the underlying LLMs and learning from these trajectories. However, these methods struggle to learn beyond the inherent capability boundary of the agents, since the agents cannot sample correct trajectories on difficult examples for further improvements. In this paper, we propose a zeroth-order self-evolution framework that enables agents to learn beyond their capability boundary by perturbing LLM parameters to adapt to difficult examples without any trajectory annotations. Specifically, we perturb LoRA parameters of LLMs, run the agent, compute the losses under the perturbed and original parameters, and use the loss difference to estimate gradients and further update the LoRA parameters. We sample trajectories using the updated LLMs for supervised fine-tuning to break through the capability boundary of the agents, forming a closed self-evolution loop. We introduce a parallel perturbation inference mechanism and an adaptive lookup mechanism to reduce time consumption in zeroth-order optimization, with an answer perplexity loss that provides smooth and stable zeroth-order loss values. Experiments on multiple deep research benchmarks show that our method obtains substantially more successful trajectories and consistently outperforms strong baselines, especially on difficult examples. The code and released artifacts are available at https://github.com/hidk1911/ZOForLLMAgents.

## Metadata
- **Published**: 2026-08-10T08:45:48Z
- **Authors**: Bingzhen Liu, Xiaomeng Fan, Yuwei Wu, Zhi Gao, Mingyang Gao, Chuanhao Li, Yunde Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09292v1)