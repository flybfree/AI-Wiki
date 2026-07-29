---
title: A Human-in-the-Loop Corpus for LLM-Based Simplification of Scientific Summaries
url: http://arxiv.org/abs/2607.25630v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_12-12-39Z_AHuman_in_the_LoopCorpusforLLM_BasedSimplification.md
generated_at: 2026-07-28 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a human-in-the-loop corpus for simplifying scientific texts using large language models. It uses GPT-4o-mini to generate baseline summaries of SciSummNet articles and then collects feedback from STEM readers and expert editors to produce refined, accessible versions. The study shows that GPT-generated summaries are preferred in terms of comprehensibility and simplicity, while expert edits preserve domain terminology.

## Key Takeaways
- Phase 1 judgments reveal a strong preference for GPT-generated summaries on comprehensibility and simplicity metrics.
- Expert-edited reference simplifications emphasize preserving domain-specific terminology to maintain scientific accuracy.
- The released corpus includes both human judgments and automatic evaluation results, providing a benchmark for simplification systems.

## Context
Scientific communication faces challenges as interdisciplinary research grows, yet most papers are inaccessible to non-specialists. AI-driven summarization offers promise but often sacrifices essential technical language or misrepresents claims. This work addresses those trade-offs by integrating human expertise into the loop.

## Implications
For researchers developing LLM-based tools, this corpus demonstrates how automated generation can be improved with targeted human feedback. Industry practitioners can leverage the benchmark to evaluate and refine their simplification pipelines for broader audience outreach.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25630v1)
