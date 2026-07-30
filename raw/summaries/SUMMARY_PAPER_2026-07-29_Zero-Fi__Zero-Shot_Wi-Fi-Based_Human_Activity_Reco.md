---
title: Zero-Fi: Zero-Shot Wi-Fi-Based Human Activity Recognition via Contrastive Signal-Language Alignment
url: http://arxiv.org/abs/2607.26381v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_01-34-02Z_Zero_Fi_Zero_ShotWi_Fi_BasedHumanActivityRecogniti.md
generated_at: 2026-07-29 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Zero-Fi, a zero-shot Wi‑Fi based human activity recognition system that aligns raw signal features with natural language descriptions using contrastive learning. The framework enables recognition of unseen activities without labeled Wi‑Fi samples or model adaptation. Experiments show effective performance on public benchmarks for held‑out classes.

## Key Takeaways
- Zero-Fi learns unified representations from complementary Wi‑Fi signal features and aligns them with semantic activity labels in a shared embedding space.
- The contrastive alignment allows zero‑shot recognition of new activities without requiring labeled data or retraining the model.
- Experiments on large public datasets demonstrate successful performance for held‑out activity classes.

## Context
Human activity recognition using Wi‑Fi signals is limited by the need for extensive labeled samples and predefined class sets. This work addresses those constraints by leveraging natural language to extend sensing capabilities beyond existing models, aligning with broader trends in cross‑modal representation learning.

## Implications
Zero‑shot methods reduce development time and data collection costs, making large‑scale activity monitoring more feasible. Practitioners can deploy systems that recognize diverse activities from a single Wi‑Fi network without custom training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26381v1)
