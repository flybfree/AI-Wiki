---
title: EAT: Expert Account Tracker for Efficient MoE Inference
url: http://arxiv.org/abs/2609.33614v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_14-28-53Z_EAT_ExpertAccountTrackerforEfficientMoEInference.md
generated_at: 2026-09-28 23:32
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces EAT (Expert Account Tracker), a novel method designed to optimize Mixture-of-Experts inference by dynamically selecting the most relevant experts through history-awareness metrics and adaptive thresholding, thereby addressing the inefficiency caused by unnecessary expert activation. Experiments demonstrate that EAT outperforms existing baselines like Top-P across various models and datasets, achieving an average reduction of over 25% in activated experts compared to vanilla MoE while improving token generation speed. Additionally, the study highlights that pruned model performance can be efficiently recovered using only 9K data via OPD and reveals critical insights regarding layer-wise expert importance, noting that higher-level experts are generally more essential for maintaining accuracy.

## Key Takeaways
- EAT leverages history-awareness metrics combined with adaptive thresholding to

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33614v1)
