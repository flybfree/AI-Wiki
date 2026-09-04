---
title: DE-Venus: A Data-Efficient RLVR Framework for Large Language Models
url: http://arxiv.org/abs/2609.03324v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_03-23-24Z_DE_Venus_AData_EfficientRLVRFrameworkforLargeLangu.md
generated_at: 2026-09-03 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DE‑Venus, a unified framework that makes reinforcement learning with verifiable rewards (RLVR) more data‑efficient for large language models. By treating supervision as an evolving state across three modules—active data selection, weak supervision construction, and training‑time supervision refinement—the authors achieve high model quality with only 10–13 % of the original labels or a small fraction of relevant data.

## Key Takeaways
- Active Data Selection allocates training and annotation budgets to maximize the impact of each label, allowing the framework to operate with far fewer annotations while preserving reward reliability.  
- Weak Supervision Construction extracts learning signals from unlabeled examples, enabling the system to generate useful targets without costly manual labeling.  
- Training‑Time Supervision Refinement filters or corrects unreliable supervision on the fly, ensuring that only trustworthy rewards are used during optimization.

## Context
Large language models increasingly rely on reinforcement learning for reasoning tasks, yet obtaining high‑quality verifiable rewards at scale remains a bottleneck due to expensive rollouts and noisy labels. Existing solutions often fragment supervision logic, making it difficult to compare or reuse methods across experiments.

## Implications
DE‑Venus reduces annotation and training costs dramatically, offering practitioners a scalable path to reliable RL for LLMs without sacrificing performance. This makes advanced reasoning capabilities more accessible in industry settings where data budgets are limited.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03324v1)
