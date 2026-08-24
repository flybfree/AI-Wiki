---
title: Benchmarking Patent Drafting from Inventor-Style Disclosures
url: http://arxiv.org/abs/2608.21249v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_16-00-52Z_BenchmarkingPatentDraftingfromInventor_StyleDisclo.md
generated_at: 2026-08-23 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Dis2Pat, a dataset that generates full patent applications from informal inventor disclosures, addressing the gap between early-stage ideas and legally coherent patents. It also proposes Patent-MAF, a multi-agent baseline for locally deployable drafting that outperforms open-source LLMs while remaining competitive with large closed‑source models.

## Key Takeaways
- The dataset Dis2Pat captures realistic patenting workflows by requiring complete applications from de‑legalized inventor disclosures, highlighting the difficulty of long‑form legal drafting. - Patent-MAF is a multi‑agent framework that enables local deployment and provides a strong baseline that consistently outperforms evaluated open‑source models. - Benchmark results show current LLMs struggle with patent drafting while Patent-MAF remains competitive against large closed‑source systems.

## Context
This work matters because it moves AI research toward practical, end‑to‑end patent generation from raw inventor input, which is a longstanding challenge in the field. It also demonstrates that multi‑agent architectures can improve performance without relying on proprietary APIs, aligning with privacy and deployment constraints.

## Implications
For patent practitioners, Patent-MAF offers a tool that can assist drafting while respecting legal constraints and user data. The findings suggest that AI systems must be evaluated not only on isolated tasks but on full workflow capabilities to meet real‑world needs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21249v1)
