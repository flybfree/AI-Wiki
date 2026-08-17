---
title: Explanation Multiplicity: Circuit-Level Interpretability Evidence Does Not Survive Defensible Analytic Variation
url: http://arxiv.org/abs/2608.13754v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_20-27-56Z_ExplanationMultiplicity_Circuit_LevelInterpretabil.md
generated_at: 2026-08-16 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether circuit‑level interpretability evidence can be reliably used to generate the technical documentation required by the EU AI Act. It shows that when the same analysis is performed under different defensible settings, the derived statements flip dramatically, indicating a lack of filability for such evidence.

## Key Takeaways
- The claim map produces a statement that flips across 73.2% of specification pairs (95% CI 0.725 to 0.738), violating the filability criterion required by conformity assessors.
- Even when fixing circuit size and using a single evaluation metric, the flip rate remains high at 27.1%, suggesting that circuit characteristics cannot stabilize the output.
- The circuits underlying these claims are nearly disjoint (median Jaccard overlap 4%) and functionally uncorrelated (Cohen's kappa 0.015), indicating instability is not due to rephrasing of a single mechanism.

## Context
The EU AI Act mandates that high‑risk AI systems provide transparent, verifiable documentation of decision processes, with mechanistic interpretability being the primary source. This study tests whether circuit discovery can meet those standards across multiple analytic settings, highlighting a gap between theoretical promise and practical compliance.

## Implications
Practitioners may overestimate the reliability of circuit‑based explanations for regulatory filings, leading to non‑compliant systems. The findings suggest that additional safeguards or alternative interpretability methods are needed before such evidence can be trusted in high‑risk AI deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13754v1)
