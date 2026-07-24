---
title: Position Bias is Hidden Behind Ceiling Effects: A Permutation Diagnostic for LLM Benchmarks
published: 2026-07-23T02:45:02Z
authors: Hiroki Tamba
url: http://arxiv.org/abs/2607.20864v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Position Bias is Hidden Behind Ceiling Effects: A Permutation Diagnostic for LLM Benchmarks

## Abstract
Position bias in multiple-choice LLM evaluation is widely cited as a confound in capability comparisons, but published measurements rely on single answer-order shuffles whose results confound the bias signal with content-level noise and sampling stochasticity. I introduce inspect_permute, an open-source extension to the inspect_ai evaluation framework that runs exhaustive answer-order permutations per question and reports the chi-squared / Cramer V signature of position bias with bootstrap confidence intervals. I apply the tool across four vendors (gpt-4o-mini, claude-haiku-4-5, gemini-2.5-flash, grok-3) on five MMLU subjects, 24,000 API calls under temperature-0 generation, with falsifier predictions pre-registered via a public SHA-256 hash before half the data was observed. Position bias turns out to be statistically detectable only within a roughly 60-95% base-accuracy Goldilocks zone. Below it, processing-load dominance swamps subject-specific signal; above it, ceiling effects compress the variance below the chi-squared test resolution. Detectable cells separate into two mechanism types: monotone A-to-D decrease (processing_load, in low-tier models) and non-monotone D-drop (content_ambiguity, in a narrow capability band). Standard MMLU places every frontier-tier model above the detection band, so absence of signal there should be read as not measurable, not unbiased. Together with the ceiling-effect characterisation in arXiv:2606.26185, this work brackets the detectable region of position-bias measurement and makes the field central question askable in a verifiable form. Package, data, preregistration under MIT.

## Metadata
- **Published**: 2026-07-23T02:45:02Z
- **Authors**: Hiroki Tamba
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20864v1)