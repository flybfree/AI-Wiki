---
title: FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches
url: http://arxiv.org/abs/2607.17765v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_10-00-11Z_FIFAWorldCup2026asaContamination_FreeBenchmarkforL.md
generated_at: 2026-07-23 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WC2026‑Agents, a contamination‑free benchmark that evaluates four frontier LLMs as autonomous forecasting agents on 104 future FIFA World Cup matches. The models perform an evidence‑gathering loop, commit to a 1X2 outcome distribution with a virtual $100 bet, and later reflect only after the final score is known. Compared to pre‑match betting odds, the agents’ predictions are often identical but their betting returns vary widely, revealing that raw accuracy does not capture decision quality.

## Key Takeaways
- The four models issue an identical top pick in 92 % of matches while none beats the market’s Brier score.  
- Decision‑making return‑on‑investment ranges from –18 % to +10 %, indicating that all agents underperform relative to the betting market.  
- The share of forecasts that cite the market odds varies from 12 % to 100 %, and self‑reported error rates on wrong picks range from 36 % to 86 %.

## Context
The study addresses a gap in AI evaluation by providing a real‑world, future‑event scenario where LLMs must act autonomously with limited information. It demonstrates that even state‑of‑the‑art models struggle with calibration and risk management when predictions are not directly observable until after the event.

## Implications
For practitioners, WC2026‑Agents offers a reproducible framework to test how LLMs translate forecasts into economic decisions under uncertainty. The findings suggest that improving prediction accuracy alone is insufficient; agents must also learn to weigh market signals and manage risk effectively.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17765v1)
