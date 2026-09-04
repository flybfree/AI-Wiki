---
title: DNative-Twin: Decision Graphs and Digital Twins for Reconstructable Agentic Decisions
url: http://arxiv.org/abs/2609.03787v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_12-59-34Z_DNative_Twin_DecisionGraphsandDigitalTwinsforRecon.md
generated_at: 2026-09-03 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DNative‑Twin, a graph‑native digital twin that records agentic decisions as typed trajectories and reexecutes the decision mechanism under declared conditions. The framework links observed states, taken paths, and authority sources to enable isolated replay and comparison. Experiments on enterprise logs show that adding replay context improves recall of unresolved divergences from 0 to 0.667, while verification results raise it to 1.0.

## Key Takeaways
- Graph structure localizes represented changes but cannot infer the effect of unobserved tool states.  
- Introducing a replay‑contract state increases unresolved‑divergence recall from 0 to 0.667 in controlled experiments.  
- When verification results are also available, recall reaches 1.0 across injected instances.

## Context
AI agents generate decisions that involve evidence, tools, constraints and actions, yet the underlying mechanisms remain opaque. Traditional digital twins capture snapshots but lack the ability to replay full decision pathways under varying conditions, limiting trustworthy verification.

## Implications
The work highlights a gap between graph representation and causal understanding in AI decision systems. Practitioners can leverage DNative‑Twin to build more reliable auditable models that separate structural insights from consequential outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03787v1)
