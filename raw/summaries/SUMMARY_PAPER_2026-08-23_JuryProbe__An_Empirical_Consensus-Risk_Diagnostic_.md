---
title: JuryProbe: An Empirical Consensus-Risk Diagnostic for Routing Reference-Free Factuality Judge Panels to Grounded Verification
url: http://arxiv.org/abs/2608.20607v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-20_23-11-55Z_JuryProbe_AnEmpiricalConsensus_RiskDiagnosticforRo.md
generated_at: 2026-08-23 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
JuryProbe is an empirical diagnostic that estimates consensus risk in reference‑free factuality judge panels and pairs it with a routing policy that grounds high‑risk acceptances to trusted references. The study shows that flagged high‑risk panels can reduce false accepts by 28 % while keeping coverage nearly unchanged, and that unanimous false consensus disappears under the best‑case diagnostic.

## Key Takeaways
- Correlated false negatives are observed in reference‑free panels (FN‑only correlations around 0.4) indicating shared blind spots.
- When a trusted‑reference best‑case diagnostic is applied, unanimous false consensus drops to zero on both minimal and non‑minimal evidence splits.
- A fixed rule flags 8–10 of 10 synthetic, benchmark‑authored, and scientific splits with improvement, while the negative control shows no benefit.

## Context
The rise of inexpensive LLM judges for factuality tasks has introduced a hidden risk: agreement among judges may stem from false‑negative blind spots rather than independent evidence. This paper addresses that risk by providing an empirical diagnostic to detect such dependency before routing decisions are made.

## Implications
For practitioners, JuryProbe offers a practical way to reduce false accepts without sacrificing much coverage, improving the reliability of AI‑driven fact verification systems. However, it provides only an empirical diagnostic and no formal risk guarantee, so periodic recalibration is still needed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20607v1)
