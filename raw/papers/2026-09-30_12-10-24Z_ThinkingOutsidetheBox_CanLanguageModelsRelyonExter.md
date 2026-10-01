---
title: Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?
published: 2026-09-30T12:10:24Z
authors: Minghan Wang, Boyuan Wang, Jinhang Zuo, Yuxin Tao, Fang kong
url: http://arxiv.org/abs/2609.39578v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?

## Abstract
Agent harnesses often improve language models with human-designed workflows, but as models grow more capable, unreliable guidance can increasingly constrain their execution. We call the ability to benefit from useful guidance while overriding unreliable guidance thinking outside the box. We introduce Box$^2$-Bench, which holds the model and task fixed while varying workflow reliability to isolate how models regulate their reliance on guidance. On Box$^2$-Bench, frontier models often benefit from reliable guidance but remain vulnerable when it is misleading or becomes unreliable. To test whether this capability can be learned, we train two open-weight models using bad workflows, reserving good workflows for evaluation. We explore two complementary training strategies: counterfactual supervised fine-tuning improves robustness, while outcome-based reinforcement learning can shift the balance toward greater use of helpful workflows. We further find that this behavior extends beyond workflows to other forms of external information, improving peer correction and robustness to corrupted memory. Together, our results identify selective reliance on fallible external information as a dimension of agent reliability not captured by task performance alone.

## Metadata
- **Published**: 2026-09-30T12:10:24Z
- **Authors**: Minghan Wang, Boyuan Wang, Jinhang Zuo, Yuxin Tao, Fang kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39578v1)