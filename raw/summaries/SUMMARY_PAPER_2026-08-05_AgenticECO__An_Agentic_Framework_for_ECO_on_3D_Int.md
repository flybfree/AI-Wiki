---
title: AgenticECO: An Agentic Framework for ECO on 3D Integrated Circuits
url: http://arxiv.org/abs/2608.03738v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_14-32-43Z_AgenticECO_AnAgenticFrameworkforECOon3DIntegratedC.md
generated_at: 2026-08-05 01:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AgenticECO, an evidence-gated tool-using agent workflow that automates ECO on 3D integrated circuits using the open-source TaiWei flow. It achieves higher clearance rates than manual repair and stock repair while keeping router disturbance minimal.

## Key Takeaways
- The agent clears seven out of nine natural defect cases versus two for full reroute and stock repair, demonstrating significant improvement in ECO success.
- Mean disturbance is only 0.66% over cleared cases and zero clock nets are touched, showing minimal impact on timing.
- A blind diagnostic restores every injected defect with zero wrong edits, confirming the approach's precision.

## Context
The paper addresses a growing challenge as Moore’s law slows and 3D integration becomes mainstream, where manual ECO processes become error-prone and time-consuming. This work contributes to AI-driven automation in semiconductor manufacturing by integrating evidence-gated reasoning into routing decisions.

## Implications
Automating ECO with an agent can reduce rework costs and improve yield on complex 3D ICs, making the technology more viable for high-volume production. Practitioners can adopt this framework to maintain legal landings while minimizing disruption, supporting tighter clock constraints and regulatory compliance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03738v1)
