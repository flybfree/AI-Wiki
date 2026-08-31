---
title: Ladders in Chaos: When, How, (and Perhaps Why) Does Test-Time Scaling Improve LLM Machine Translation
published: 2026-08-28T16:22:39Z
authors: Di Wu, Sergey Troshin, Christof Monz, Antske Fokkens, Vlad Niculae
url: http://arxiv.org/abs/2608.28496v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Ladders in Chaos: When, How, (and Perhaps Why) Does Test-Time Scaling Improve LLM Machine Translation

## Abstract
Two forms of test-time scaling for Large Language Models (LLMs) have emerged as effective and widely adopted paradigms: sequential, in which later answer attempts depend on earlier ones, and parallel, such as i.i.d. sampling with reranking. In this study, we investigate their properties in translation. First, our study shows that sequential sampling has a higher performance ceiling, providing a more diverse and effective pool of samples, particularly under smaller sampling budgets. Second, we interrogate the nature of test-time scaling through a multidimensional manual analysis. Human analysis of the Best-of-$N$ translations demonstrates that sequential sampling substantially improves translation fluency and naturalness, but can degrade accuracy when inference budgets are large. Finally, we suggest an explanation of the mechanism through which sequential scaling improves machine translation. Our controlled analysis partially attributes the success of sequential self-improvement to the model's access to a larger target-side context. Ablation experiments on sequential sampling demonstrate its robustness across different sampling temperatures, while also revealing sensitivity to context construction, suggesting directions for future improvement.

## Metadata
- **Published**: 2026-08-28T16:22:39Z
- **Authors**: Di Wu, Sergey Troshin, Christof Monz, Antske Fokkens, Vlad Niculae
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28496v1)