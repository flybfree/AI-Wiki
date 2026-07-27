---
title: Pixels for Programs? A Cross-Provider Case Study of Input-Token Accounting for Source Code as Text and Images
url: http://arxiv.org/abs/2607.21672v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-23_09-19-16Z_PixelsforPrograms_ACross_ProviderCaseStudyofInput_.md
generated_at: 2026-07-27 00:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how commercial APIs count input tokens when code is rendered as images versus kept as plain text, using a reproducible case study across five languages and varying source lengths. The results show that image representations reduce token usage by roughly 75‑87 % but the savings vary significantly between providers, with Gemini requiring far more tokens at short inputs.

## Key Takeaways
- Image-to-text ratios average 0.135, 0.194, and 0.242 across Anthropic, OpenAI, and Google Vertex AI, indicating substantial token reductions of 86.5 %, 80.6 %, and 75.8 % respectively.
- Gemini images demand about six times more tokens than text at the smallest code size (20 lines), while they only overtake text later in longer inputs.
- The non‑monotonic token count for Gemini across a page boundary reveals that provider accounting is not simply monotonic with input length.

## Context
The study highlights a growing trend of using vision‑language models to process code, which promises efficiency but raises questions about how downstream services measure usage. Understanding these counting differences is essential because billing and quota limits are often based on token counts rather than actual computational cost.

## Implications
For developers and product managers, the findings suggest that relying solely on image rendering may not always reduce API costs as expected, especially with Gemini. Practitioners should verify provider‑specific token accounting before adopting code‑as‑image pipelines to avoid unexpected usage spikes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21672v1)
