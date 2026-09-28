---
title: Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models
published: 2026-09-25T07:52:37Z
authors: Bing Wang, Changchun Li, Xin-Qiang Cai, Lin Yuanbo Wu, Ximing Li, Gang Niu, Masashi Sugiyama
url: http://arxiv.org/abs/2609.30935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models

## Abstract
Continual fine-tuning is essential for large language models (LLMs) to dynamically adapt to real-world environments, yet it inevitably suffers from catastrophic forgetting, particularly the performance degradation of previous tasks and LLMs' general-purpose knowledge. Although existing methods, such as orthogonal gradient projection, mitigate the forgetting across various fine-tuning tasks, they fundamentally fail to preserve pre-training LLMs' inherent general-purpose knowledge because the original data and gradients of off-the-shelf pre-training LLMs required by these methods are strictly unknown and highly diverse. To bridge this critical gap, we propose EoupCT, a novel framework designed to Estimate and Orthogonalize Unknown Pre-training gradients for Continual LLM fine-Tuning. Specifically, EoupCT estimates pre-training gradients by dynamically generating pseudo data that is most susceptible to forgetting for new tasks through a learnable soft prompt equipped with Gumbel-Softmax relaxation. Furthermore, we formulate a multi-objective optimization problem and introduce a first-order efficient Pareto optimizer that jointly optimizes LLM parameters and the soft prompt, rigorously enforcing orthogonality between new task updates and the estimated pre-training gradients. Extensive experiments across multiple LLMs demonstrate that EoupCT effectively preserves both task-specific proficiency and inherent general-purpose knowledge, successfully mitigating the catastrophic forgetting.

## Metadata
- **Published**: 2026-09-25T07:52:37Z
- **Authors**: Bing Wang, Changchun Li, Xin-Qiang Cai, Lin Yuanbo Wu, Ximing Li, Gang Niu, Masashi Sugiyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30935v1)