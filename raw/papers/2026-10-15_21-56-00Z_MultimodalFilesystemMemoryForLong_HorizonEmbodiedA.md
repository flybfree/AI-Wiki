---
title: Multimodal Filesystem Memory For Long-Horizon Embodied Agents
published: 2026-10-15T21:56:00Z
authors: Chloe Su, Jiahan Li, Zhenting Qi, Chaoran Cheng, Haoyu Chen, Sejoon Jun, Weirui Ye, Yilun Du
url: http://arxiv.org/abs/2610.22686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multimodal Filesystem Memory For Long-Horizon Embodied Agents

## Abstract
Agents operating over long horizons need an effective memory that allows them to reuse their experience throughout long interactions. If the entire history of an interaction is retained, it becomes difficult to find the relevant experience, while compressing it into summaries may result in the loss of visual and spatial details that are required later on. We present \textbf{MFM}, a multimodal filesystem memory architecture that keeps complementary types of agent memory. \textbf{Episodic memory} stores the observations, actions, and outcomes, and \textbf{spatial memory} associates experiences with locations. \textbf{Semantic and procedural memory} build up general knowledge and reusable methods of acting, and \textbf{working memory} holds the current plans. MFM makes use of searchable textual records to connect these different representations to the underlying multimodal episodes. The agents are able to find previous experiences by means of contextual cues and to examine the original observations in order to recover details that are missing from their textual descriptions. Through consolidation, the agents convert experience into higher-level knowledge and procedures while still keeping references to the original episodes. In the case of long-horizon Minecraft and computer-use tasks, MFM leads to improved performance with three base models. With GPT-6-Astra, MFM completes \emph{Mine Diamond from Scratch} and reaches 16 out of 24 milestones on the \emph{Ender Dragon} task, as against 12.7 for the best baseline. On CUABench-KiCad it attains a mean reward of 0.440, as compared to 0.400 for the best baseline and 0.267 in the case of no persistent memory.

## Metadata
- **Published**: 2026-10-15T21:56:00Z
- **Authors**: Chloe Su, Jiahan Li, Zhenting Qi, Chaoran Cheng, Haoyu Chen, Sejoon Jun, Weirui Ye, Yilun Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22686v1)