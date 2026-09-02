---
title: Autoresearch for Marketplace Catalogs: From Legacy Forms to AI-Native Matching
published: 2026-08-31T19:18:07Z
authors: Kartik Ravisankar, Hojat Abdolanezhad, Daniel Capo, Sang Su Lee, Shishir Dash, Vijay Anand Raghavan
url: http://arxiv.org/abs/2609.00274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Autoresearch for Marketplace Catalogs: From Legacy Forms to AI-Native Matching

## Abstract
Two-sided service marketplaces are moving from deterministic request-form intake to AI-native probabilistic matching, enabled by large language models (LLMs) that infer intent, preferences, and latent constraints from natural language. Relying on inferred intent rather than fixed-form fields forces these platforms to regenerate the provider-side preference taxonomy underwriting matching, search, and pricing: attributes interpretable to service providers while remaining a useful signal for marketplace decisions. We present an autoresearch loop that generates this taxonomy, one occupation at a time, and has been deployed in production at a major U.S. consumer services marketplace since April 2026, spanning 132 occupations. Instead of one global hierarchy, the loop treats each occupation as an independent generation problem and runs iterative propose-evaluate-keep refinement cycles. Each candidate tag set is scored by a recalibrated six-rubric LLM-as-judge framework, and a 7-critic panel of distinct personas contributes weighted penalties to an adjusted score, with no hard vetoes. A separate parity-mapping stage maps legacy request-form Q&A pairs back to the generated taxonomy, yielding both a coverage signal and an interface for human quality assurance; it does so by first inferring the provider attribute each legacy question was meant to measure, rather than translating questions to tags literally.

## Metadata
- **Published**: 2026-08-31T19:18:07Z
- **Authors**: Kartik Ravisankar, Hojat Abdolanezhad, Daniel Capo, Sang Su Lee, Shishir Dash, Vijay Anand Raghavan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00274v1)