---
title: MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation
published: 2026-10-02T15:48:23Z
authors: Chenzhi Liu, Yue Zhang, Jiehong Lin, Jianan Wang, Bo Wang, Zhongrui Wang, Xiaojuan Qi
url: http://arxiv.org/abs/2610.03476v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation

## Abstract
Long-horizon mobile manipulation presents significant challenges due to compounding execution errors and capacity interference between locomotion and arm control. While recent Vision-Language-Action models excel at short-horizon tasks, they lack the hierarchical reasoning required for multi-stage objectives. Furthermore, existing hierarchical agents suffer from rigid sub-task mapping, inflexible replanning, and a lack of continuous learning. To address these limitations, we introduce MobiAgent, a dual-loop agentic framework that bridges robust deployment execution and recursive policy self-improvement. During deployment, the Inner Loop decouples high-level reasoning from low-level control through highly composable atomic skills. It employs Vision-Language models for receding-horizon planning and visual reflection, dynamically composing skills to ensure robust error recovery. These skills are executed by specialized flow-matching experts that share a unified VLM backbone, maximizing reusability while mitigating capacity interference. Concurrently, the Outer Loop drives automated lifelong learning by autonomously segmenting and verifying deployment rollouts, clustering them to discover atomic skills, and continuously fine-tuning the skill library without human annotations. Evaluations on RoboCasa, BEHAVIOR-1K, and real-world tasks demonstrate the effectiveness of MobiAgent. It outperforms $π_{0.5}$-TA by 22.5 percentage points on BEHAVIOR-1K and enables robust recovery from execution failures. Through autonomous data recycling, success improves from 7.50% to 27.50% on RoboCasa and from 32.5% to 57.5% on Astribot S1.

## Metadata
- **Published**: 2026-10-02T15:48:23Z
- **Authors**: Chenzhi Liu, Yue Zhang, Jiehong Lin, Jianan Wang, Bo Wang, Zhongrui Wang, Xiaojuan Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03476v1)