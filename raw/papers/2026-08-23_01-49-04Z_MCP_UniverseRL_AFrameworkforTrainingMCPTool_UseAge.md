---
title: MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning
published: 2026-08-23T01:49:04Z
authors: Ziyang Luo, Yan Yang, Xiangru Jian, Ziji Shi, Xiaoqiang Lin, Jun Hao Liew, Silvio Savarese, Junnan Li
url: http://arxiv.org/abs/2608.22167v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning

## Abstract
Reinforcement learning (RL) has become an effective way to improve the tool-use ability of large language models (LLMs), but most existing RL frameworks stop at the policy update. For every new domain, the user is left with two hard systems problems: standing up an isolated environment for each of hundreds of concurrent trajectories and connecting it to training, and scheduling the rollout so that the GPU stays busy across long, multi-turn episodes that spend much of their time stalled on slow tool calls. We present MCP-Universe RL (MCP-U RL), an open-source framework that takes over both. It uses the Model Context Protocol (MCP) as the interface to the environment, so any tool already exposed as an MCP server plugs into training with no RL-specific integration code. It builds the two missing layers once and reuses them across domains: an environment-orchestration layer that provisions, isolates, and recycles the MCP environments over a pluggable container backend, and a rollout-orchestration layer whose staged pipeline overlaps trajectories to keep the GPU busy while episodes wait on tools. A backend-agnostic training layer then applies the update through an existing RL backend, with veRL and slime integrations. With one configuration, changing only the task specification, we train software-engineering, deep-research, and general tool-use agents on gpt-oss-20b and improve task reward in all three.

## Metadata
- **Published**: 2026-08-23T01:49:04Z
- **Authors**: Ziyang Luo, Yan Yang, Xiangru Jian, Ziji Shi, Xiaoqiang Lin, Jun Hao Liew, Silvio Savarese, Junnan Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22167v1)