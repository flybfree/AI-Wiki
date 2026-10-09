---
title: The Harness as the Only Mutable Surface: Compliance-Bounded Self-Evolution of LLM Agents in Credit Pipelines, with a Measured Admission Gate
url: http://arxiv.org/abs/2610.10629v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-07_12-33-48Z_TheHarnessastheOnlyMutableSurface_Compliance_Bound.md
generated_at: 2026-10-08 21:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes that self-evolving LLM agents in regulated credit pipelines must confine their adaptation to the runtime harness—instruction text, tool-call logic, and primitive composition—while keeping model weights fixed, ensuring every change is a reviewable diff with an attached cause and test. The author introduces a dual-loop engine with a single admission gate that writes a hash-chained record before deployment, and evaluates it in simulation across three families of supervisory reinterpretation at three severities, demonstrating that the gated loop admits only 144 of 7,449 candidate changes without worsening held-out error, while an unbounded alternative admits 309 harmful changes and leaves missed flags above 10% in 49 of 90 runs.

## Key Takeaways
- The admission gate acts as a hard compliance boundary: it filters 7,449 candidate changes down to 144 safe ones, restores false-positive rates to oracle level, and never raises missed flags in low- and mid-severity cells, whereas replacing the gate with the weaker check an unbounded system applies (fewer visible errors in recent traces) admits 309 harmful changes and leaves missed flags above 10% in 49 of 90 runs, showing that false positives fall only because the screening threshold was loosened rather than genuinely improved.
- When evaluated on pre-shift labels, the gate rejects every candidate, establishing a critical constraint: a supervisory reinterpretation cannot be absorbed by the agent unless it is explicitly encoded as a rule that relabels historical data, meaning the agent cannot silently "learn" a new interpretation without a traceable rule change.
- The paper maps its mechanisms to the EU AI Act's provisions for high-risk credit scoring systems and notes that the April 2026 US model-risk guidance explicitly excludes agentic AI from its scope, creating a regulatory gap where self-evolving agents operate without mandated supervisory review structures.

## Context
Self-improving LLM agents are increasingly deployed in high-stakes financial workflows such as credit scoring, where regulators require named changes, recorded tests, and documented approvals. This paper addresses a fundamental tension: an agent that rewrites its own weights or architecture destroys the auditable artifact a supervisor depends on. By bounding self-evolution to the harness layer and enforcing a hash-chained admission gate, the work bridges the gap between autonomous adaptation and regulatory reviewability, offering a concrete architectural pattern for compliance-bounded agentic systems.

## Implications
For practitioners building agentic AI in regulated credit pipelines, the paper provides a deployable architecture—dual-loop with a single admission gate—that satisfies EU AI Act requirements for high-risk systems while enabling genuine self-improvement. The finding that the gate's fixed tolerance blocks the correct primitive replacement at the highest structural severity in half the seeds highlights a practical tuning challenge: tolerance thresholds must be calibrated per severity class to avoid over-constraining legitimate structural repairs. The regulatory gap identified in US guidance signals that firms deploying agentic AI in credit decisions may need to build their own internal review gates ahead of any forthcoming US regulatory coverage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10629v1)
