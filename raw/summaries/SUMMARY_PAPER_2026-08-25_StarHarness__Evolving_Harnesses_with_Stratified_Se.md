---
title: StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments
url: http://arxiv.org/abs/2608.24804v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_16-48-05Z_StarHarness_EvolvingHarnesseswithStratifiedSearchf.md
generated_at: 2026-08-25 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces StarHarness, a framework that evolves environment-specific agent harnesses while keeping model weights fixed. It improves full-benchmark performance by 20-35 percentage points after a few accepted changes per environment. Gains persist on tasks excluded from evolution and transfer across GPT and Qwen models.

## Key Takeaways
- StarHarness constructs a compact evolution pool by stratifying tasks according to baseline failure behavior, separating proposer-visible search tasks from proposer-hidden selection tasks.
- The framework reserves held-out tasks for evaluating generalization, allowing assessment of improvements without re-evolution.
- Trace analysis shows that interface repairs and operational knowledge compress search, reducing false-positive diagnoses and shortening trajectories.

## Context
Enterprise AI agents often struggle with tool-rich environments where model outputs are misaligned with operational conventions. Traditional harnesses require fine-tuning or manual adjustments for each domain, limiting scalability. This work addresses the persistent mismatch by automating harness evolution through stratified search.

## Implications
Practitioners can deploy more reliable AI tools without retraining models, saving time and resources. The approach demonstrates that small, targeted changes to harness configuration can yield large performance gains across diverse enterprise settings. This encourages a shift toward adaptive, environment-aware AI pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24804v1)
