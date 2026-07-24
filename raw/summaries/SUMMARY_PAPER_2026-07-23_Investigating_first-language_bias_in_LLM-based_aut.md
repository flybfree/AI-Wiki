---
title: Investigating first-language bias in LLM-based automated essay scoring: A cross-prompt evaluation of an open-weight AI-model on TOEFL essays
url: http://arxiv.org/abs/2607.14605v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_06-10-08Z_Investigatingfirst_languagebiasinLLM_basedautomate.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how a LoRA‑adapted open‑weight LLM performs on unseen TOEFL essays and whether its scoring reflects the test taker’s first language. It reports an overall band agreement of 77.79% and a quadratic weighted kappa of 0.702, while noting that essays from European backgrounds consistently score higher than those from East‑Asian backgrounds.

## Key Takeaways
- The model shows robust cross‑prompt generalization with stable accuracy across all eight unseen prompts and no advantage for thematically related prompts.
- A systematic L1 bias exists: within each proficiency band, European‑language essays receive higher scores than East‑Asian ones despite the training data not being language‑biased.
- This is the first large‑scale fairness analysis of a fine‑tuned open‑weight LLM for automated essay scoring.

## Context
Automated essay scoring relies on AI models that must generalize to diverse test takers and prompts. Fairness in such systems is critical because biased outputs can affect educational equity and institutional trust. This study adds empirical evidence about language‑related performance gaps in a widely used assessment tool.

## Implications
The findings warn developers of open‑weight LLMs that fine‑tuning on English‑centric data may produce hidden L1 disparities, prompting the need for bias mitigation strategies. Practitioners should monitor cross‑language scoring to ensure equitable evaluation and maintain credibility with diverse test‑taker populations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14605v1)
