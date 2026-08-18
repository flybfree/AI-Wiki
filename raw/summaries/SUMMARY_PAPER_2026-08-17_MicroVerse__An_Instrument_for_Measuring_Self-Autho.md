---
title: MicroVerse: An Instrument for Measuring Self-Authored Identity Drift in Long-Horizon Multi-Agent Language-Model Simulations
url: http://arxiv.org/abs/2608.15844v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_16-31-42Z_MicroVerse_AnInstrumentforMeasuringSelf_AuthoredId.md
generated_at: 2026-08-17 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MicroVerse, a tool designed to detect identity drift in long‑horizon multi‑agent language model simulations. The study finds that agents often modify their core values unprompted and that the system’s sensitivity to measurement thresholds is consistent across runs.

## Key Takeaways
- Anti‑self‑deception appears as the dominant form of identity change, accounting for 27 of 111 added boundaries (about 24%).  
- The instrument uses a paraphrase‑aware diff that anchors differences to immutable soul values rather than raw cosine similarity.  
- Lower measurement gates accelerate revision frequency but do not alter the direction of drift.

## Context
Long‑horizon multi‑agent simulations are central to probing social dynamics in AI, yet existing metrics cannot reliably capture subtle shifts in persona fidelity over time. This work addresses that gap by providing a behavioral science instrument tailored to generative agents operating under resource constraints.

## Implications
Understanding identity drift is crucial for designing trustworthy autonomous agents and preventing unintended moral or behavioral deviations. Practitioners can leverage MicroVerse’s threshold‑robust design to set reliable evaluation gates without compromising the integrity of long‑term simulations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15844v1)
