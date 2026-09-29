---
title: Where Do Test-Time Scaling and Training Fall Short in Individual Stance Prediction?
published: 2026-09-27T03:27:05Z
authors: Yuyang Zhao, Xuan Liu, HaoYang Shangm Haojian Jin
url: http://arxiv.org/abs/2609.33155v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Do Test-Time Scaling and Training Fall Short in Individual Stance Prediction?

## Abstract
Test-time scaling and post-training have improved LLM performance in coding and mathematical reasoning, but their effectiveness for individual stance prediction remains unclear. We study this question by predicting a person's stance in a new discussion from their history. We evaluate widely used test-time scaling strategies and post-training methods, such as supervised fine-tuning and reinforcement learning, and identify four failure modes across generation, selection, and learning: (1) incorrect consensus, where repeated samples agree on the wrong stance; (2) selection failure, where generation covers the observed stance but selection misses it; (3) response overfitting, where supervised fine-tuning improves imitation but harms prediction; and (4) early plateau, where reinforcement learning shows modest initial gains followed by limited further improvement. We expose these failures using STANCE-BENCH, which contains 2499 prediction tasks from 500 Hacker News users. Guided by this analysis, we explore a simple approach that combines direct scores for all candidate stances with explicit assessments of support from the individual's history. On the 781-task test set, this approach achieves 21.83 discussion-specific Macro F1 with Qwen3-8B, compared with 19.27 for direct scoring. Our results motivate evaluating candidate generation, final selection, and person-specific evidence use separately.

## Metadata
- **Published**: 2026-09-27T03:27:05Z
- **Authors**: Yuyang Zhao, Xuan Liu, HaoYang Shangm Haojian Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33155v1)