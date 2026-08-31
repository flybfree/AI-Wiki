---
title: Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration
published: 2026-08-28T12:26:03Z
authors: Xiaoqing Wang, Keman Huang, Bin Liang, Hongyu Li, Xiaoyong Du, Wuqiong Pan
url: http://arxiv.org/abs/2608.28264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration

## Abstract
Multi-agent systems (MAS) powered by large language models have shown promise for complex tasks but suffer from high failure rates. Current self-reflection methods for MAS require all agents to reflect upon failure, overlooking a critical reality: failures typically stem from a specific agent leading the task astray, namely the decisive error agent, while others merely fulfill their regular duties. Forcing regular-behaving agents to reflect contaminates their memory with wrong insights. Hence, we propose DoCtOR (Diagnose-then-Correct PPO-enhanced Reflection), a novel reflection framework that enhances multi-agent collaboration. DoCtOR first identifies the decisive error step and decisive error agent through automated failure attribution, then employs counterfactual reasoning to generate a corrected decisive error step, and finally engages only the decisive error agent to produce targeted reflections. Experimental results show DoCtOR achieves 22%, 26%, and 27% improvements over initial success rates on HotPotQA, ChartQAPro, and Mind2Web datasets, outperforming Reflexion, Retroformer, and COPPER. We further establish the generalizability of our diagnose-then-correct paradigm and demonstrate that in low-resource settings, focusing reflection on reasoning steps after the decisive error step achieves comparable quality to reflecting on the complete failure trajectory.

## Metadata
- **Published**: 2026-08-28T12:26:03Z
- **Authors**: Xiaoqing Wang, Keman Huang, Bin Liang, Hongyu Li, Xiaoyong Du, Wuqiong Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28264v1)