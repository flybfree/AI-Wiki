---
title: VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement
published: 2026-10-19T13:10:54Z
authors: Ruotian Peng, Yuanyi Ren, Shuaiqi Liu, Xin Guo, Fang Zhu, Yangyi Huang, Yue Wu, Zheng Wang, Yandong Wen, Zhihang Fu
url: http://arxiv.org/abs/2610.26342v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement

## Abstract
Recursive self-improvement (RSI) requires agents to diagnose system bottlenecks and coordinate improvements across training and inference. We refer to the agents' capability to jointly optimize training data, the trainer, and the inference harness as cross-component co-design. We introduce VibeTraining-Bench, a benchmark for evaluating this capability across tasks spanning terminal operation, software engineering, multi-turn tool use, and mathematical reasoning. Within each task, research agents start from an identical initial agent system under a fixed resource budget. Guided by validation feedback, they iteratively refine data, trainers, and inference harnesses, then select and submit a final agent system for evaluation on the test set. To prevent reward hacking, we enforce three safeguards: test data isolation, separate research and grading containers, and network restrictions for research agents. Our evaluation results show that frontier research agents substantially improve target agent systems. For example, on SWE-bench Verified, GPT-6-Astra raises the target agent system's performance from 32.9% to 53.7%, comparable to the human-developed instruct model's 55.4%. However, there is still room to improve their ability to co-design and iteratively refine data, trainer, and harness to achieve cumulative performance gains. We hope that VibeTraining-Bench will serve as a unified platform for advancing RSI, deepening our understanding of cross-component optimization for agent systems. Code and data are available at https://github.com/D2I-ai/VibeTrainingBench.

## Metadata
- **Published**: 2026-10-19T13:10:54Z
- **Authors**: Ruotian Peng, Yuanyi Ren, Shuaiqi Liu, Xin Guo, Fang Zhu, Yangyi Huang, Yue Wu, Zheng Wang, Yandong Wen, Zhihang Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26342v1)