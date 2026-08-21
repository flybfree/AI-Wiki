---
title: Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization
url: http://arxiv.org/abs/2608.20281v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_17-14-24Z_Inject_Align_Recover_StagedPost_TrainingforRetriev.md
generated_at: 2026-08-20 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces IAR, a three-stage post‑training framework that injects structured document knowledge into large language models, aligns the model’s QA behavior with answer‑only supervision, and recovers general capabilities by merging domain‑adapted and base instruction models. Across multiple datasets and model families, IAR achieves higher accuracy in both domain‑specific questions and overall performance compared to vanilla fine‑tuning. The framework’s modular design allows each stage to be applied independently, facilitating integration into existing fine‑tuning pipelines.

## Key Takeaways
- Inject converts source documents into continuation, rewrite, and instruction‑conditioned reconstruction objectives.
- Align adapts the injected model with answer‑only QA supervision.
- Recover merges the domain‑adapted model with the base instruction model to recover general capabilities.

## Context
In retrieval‑free document internalization, models must encode static corpora into their parameters without relying on external retrieval systems. This approach is crucial for applications where latency or access constraints limit real‑time lookup. The modular nature of IAR makes it adaptable to various fine‑tuning workflows and model architectures.

## Implications
The results suggest that post‑training fine‑tuning can be as effective as retrieval pipelines for knowledge grounding, offering a scalable alternative for enterprise and research settings. Practitioners may adopt IAR to embed domain expertise directly into models without costly data retrieval infrastructure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20281v1)
