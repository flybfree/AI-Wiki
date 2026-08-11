---
title: Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills
url: http://arxiv.org/abs/2608.07885v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_03-22-31Z_ReasonWide_NotDeep_AmortizingtheReasoningPremiumin.md
generated_at: 2026-08-10 22:32
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates why reasoning‑capable language models generate many extra tokens and how that cost can be reduced. It demonstrates that a non‑reasoning model can achieve comparable performance by receiving distilled skills extracted from either reasoning or non‑reasoning trajectories, cutting output token usage dramatically while eliminating reasoning traces.  

## Key Takeaways  
- The analysis shows a 3‑6× increase in tokens for each episode when models perform deep per‑instance reasoning, much of which is redundant procedural work.  
- A compact natural‑language skill distilled from a small corpus can recover 55‑100%+ of the reasoning gap on GPT‑5.4‑mini, surpassing pure reasoning modes on two benchmarks while emitting far fewer tokens and no reasoning tokens.  
- Skills derived solely from non‑reasoning trajectories remain competitive with those from paired reasoning/non‑reasoning corpora, indicating that wide search across episodes is often more efficient than deep per‑instance search.  

## Context  
Current large language models are evaluated on multi‑step agentic tasks where reasoning improves accuracy but at a high token cost. Researchers seek ways to amortize this cost without sacrificing performance, especially as deployment budgets limit output length and computational expense.  

## Implications  
Distilling skills enables cheaper, faster agents that can be deployed in resource‑constrained settings such as mobile or edge devices. This shift from costly per‑instance reasoning to reusable procedural knowledge could reshape model design, encouraging wider use of smaller models for complex tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07885v1)
