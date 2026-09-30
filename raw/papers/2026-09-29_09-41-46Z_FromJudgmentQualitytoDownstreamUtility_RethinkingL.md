---
title: From Judgment Quality to Downstream Utility: Rethinking LLM-as-a-Judge for Open-Ended Tasks
published: 2026-09-29T09:41:46Z
authors: Zheng Zhang, Lufei Li, Xinyue Tan, Yuanhao Zeng, Ziwei Shan, Yexin Li, Kan Ren
url: http://arxiv.org/abs/2609.37145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Judgment Quality to Downstream Utility: Rethinking LLM-as-a-Judge for Open-Ended Tasks

## Abstract
LLM-as-a-Judge is increasingly used to evaluate policy responses on open-ended tasks that lack ground-truth answers. Existing work often directly converts the resulting judgments into reward signals for policy training, paying limited attention to intrinsic judgment quality and largely restricting the use of Judges to training-time supervision. We systematically investigate judgment quality and downstream utility by examining both how judgments are elicited and how they are used. For judgment elicitation, we vary the Judge protocol along three dimensions: verdict granularity, critique usage, and evaluation batching. For judgment usage, beyond policy training, we extend Judge to test-time inference through Best-of-N selection, Judge-guided revision, and beam search. We find that, (i) Surprisingly, judgment quality and downstream utility do not always align. (ii) Judge protocol design substantially affects both intrinsic judgment quality and downstream utility. (iii) Judge guidance effectively converts test-time compute into performance gains, with benefits varying across inference strategies. Our results call for a multifaceted evaluation of LLM Judges on open-ended tasks, encompassing intrinsic judgment quality, and downstream utility.

## Metadata
- **Published**: 2026-09-29T09:41:46Z
- **Authors**: Zheng Zhang, Lufei Li, Xinyue Tan, Yuanhao Zeng, Ziwei Shan, Yexin Li, Kan Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37145v1)