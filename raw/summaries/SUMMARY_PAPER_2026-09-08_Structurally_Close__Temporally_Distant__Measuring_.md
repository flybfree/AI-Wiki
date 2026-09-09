---
title: Structurally Close, Temporally Distant: Measuring Security Exposure in Long-Horizon LLM Agents
url: http://arxiv.org/abs/2609.05911v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-05_06-09-06Z_StructurallyClose_TemporallyDistant_MeasuringSecur.md
generated_at: 2026-09-08 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces influence distance as a structural measure of security exposure for long‑horizon LLM agents, contrasting it with sequence distance to reveal hidden temporal gaps. Experiments on 454 injection–sink pairs across multiple models show that most attacks are temporally decoupled, with median gap nine hops.

## Key Takeaways
- Influence distance is always less than or equal to sequence distance, exposing a gap measured as ΔT.
- In 97% of cases the gap exceeds zero, indicating hidden separation between untrusted input and sensitive actions.
- A deterministic gate based on influence distance blocks five missed attack sinks without harming benign traffic.

## Context
Long‑horizon LLM agents rely on persistent memory and external tools, making security analysis challenging. Traditional step‑count metrics ignore structural dependencies, leading to overestimation of safety.

## Implications
Practitioners can design runtime guards that inspect influence pathways rather than raw sequences, improving targeted protection without unnecessary blocking. This approach refines AI risk assessment beyond simple latency thresholds.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05911v1)
