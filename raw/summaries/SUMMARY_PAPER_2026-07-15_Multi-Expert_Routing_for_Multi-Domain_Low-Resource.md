---
title: Multi-Expert Routing for Multi-Domain Low-Resource OCR: A Manchu Case Study
url: http://arxiv.org/abs/2607.14041v1
type: paper-summary
date: 2026-07-15
source_paper: 2026-07-15_17-12-37Z_Multi_ExpertRoutingforMulti_DomainLow_ResourceOCR_.md
generated_at: 2026-07-15 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a multi‑expert routing system for historical Manchu OCR that reuses checkpoints from an iterative fine‑tuning process as domain specialists and employs a lightweight page‑level classifier to dispatch pages by visual style. On three frozen test sets the router matches each specialist with two‑decimal precision, achieving 0.30 % CER on regular script, 1.57 % on memorials, and 4.83 % on running script, while reaching 99.3 % page‑level domain accuracy.

## Key Takeaways
- The router matches the selected specialist for each writing style at two‑decimal precision, delivering CER rates of 0.30 %, 1.57 %, and 4.83 % on regular script, memorials, and running script respectively.
- Two of the three specialists were not trained specifically for their final domain; only the running‑script expert was targeted with that domain during training.
- The system achieves 99.3 % page‑level domain accuracy, matching a domain‑label oracle at the same precision.

## Context
The work addresses the challenge of low‑resource OCR where labeled data is scarce and visual styles vary widely across historical scripts. By leveraging existing fine‑tuned checkpoints as specialized experts, it demonstrates how knowledge reuse can mitigate data scarcity in multilingual or multimodal tasks.

## Implications
This approach offers a scalable template for deploying domain‑specific models without extensive new training, which could be applied to other low‑resource linguistic or visual domains. Practitioners may adopt similar routing mechanisms to improve accuracy and efficiency across heterogeneous datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14041v1)
