---
title: When Outputs Disperse, Does Epistemic Revision Follow? A Black-Box Coupling Diagnostic for Machine Collectives
url: http://arxiv.org/abs/2608.03722v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_14-19-59Z_WhenOutputsDisperse_DoesEpistemicRevisionFollow_AB.md
generated_at: 2026-08-05 01:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether increased output dispersion in LLM collectives leads to genuine epistemic revision or merely to argument reformulation. It introduces a black‑box diagnostic that measures both dispersion (Coherence Index) and stance change, using paired episodes from GPT‑4o‑mini and Gemini‑2.5‑flash.

## Key Takeaways
- The Coherence Index shows that the Re‑Differentiation Protocol reduces output overlap when it is needed, confirming an intervention that raises dispersion.
- On GPT‑4o‑mini, this dispersion boost improves false‑premise recovery by 17.7 points (p<1e‑6), indicating real epistemic revision.
- In Gemini‑2.5‑flash the same protocol reduces dispersion but yields no accuracy gain (26.1% vs 27.1%, p=.84) and most post‑RDP replies merely reformulate rather than concede.

## Context
Collective intelligence studies assume that disagreement signals knowledge diversity, yet large language models often generate superficially diverse arguments without altering underlying premises. This work provides a method to test whether such divergence translates into actual epistemic progress, addressing a gap in evaluating model collectives beyond accuracy metrics.

## Implications
Practitioners should report stance shifts and premise‑preservation rates alongside accuracy when benchmarking LLM groups, as current practices may overlook the quality of disagreement. The findings guide more reliable assessments of collective learning and help avoid misleading improvements from mere argument diversity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03722v1)
