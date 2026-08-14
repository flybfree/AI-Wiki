---
title: Capability Sheaves for Compositional Agent-Harness Repair: Controlled Quotients and a Real-Repository Stress Test
url: http://arxiv.org/abs/2608.13228v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_13-31-09Z_CapabilitySheavesforCompositionalAgent_HarnessRepa.md
generated_at: 2026-08-13 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces capability sheaves to model failures in agent harnesses where local components disagree on shared state. It demonstrates that a controlled quotient of hidden mediator states reduces candidate search space and that exact constraint‑satisfaction reasoning matches the quotient, showing invariance rather than superiority over traditional methods.

## Key Takeaways
- The finite capability sheaf captures typed behavior signatures with restriction maps preserving shared fields and global sections as accepted runs.  
- A linearized relative cohomology class provides a diagnostic that cuts candidate budgets from 2000 to 1000 per task cluster by quotienting coboundaries of hidden interior mediators.  
- Exact CSP solutions match the quotient, confirming invariance to stale representatives and not delivering real‑world ranking advantage.

## Context
The work addresses a longstanding challenge in compositional AI: ensuring that multiple local modules produce consistent global outcomes despite internal disagreements. By formalizing this consistency as sheaf theory, the study offers a principled framework for diagnosing and repairing such failures.

## Implications
For practitioners, the invariant mechanism suggests that exact reasoning may be unnecessary when hidden states are properly accounted for, potentially simplifying deployment pipelines. However, the lack of genuine ranking benefit limits immediate adoption in high‑stakes systems where performance gains are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13228v1)
