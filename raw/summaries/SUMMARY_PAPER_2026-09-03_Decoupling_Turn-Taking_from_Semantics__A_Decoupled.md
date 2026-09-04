---
title: Decoupling Turn-Taking from Semantics: A Decoupled Data Approach for Finite-State-Machine-Based Full-Duplex Dialogue
url: http://arxiv.org/abs/2609.03321v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_03-17-07Z_DecouplingTurn_TakingfromSemantics_ADecoupledDataA.md
generated_at: 2026-09-03 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a decoupled data approach for full‑duplex dialogue that separates turn‑taking from semantics using real spoken Human‑Human (HH) audio and synthetic Human‑Agent (HA) text. It uses a rule‑based event classification to serialize HH dialogues into finite‑state‑machine tapes, enabling supervised learning without LLM annotations. Experiments demonstrate improved turn‑taking performance while preserving the foundation model’s semantic ability.

## Key Takeaways
- The method separates turn‑taking control from semantic generation by training on real spoken HH audio and synthetic HA text.
- A rule‑based event classification serializes HH dialogues into FSM tapes, allowing scalable supervision without LLM‑generated annotations.
- The Source‑Aware Calibrated loss jointly aligns state transition token distributions with the appropriate data source.

## Context
Full‑duplex dialogue systems aim to enable simultaneous speaker modeling and response generation, yet most approaches rely on synthetic data that cannot capture the fine‑grained acoustic dynamics of human speech. This work bridges that gap by grounding turn‑taking supervision in authentic spoken interactions while leveraging existing LLM semantics.

## Implications
Practitioners can adopt this decoupled framework to build more natural conversational agents without costly annotation pipelines, reducing reliance on synthetic data generation. The approach may also inspire hybrid models that combine real audio cues with language models for richer dialogue experiences.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03321v1)
