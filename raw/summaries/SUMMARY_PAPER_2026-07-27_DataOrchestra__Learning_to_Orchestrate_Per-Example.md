---
title: DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data
url: http://arxiv.org/abs/2607.24717v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_17-54-12Z_DataOrchestra_LearningtoOrchestratePer_ExampleCura.md
generated_at: 2026-07-27 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
DataOrchestra introduces a framework that orchestrates per-example curation of pretraining data by deciding whether to drop, untouch, or clean each chunk. The system selects downstream operations such as editing or LLM rewriting and generates concrete instructions for execution. Experiments show stable average gains across 11 benchmarks when training models from 0.5B to 7B.

## Key Takeaways
- DataOrchestra dynamically decides per example whether a data chunk is dropped, untouched, or cleaned, enabling fine‑grained processing decisions.
- The orchestrator selects one or more downstream operations and creates concrete instructions that are executed by tool models for rewriting steps.
- Training from scratch on processed web data yields stable average gains over individual methods across 11 benchmarks while reducing unnecessary compute.

## Context
Current pretraining pipelines apply uniform strategies to large corpora, limiting adaptability to example‑specific quality. This rigidity hampers performance and compute efficiency in scaling LLM training.

## Implications
The ability to tailor data processing per example could improve model robustness and reduce wasted resources, offering a scalable approach for diverse datasets. Practitioners may adopt DataOrchestra to fine‑tune pretraining pipelines without sacrificing speed or quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24717v1)
