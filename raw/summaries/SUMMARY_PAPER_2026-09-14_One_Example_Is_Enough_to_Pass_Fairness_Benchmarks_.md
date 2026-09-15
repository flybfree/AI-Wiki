---
title: One Example Is Enough to Pass Fairness Benchmarks: Rethinking Fairness Evaluation for Aligned LLMs
url: http://arxiv.org/abs/2609.14860v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-14_00-21-26Z_OneExampleIsEnoughtoPassFairnessBenchmarks_Rethink.md
generated_at: 2026-09-14 22:23
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper challenges the reliability of widely used fairness benchmarks like BBQ, arguing that they are overly simplistic and easily gamed. The authors demonstrate that aligning a base language model with just a single example using either Group Relative Policy Optimization or one-shot in-context learning dramatically boosts benchmark accuracy, effectively closing the performance gap typically achieved through large-scale reinforcement learning from human feedback. Ultimately, the study concludes that these multiple-choice abstention formats measure superficial structural cues rather than genuine fairness alignment.

## Key Takeaways
- Fine-tuning a base model with Group Relative Policy Optimization on just one BBQ example increases accuracy from 79.9% to 92.9%, while using the same example as an in-context learning demonstration pushes accuracy to 99.0%.
- Cross-conditioning analysis reveals that these performance gains are driven by the emergence of a category-agnostic "missing evidence" reasoning

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14860v1)
