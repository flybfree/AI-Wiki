---
title: DuplexSpeechBench-IFEval: Evaluating Implicit Instruction Following in Full-Duplex Voice Agents
url: http://arxiv.org/abs/2609.03423v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_06-28-02Z_DuplexSpeechBench_IFEval_EvaluatingImplicitInstruc.md
generated_at: 2026-09-03 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DuplexSpeechBench‑IFEval, a benchmark that evaluates how full‑duplex voice agents implicitly follow conversational instructions across eight assistant roles and five conditioning protocols. The study measures real‑time floor management with an Instruction Adherence Score (IAS) and persona consistency with a Persona Adherence Score (PAS). Across six systems, it finds that architecture influences performance: explicit instructions improve adherence while persona‑only conditions reduce scores by 9.7% for F‑Actor and 4.5% for PersonaPlex.

## Key Takeaways
- The benchmark demonstrates a significant drop in floor management when agents must infer behavior from a persona only, with IAS decreasing by up to 9.7% compared to explicit instructions.
- Even when systems correctly apply conflicting directives to their assigned personas, they still fail to override those personas under safety conflicts, indicating limited conflict resolution capability.
- Some models like GPT‑Realtime and MiniCPM‑o maintain high PAS but show little change in floor behavior between explicit and persona‑only conditioning, revealing a disconnect between content fidelity and conversational timing.

## Context
Full‑duplex voice agents must continuously manage turns, backchanneling, and proactive actions without human intervention. Existing benchmarks rely on explicit turn instructions, while real deployments often use role‑based personas that require implicit behavior inference, creating a gap in evaluating truly adaptive conversational systems.

## Implications
For practitioners, the results highlight the need for architectures that can seamlessly switch between explicit and inferred behaviors while respecting safety constraints. Industry developers should prioritize models that balance persona consistency with real‑time floor management to deliver natural, safe human‑like interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03423v1)
