---
title: TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation
url: http://arxiv.org/abs/2608.02975v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_00-24-06Z_TQLite_Multi_LLMJuryGuidedDistillationforReal_time.md
generated_at: 2026-08-05 01:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TQLite, a distillation framework that lets small language models (SLMs) achieve MQM translation quality evaluation performance comparable to large reasoning model (LRM)-based evaluators. By leveraging a multi-LLM jury to generate synthetic training data and aggregating responses, TQLite enables scalable real-time evaluation with minimal compute cost.

## Key Takeaways
- SLMs can reach high MQM evaluation scores when trained via TQLite using synthetic data from a diverse panel of models.
- The framework reduces computational expense by replacing expensive LLM or LRM evaluators with lightweight SLMs, offering cost-effective deployment at scale.
- Multi-LLM jury aggregation improves training data quality, leading to robust performance across varied translation tasks.

## Context
Current TQ evaluation relies heavily on LLMs and LRMs which are resource-intensive for real-time applications. Small models remain limited by reasoning capabilities needed for nuanced judgments. This work addresses the gap between model efficiency and evaluation fidelity in a field where latency and cost are critical constraints.

## Implications
For industry practitioners, TQLite provides a practical pathway to embed high-quality translation quality assessment into low‑cost pipelines without sacrificing performance. Researchers gain insight into how synthetic data curation can bridge the capability divide between small and large models, informing future scalable AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02975v1)
