---
title: Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks
published: 2026-09-03T06:44:04Z
authors: Xiangyu Wang, Jin Wu, Xiaoyu Li, Chanjin Zheng, Yifeng Zhou
url: http://arxiv.org/abs/2609.03432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks

## Abstract
Automated evaluation of creativity tasks remains challenging for LLM-as-a-Judge, as LLM is susceptible to biases such as verbosity bias and leniency bias. Such limitations are particularly evident in Contextually-Grounded and Procedurally-Structured Tasks (CGPST), a complex multi-step creativity task where inter-step dependencies, highly subjectivity, and wide scoring ranges lead to more unstable and biased judgments. Existing approaches either rely on task-specific training or directly apply LLM-as-a-Judge, both of which struggle to ensure reliable evaluation under such complexity. To bridge these gaps, we propose CreaEval, an automated creativity evaluator for CGPST that decouples typical LLM-as-a-Judge into analysis and judging. Correspondingly, CreaEval involves two critical phases: Memory-augmented Analysis, a SoT-LLM converts multi-step responses into structured evaluation evidence, incorporating cross-step memory; and Evidence-based Judging, a Judge-LLM uses the extracted evidence for judging without accessing raw responses. Comprehensive experiments show that CreaEval achieves an average performance improvement of 22.74% over the second-best baselines across CGPST and two classic simple creativity tasks, demonstrating its generalizability. The code is available at https://github.com/Jaong/CreaEval.

## Metadata
- **Published**: 2026-09-03T06:44:04Z
- **Authors**: Xiangyu Wang, Jin Wu, Xiaoyu Li, Chanjin Zheng, Yifeng Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03432v1)