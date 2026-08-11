---
title: Opportunity Is Not Realizability: Selection-Valid Diagnostics for Multi-LLM Routing
url: http://arxiv.org/abs/2608.08265v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_17-53-43Z_OpportunityIsNotRealizability_Selection_ValidDiagn.md
generated_at: 2026-08-11 13:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the gap between oracle routing opportunities and deployable router performance by developing selection‑valid diagnostics for multi‑language model pools. It proves confidence intervals that hold under various selection criteria and shows that real routers capture only a fraction of the theoretical gain.

## Key Takeaways
- The oracle opportunity is quantified with confidence intervals that remain valid when testing against the best fixed model or any router family member.
- A signal‑information sandwich provides bounds on Bayes‑optimal gains while avoiding full‑information oracle pitfalls.
- Greedy submodular coverage yields a (1‑1/e) guarantee for compact pools, yet observed deployable routers recover only 7.5–14.4% of the gap.

## Context
Multi‑model routing is central to scaling AI assistants where selecting the best model per query improves quality but adds latency and complexity. Diagnostics that rely on unrealistic oracle data often mislead practitioners about achievable performance improvements.

## Implications
Practitioners can now trust interval estimates when evaluating router designs, avoiding overestimation of gains from selection. This clarifies trade‑offs between theoretical potential and real‑world deployment, guiding resource allocation in AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08265v1)
