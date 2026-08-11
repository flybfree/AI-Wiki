---
title: Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency in Interactive Narratives
published: 2026-08-08T14:38:18Z
authors: Yingpeng Ma, Jianhao Yan, Bei Shi, Ka Hou Kam, Runnan Wang, Xuebo Liu, Yulong Chen, Yue Zhang, Derek F. Wong
url: http://arxiv.org/abs/2608.08160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency in Interactive Narratives

## Abstract
The rapid advancement of Large Language Models (LLMs) is revolutionizing AI for Games by enabling open-ended and fluid interactive storytelling. However, existing research has largely overlooked the critical challenge of maintaining long-horizon logical consistency and narrative integrity against unconstrained user interventions. To address this, we formulate this challenge as Narrative Commitment Preservation (NCP), and take interactive narrative as our testbed. We introduce NCP-Bench, a benchmark of 100 narrative environments derived from movie synopses. Each environment includes a structured narrative specification (trajectory, commitments, and initial facts) that we can automatically check throughout the interaction between the player agent and the narrator agent. Experiments across state-of-the-art LLMs reveal a substantial long-horizon consistency gap: high linguistic quality does not guarantee commitment preservation; even strong models frequently generate logically conflicting content under adversarial interventions, with the best-performing model (GPT-5.2) achieving only 42% survival rate after 20 turns and fact conflict rates ranging from 40% to 68% across models, and only isolated runs satisfying all achievement commitments within the 100-turn limit.

## Metadata
- **Published**: 2026-08-08T14:38:18Z
- **Authors**: Yingpeng Ma, Jianhao Yan, Bei Shi, Ka Hou Kam, Runnan Wang, Xuebo Liu, Yulong Chen, Yue Zhang, Derek F. Wong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08160v1)