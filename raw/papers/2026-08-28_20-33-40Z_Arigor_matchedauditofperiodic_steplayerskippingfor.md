---
title: A rigor-matched audit of periodic-step layer skipping for efficient llm inference: conflayers versus swift, with a supplemental analysis of trained routing alternatives
published: 2026-08-28T20:33:40Z
authors: Prateek Kumar Sikdar, Arpan Ghosh
url: http://arxiv.org/abs/2608.28846v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A rigor-matched audit of periodic-step layer skipping for efficient llm inference: conflayers versus swift, with a supplemental analysis of trained routing alternatives

## Abstract
Layer-skipping methods for efficient LLM inference decide, at some granularity, which transformer layers to execute for a given input. We present a rigor-matched, three-seed audit of two periodic-step, search-based methods that make this decision online at inference time and re-evaluate it every few generation steps: a confidence-gated early-exit baseline (ConfLayers) and genuine self-speculative decoding (SWIFT, Xia et al. 2024), together with vanilla autoregressive decoding, across two model scales (Qwen2.5-0.5B and Qwen2.5-1.5B) and two tasks (GSM8K reasoning and CNN/DailyMail summarization). SWIFT is the strongest method on accuracy in three of four cells; ConfLayers is dominated everywhere, with particularly large deficits on GSM8K at 1.5B. Once online-search overhead is separated from pure inference cost, SWIFT's true inference speed is faster than ConfLayers's in all four cells (5-21%), reversing the naive wall-clock ranking in three of them. ConfLayers's search overhead is small and stable (1-2% of cost), while SWIFT's is larger and more variable (up to 28.7%). We additionally examine two trained-routing methods, LayerRoute (Sikdar, 2026) and LayerDrop (Fan et al. 2020), as a supplemental analysis because they operate at coarser decision granularities. Under a verified protocol with genuine per-input gating, a genuine full-model baseline, and genuine inference-time compute skipping, both show modest speedups (1.08-1.33x) but accuracy well below the periodic-step methods, including a near-total collapse for LayerRoute on GSM8K at 1.5B (0.003 mean exact-match across three seeds). We release the full audit protocol as a template for rigor-matched efficiency comparisons.

## Metadata
- **Published**: 2026-08-28T20:33:40Z
- **Authors**: Prateek Kumar Sikdar, Arpan Ghosh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28846v1)