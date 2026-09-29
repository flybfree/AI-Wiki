---
title: Streamlined Reflective Evolution for Task-Adaptive Self-Refinement Pipelines
published: 2026-09-26T10:45:36Z
authors: Xiaofan Zhou, Lu Cheng
url: http://arxiv.org/abs/2609.32458v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Streamlined Reflective Evolution for Task-Adaptive Self-Refinement Pipelines

## Abstract
Reflective prompt optimization improves large language model (LLM) systems without updating model weights, but fixed architectures constrain how self-refinement is organized. We introduce Workflow-Designing Agents (WDA), a framework for streamlined reflective evolution of task-adaptive self-refinement pipelines. Starting from a minimal prompt, WDA jointly evolves stage instructions and their sequential structure. During evolution, we find that repeated revisions can accumulate redundant instructions in a single prompt. In WDA, we propose to address this problem with SPLIT, which redistributes these instructions across specialized stages. Three-example reflection and local screening guide selective search, while calibration scores guide Pareto admission and rollback of unhelpful trailing updates. The resulting pipelines are task-adaptive: their instructions and depth are learned from task data, then fixed for all test inputs within that task. We evaluate WDA on five benchmarks spanning knowledge, mathematical reasoning, multi-hop question answering, and instruction following. On Qwen3.5-9B, WDA achieves an average score of 51.24%, improving over the initial solver by 8.63 percentage points and the variant without SPLIT by 2.60 points. On GPT-4.1-mini, it achieves 49.00%, with corresponding gains of 5.62 and 3.69 points. These results support task-adaptive self-refinement as a complementary direction to broader agentic workflow search.

## Metadata
- **Published**: 2026-09-26T10:45:36Z
- **Authors**: Xiaofan Zhou, Lu Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32458v1)