---
title: REVEAL: Reverse Engineering Agentic Latents from Frontier-Model Traces
published: 2026-10-12T07:14:47Z
authors: Yuetian Du, Meng Wang, Yucheng Wang, Zhangzhe Chen, Wei Wang, Boyu Yang, Weiqi Zhai, Bing Zhao, Ming Kong, Zhan Zhou, Jie Liu, Qiang Zhu
url: http://arxiv.org/abs/2610.16288v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REVEAL: Reverse Engineering Agentic Latents from Frontier-Model Traces

## Abstract
Frontier LLM agents perform complex interactive tasks, but their inference costs motivate transferring their experience to smaller open-source agents. Distillation and latent communication typically require target-model training or access to source-model internals. We study how textual frontier-model trajectories can provide reusable local controls for a frozen agent. Inspired by protocol reverse engineering, we introduce $\textit{Agentic Latents}$, comprising anchored states and dynamic profiles of feedback--response cycles elicited by replay in the target model. Our training-free framework, $\textbf{REVEAL}$ ($\textbf{REV}$erse $\textbf{E}$ngineering $\textbf{A}$gentic $\textbf{L}$atents), uses these profiles and trajectory outcomes to match and select local events from successful and failed rollouts of the same task and source model. Their response-transition contrasts yield a target-specific steering direction, applied before each response. Within-benchmark evaluations on Terminal-Bench 2.1 and Humanity's Last Exam with tools report higher accuracy than unmodified agents across three targets. Representation analyses and behavioral case studies support reusing frontier-model experience as local activation control.

## Metadata
- **Published**: 2026-10-12T07:14:47Z
- **Authors**: Yuetian Du, Meng Wang, Yucheng Wang, Zhangzhe Chen, Wei Wang, Boyu Yang, Weiqi Zhai, Bing Zhao, Ming Kong, Zhan Zhou, Jie Liu, Qiang Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16288v1)