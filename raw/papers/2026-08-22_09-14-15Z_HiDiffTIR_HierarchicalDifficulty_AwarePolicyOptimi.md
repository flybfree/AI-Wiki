---
title: HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning
published: 2026-08-22T09:14:15Z
authors: Yucan Guo, Xiaohan Wang, Miao Su, Saiping Guan, Zhongni Hou, Jiajun Chai, Wei Lin, Guojun Yin, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
url: http://arxiv.org/abs/2608.21863v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning

## Abstract
Tool-Integrated Reasoning (TIR) is a fundamental capability for LLM agents to solve complex tasks by interacting with external tools iteratively. Reinforcement Learning (RL) has become the dominant paradigm for enabling this capability. However, existing approaches typically assign uniform trajectory-level advantages and treat all correct tool calls equally, ignoring the varying difficulty and learning value across trajectories and reasoning steps. This can lead to imprecise learning signals that do not adequately distinguish between trivial and challenging tool-use patterns. To address this limitation, we propose HiDiffTIR, a Hierarchical Difficulty-aware policy optimization framework for multi-turn TIR. HiDiffTIR performs difficulty-aware credit assignment at both trajectory and turn levels, enabling the policy to focus on more informative trajectories and harder reasoning steps. Notably, this fine-grained optimization is achieved without additional supervision, relying solely on group-level statistics derived from standard RL rollouts. Extensive experiments on three tool-using benchmarks demonstrate that HiDiffTIR consistently improves multi-turn TIR performance and tool invocation accuracy over strong RL baselines, highlighting the necessity of difficulty-aware credit assignment for effective policy optimization in tool-integrated LLM agents.

## Metadata
- **Published**: 2026-08-22T09:14:15Z
- **Authors**: Yucan Guo, Xiaohan Wang, Miao Su, Saiping Guan, Zhongni Hou, Jiajun Chai, Wei Lin, Guojun Yin, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21863v1)