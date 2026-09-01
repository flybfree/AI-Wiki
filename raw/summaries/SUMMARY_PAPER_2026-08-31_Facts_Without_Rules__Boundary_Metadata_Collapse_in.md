---
title: Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs
url: http://arxiv.org/abs/2608.29028v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_03-38-35Z_FactsWithoutRules_BoundaryMetadataCollapseinMulti_.md
generated_at: 2026-08-31 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how multi‑agent large language model handoffs can unintentionally erase privacy‑protecting boundary metadata while preserving operational facts, a phenomenon termed summary collapse. Experiments on GPT‑5‑mini and DeepSeek‑R1‑32B show that compressed handoff summaries retain operational details but lose most boundary markers, leading to higher leakage in downstream tasks.

## Key Takeaways
- Boundary markers survive only about half as often when handoffs are limited to 25 words (σ_b≈0.57) compared with free‑text handoffs where survival is near 0.80, indicating that truncation destroys metadata.
- Operational facts remain largely intact even under compression, showing a decoupling between factual content and privacy boundaries at the handoff level.
- Leakage rates drop to under 15% when explicit constraints are used, whereas vague language causes leaks in 73% of GPT cases and 50% of DeepSeek cases.

## Context
The study highlights a growing concern that compressed representations in AI systems may sacrifice privacy safeguards without obvious loss of functionality. As multi‑agent workflows become standard, the hidden cost of metadata loss is an emerging risk for responsible deployment.

## Implications
For developers, designing handoff artifacts must prioritize explicit boundary language to prevent information leakage. Practitioners should adopt audience allowlists and precise redaction strategies rather than relying solely on summary compression or prompt tweaks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29028v1)
