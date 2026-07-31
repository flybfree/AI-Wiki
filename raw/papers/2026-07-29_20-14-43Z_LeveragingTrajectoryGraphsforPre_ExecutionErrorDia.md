---
title: Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems
published: 2026-07-29T20:14:43Z
authors: Xu Zheng, Zhuomin Chen, Chaohao Lin, Hua Wei, Haifeng Chen, Wei Cheng, Dongsheng Luo
url: http://arxiv.org/abs/2607.27443v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems

## Abstract
Large Language Model~(LLM)-based agents have demonstrated exceptional performance across a wide range of complex interactive tasks. However, they often struggle with long-horizon interactive tasks common in domains, such as embodied AI. The complexity and vast action spaces in these settings lead to compounding errors, where a single suboptimal action can derail an entire trajectory, causing the agent to exhaust its limited step budget on inefficient or unrecoverable paths. To overcome this without costly fine-tuning, we draw inspiration from software debugging, where execution logs are analyzed to preemptively catch errors. We propose \textit{Trajectory Graph Copilot}, a novel framework that acts as a ``copilot'' for LLM agents by diagnosing potential action errors before they are executed. At its core,\textit{Graph Debugger} models historical trajectories as a probabilistic graph and uses a Graph Neural Network to identify sequential action patterns that frequently lead to failure. Functioning as a proactive diagnostic sandbox, our method provides early warnings on potentially flawed actions, prompting the agent to self-correct. This pre-action error diagnosis prevents costly mistakes, significantly enhancing the agent's ability to complete long-horizon tasks successfully. The extensive experiments on four benchmarks with three LLM agents demonstrate a $14.69\%$ pass ratio improvement on average.

## Metadata
- **Published**: 2026-07-29T20:14:43Z
- **Authors**: Xu Zheng, Zhuomin Chen, Chaohao Lin, Hua Wei, Haifeng Chen, Wei Cheng, Dongsheng Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27443v1)