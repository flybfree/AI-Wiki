---
title: How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks
url: http://arxiv.org/abs/2608.14905v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_21-39-38Z_HowDoAgentsFailonAutoResearch_End_to_EndDiagnostic.md
generated_at: 2026-08-17 21:42
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AutoResearchEval, a comprehensive evaluation of 100 frontier research tasks across seven domains to diagnose failures in end-to-end autonomous scientific agents. It discovers that all agents share a common metacognitive deficit: they cannot verify their outputs against evidence or revise when incorrect. The failure taxonomy ARFT catalogs 45 empirically grounded patterns.

## Key Takeaways
- AutoResearchEval spans the full research lifecycle, providing process-level annotations for 800 agent trajectories across eight harness-model combos.
- A human-calibrated agent-as-a-judge pipeline enables fine-grained attribution of failures to specific artifacts rather than high‑level model errors.
- The ARFT taxonomy reveals a unified metacognitive limitation: agents lack the ability to check their work against evidence and iterate.

## Context
Current AI research focuses on narrow task performance, often ignoring how complex workflows unfold. This study moves beyond static benchmarks to capture dynamic processes, offering a richer view of autonomous discovery systems.

## Implications
For researchers building agentic scaffolds, the findings suggest that improving metacognitive loops is essential before expecting reliable end‑to‑end research assistance. The released dataset and taxonomy can guide systematic debugging and future model design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14905v1)
