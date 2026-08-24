---
title: JuryProbe: An Empirical Consensus-Risk Diagnostic for Routing Reference-Free Factuality Judge Panels to Grounded Verification
published: 2026-08-20T23:11:55Z
authors: Tianxin Zhou, Ruixi Lin
url: http://arxiv.org/abs/2608.20607v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JuryProbe: An Empirical Consensus-Risk Diagnostic for Routing Reference-Free Factuality Judge Panels to Grounded Verification

## Abstract
Panels of inexpensive LLM judges increasingly make accept-or-escalate decisions. In factuality settings, accepting a claim because several reference-free judges agree can create a hidden risk: agreement may reflect shared false-negative blind spots rather than independent evidence. We introduce JuryProbe, an empirical consensus-risk diagnostic for reference-free factuality judge panels, paired with a calibration-based routing policy. JuryProbe estimates consensus risk from a labeled calibration probe using false-negative-only (FN-only) judge correlation and false-consensus lift; when flagged high-risk, reference-free majority accepts are routed to the same judges with trusted references. On audited FEVER corruptions, reference-free panels show correlated false negatives (FN-only correlations 0.402 and 0.368; lifts 3.13x and 18.13x), while unanimous false consensus drops to zero under a trusted-reference best-case diagnostic on both minimal-pair and non-minimal-pair evidence. In flagged settings, the routed policy is by construction equivalent to grounding every reference-free majority accept (verified in 34/34 splits): improvement comes from accept-conditioned grounding, while the diagnostic determines whether to activate it. A fixed, pre-specified rule flags 8-10 of 10 splits across synthetic, benchmark-authored, and scientific families and 0 of 10 on a negative control, where standing down avoids 28% of reference acquisitions at a 0.004 increase in false accepts. False-accept reduction persists under weak BM25 retrieval at substantial coverage cost, while stale stand-down labels require periodic recalibration. JuryProbe provides no formal risk guarantee and does not establish reliable stand-down on natural panels; its supported contribution is an empirical diagnostic of high-risk panel error dependence.

## Metadata
- **Published**: 2026-08-20T23:11:55Z
- **Authors**: Tianxin Zhou, Ruixi Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20607v1)