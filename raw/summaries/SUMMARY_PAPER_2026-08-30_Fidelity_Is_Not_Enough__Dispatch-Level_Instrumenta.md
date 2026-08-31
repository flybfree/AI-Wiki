---
title: Fidelity Is Not Enough: Dispatch-Level Instrumentation for Agentic Datasheet Extraction
url: http://arxiv.org/abs/2608.28439v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_15-25-12Z_FidelityIsNotEnough_Dispatch_LevelInstrumentationf.md
generated_at: 2026-08-30 20:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces dispatch‑level instrumentation to detect fidelity failures in agentic document extraction where models generate answers without invoking tools. It demonstrates that a rule‑based classifier and a silent‑failure detector based solely on tool calls achieve high recall while keeping false positives low across 37 hand‑curated claims.

## Key Takeaways
- The study shows that fidelity can be compromised when tools are disabled, leading to fabricated source text.
- A silent‑failure detector that only monitors which tools were called recovers all 50 planted faults without flagging clean extractions.
- The detectors have asymmetric performance: one bounds false positives, the other is recall by construction.

## Context
In AI research on agentic systems, measuring fidelity against datasheets is crucial but often limited to post‑hoc checks. This work highlights the need for continuous observability at the dispatch level to catch silent errors before they propagate.

## Implications
Practitioners can adopt tool‑call auditing as a lightweight safeguard that improves reliability without heavy computational cost. It also underscores that fidelity may persist even when tools are bypassed, suggesting broader architectural vigilance is needed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28439v1)
