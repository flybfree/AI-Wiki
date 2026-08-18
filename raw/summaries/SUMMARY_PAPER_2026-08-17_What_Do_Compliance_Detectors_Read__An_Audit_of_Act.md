---
title: What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models
url: http://arxiv.org/abs/2608.16852v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_17-37-07Z_WhatDoComplianceDetectorsRead_AnAuditofActivationP.md
generated_at: 2026-08-17 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether current compliance detectors for deployed language models truly follow the rules they are meant to enforce, a phenomenon termed rule blindness. Experiments show that altering or removing governing clauses does not change detection accuracy across various guard and activation probe designs, indicating that detectors rely on superficial cues rather than substantive reasoning.

## Key Takeaways
- Deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged for every guard and activation probe we test.  
- A purpose‑built benchmark with two rules and two scenarios demonstrates that neither alone predicts the label, confirming rule blindness under a design no prior benchmark rules out.  
- The Internal Compliance Score (ICS) is a training‑free readout that scores responses but fails to meet pre‑registered criteria for beating trivial baselines.

## Context
The paper addresses a growing need in AI safety where regulatory compliance is treated as an audit control, yet existing detectors often ignore the underlying rules. This gap raises questions about trustworthiness and accountability of automated monitoring systems.

## Implications
For practitioners, rule blindness means that compliance checks cannot be relied upon to produce meaningful audits without costly retraining. The release of a counterfactual protocol offers a tool for future research to verify guard claims, but it also highlights the need for more robust, reasoning‑based detection mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16852v1)
