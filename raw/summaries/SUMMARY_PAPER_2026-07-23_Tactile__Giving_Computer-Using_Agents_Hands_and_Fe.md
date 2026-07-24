---
title: Tactile: Giving Computer-Using Agents Hands and Feet
url: http://arxiv.org/abs/2607.14443v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_00-35-25Z_Tactile_GivingComputer_UsingAgentsHandsandFeet.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Tactile, an open‑source tool layer that replaces brittle screen‑clicking with a reliable “hands and feet” interface for computer‑using agents. By converting UI evidence into actionable, verifiable objects, Tactical improves the success rate of code‑generation tasks from 41.1% to 50.0% on macOSWorld‑style problems.

## Key Takeaways
- Tactile creates compact target candidates that include source labels, roles or text, state, geometry, executable affordances, and verification cues, turning raw UI data into structured interface states.
- The observe‑ground‑act‑verify loop prefers native semantic actions when possible, falls back to OCR‑grounded coordinates only when visible text is the best evidence, and retains full provenance for replay and failure attribution.
- Experiments on a 96‑task cross‑agent subset show consistent gains across Codex, Claude Code, OpenCode, and Goose, raising overall success from 41.1% to 50.0%.

## Context
Computer‑use agents currently rely on fragile visual parsing that collapses grounding, execution, and verification into a single ambiguous operation. This limitation hampers the integration of AI agents with desktop applications, limiting their practical usefulness.

## Implications
For practitioners, Tactile provides a reusable substrate that exposes software actions as semantic objects, enabling more robust and auditable automation pipelines. The field will benefit from a shift toward verifiable execution layers rather than relying solely on stronger models to compensate for brittle interfaces.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14443v1)
