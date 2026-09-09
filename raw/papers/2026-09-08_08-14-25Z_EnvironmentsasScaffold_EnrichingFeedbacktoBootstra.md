---
title: Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks
published: 2026-09-08T08:14:25Z
authors: Hongbang Yuan, Zhuoran Jin, Yixin Cao
url: http://arxiv.org/abs/2609.08404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks

## Abstract
Large Language Models demonstrate remarkable proficiency in static reasoning, yet training them as autonomous agents through Reinforcement Learning (RL) for long-horizon tasks is often hindered by severe reward sparsity. While conventional \textit{agent-side warming} up via supervised fine-tuning (SFT) can alleviate this, it is frequently limited by data scarcity and constrained exploration. To address this, we propose a paradigm shift to \textit{environment-side adaptation} by constructing \textbf{F}eedback-\textbf{E}nriched \textbf{E}nvironments (\textbf{FEEs}). Through a pilot study, we establish a feedback design strategy that reformulates environments by transitioning from action guidance to observation enrichment during the later stages of both intra-episode exploration and inter-episode evolution. Large-scale experiments on SciWorld and BFCL benchmarks using various Qwen3 model scales and RL algorithms such as GRPO, GSPO, and DAPO demonstrate that FEEs consistently yield performance improvements over standard settings. Furthermore, our analysis reveals that training with FEEs \textbf{(1)} stabilizes training dynamics by reducing entropy volatility, \textbf{(2)} facilitates proactive state-space exploration in difficult tasks, \textbf{(3) }ensures the internalization of environmental guidance into policy weights rather than acting as a mere inference-time prior, and \textbf{(4) }identifies intra-group feedback consistency as a critical boundary for stable optimization.

## Metadata
- **Published**: 2026-09-08T08:14:25Z
- **Authors**: Hongbang Yuan, Zhuoran Jin, Yixin Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08404v1)