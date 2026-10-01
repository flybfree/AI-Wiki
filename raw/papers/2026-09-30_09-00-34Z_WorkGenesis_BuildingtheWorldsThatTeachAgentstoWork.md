---
title: WorkGenesis: Building the Worlds That Teach Agents to Work
published: 2026-09-30T09:00:34Z
authors: Xinyu Zhu, Fenyi Liu, Yuzhu Cai, Shuo Tang, Rui Ye, Linfeng Zhang, Siheng Chen
url: http://arxiv.org/abs/2609.39325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WorkGenesis: Building the Worlds That Teach Agents to Work

## Abstract
The ability of Large Language Model (LLM) agents to complete daily and professional work is receiving increasing attention. Training such agents requires realistic work scenarios. Expert-authored occupational work is costly and slow to produce, while unconstrained synthesis often yields tasks with weak factual grounding or internally inconsistent requirements. To bridge this gap, we introduce WorkGenesis, a framework that constructs executable occupational work from real-world artifacts through two core technical innovations: (1) Evidence-Based Work Construction, which grounds each unit of work in real-world evidence by retrieving public files guided by O*NET occupational knowledge and synthesizing the surrounding context, companion materials, work request, and itemwise rubric around them; and (2) Execution-Guided Consistency Verification, which renders a reference deliverable inside the constructed work, attributes every unsatisfied rubric item to the agent, the task, or the rubric, and uses task and rubric defects as feedback to iteratively repair the work until it passes the audit. Experimental results demonstrate that Fx-Work-35B, trained with simple supervised fine-tuning (SFT) on only 20K units of work synthesized by WorkGenesis, achieves the highest scores among all comparable-scale baselines on the five reported metrics across GDPvalAA-v2, APEX-Agents-AA, and JobBench (31.00 versus 24.79 average score), and even surpasses frontier models such as the 1.6T DeepSeek-V4-Pro-Preview. These results show that WorkGenesis provides scalable training data for working agents.

## Metadata
- **Published**: 2026-09-30T09:00:34Z
- **Authors**: Xinyu Zhu, Fenyi Liu, Yuzhu Cai, Shuo Tang, Rui Ye, Linfeng Zhang, Siheng Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39325v1)