---
title: Agentic Data Cleaning Without a Clean Reference: An Experimental Study of Capabilities and Trade-offs
url: http://arxiv.org/abs/2608.14765v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_11-55-53Z_AgenticDataCleaningWithoutaCleanReference_AnExperi.md
generated_at: 2026-08-17 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how various agent capabilities influence reference‑free data cleaning when no trusted clean reference exists. It evaluates seven configurations on financial, clinical and environmental datasets using synthetic corruption and reports that deterministic profiling gave the highest detection F1 of 0.561 while LLM‑based full conservative achieved 0.421 but no single configuration excelled across all metrics.

## Key Takeaways
- Deterministic profiling alone provides the best detection performance with an F1 score of 0.561, showing that simple rule‑based methods can outperform complex agents in this setting.
- The full conservative LLM configuration yields the highest overall F1 among agentic approaches at 0.421, yet it still falls short compared to profiling and introduces no unsafe repairs.
- All configurations suffer from trade‑offs between detection accuracy, evidence grounding, conservative behaviour, reproducibility and operational cost, indicating that adding capabilities does not guarantee consistent improvement.

## Context
Reference‑free data cleaning remains a critical challenge for AI agents because errors can be genuine or valid observations. Existing work often relies on curated clean references which are unavailable in real‑world pipelines. This study contributes an evidence‑grounded framework that systematically combines profiling, LLM reasoning and executable tools to evaluate these trade‑offs.

## Implications
For practitioners, the findings suggest that starting with lightweight, deterministic methods may be more effective than deploying full AI agents for data cleaning tasks. The paper also highlights the need for transparent provenance logging and conservative repair policies to ensure reproducibility and safety in automated pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14765v1)
