---
title: When Can LLM Reasoning Reliably Reuse Intermediate Results?
published: 2026-10-20T05:24:05Z
authors: Deyuan Liu, Zecheng Wang, Xuanyi Liu, Jungang Li, Yihao Hu, Mingjie Tang, Bryan Dai, Jie Fu
url: http://arxiv.org/abs/2610.27662v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Can LLM Reasoning Reliably Reuse Intermediate Results?

## Abstract
Sampling complete solutions gives large language models more chances to solve a problem, but each attempt starts again. For tasks with several subproblems, all required answers must be correct in the same attempt. Retaining intermediate results can avoid repeating correct work, but errors in those results may affect later attempts. We study when this reuse is reliable and how much computation it requires. For local retries that stop when no candidate passes within the retry budget, we give conditions for correct completion and bound the average number of attempts. We also show how checking cost and the chance of passing a check affect total computation. Experiments across eight reasoning models examine composite mathematics and arithmetic. Across four DeepSeek models, average success on the second subproblem is 36.2 percent without first-subproblem context, 57.2 percent with its answer, and 58.3 percent with its reasoning and answer. These scores measure second-subproblem coverage and include continuations made when selection fails. Arithmetic experiments show that similar first-attempt accuracies can lead to very different coverage after repeated attempts. Code is available at https://github.com/SempraETY/Intermediate-State-Reuse.

## Metadata
- **Published**: 2026-10-20T05:24:05Z
- **Authors**: Deyuan Liu, Zecheng Wang, Xuanyi Liu, Jungang Li, Yihao Hu, Mingjie Tang, Bryan Dai, Jie Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27662v1)