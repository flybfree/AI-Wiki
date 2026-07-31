---
title: Flat Score, Amplified Failures: How the Error Budget Masks Damage in Quantized LLM Agents
url: http://arxiv.org/abs/2607.27275v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_12-40-04Z_FlatScore_AmplifiedFailures_HowtheErrorBudgetMasks.md
generated_at: 2026-07-30 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how 4‑bit post‑training quantization influences the performance of multi‑turn tool‑calling LLM agents on τ²‑bench, finding that the standard ten‑error budget masks damage caused by extra failures. While the overall score appears unchanged, shrinking the budget to two errors reveals a significant gap in one cell where error volume increases.

## Key Takeaways
- Quantization seems lossless because the benchmark’s ten‑error budget absorbs up to 2.5× more failures than full precision.  
- The failure set remains identical across precisions, with only 0.18% novel events and rank correlation ≥ 0.94.  
- Reducing the error budget exposes a 17‑point score gap exactly where quantization adds error volume.

## Context
Multi‑turn LLM agents depend on precise tool calls, making them vulnerable to subtle weight changes. τ²‑bench is widely used for error analysis in such settings, but its ten‑error budget can obscure performance degradation caused by quantization.

## Implications
Practitioners should report per‑channel error rates and success under shrinking budgets alongside task reward to detect hidden damage. This practice strengthens trust in quantized models and guides targeted repair strategies like prompt interventions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27275v1)
