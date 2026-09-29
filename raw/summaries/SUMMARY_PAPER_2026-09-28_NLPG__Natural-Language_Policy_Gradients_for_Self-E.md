---
title: NLPG: Natural-Language Policy Gradients for Self-Evolving Language Agents
url: http://arxiv.org/abs/2609.33379v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_09-01-48Z_NLPG_Natural_LanguagePolicyGradientsforSelf_Evolvi.md
generated_at: 2026-09-28 21:41
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Natural-Language Policy Gradients (NLPG), an external policy-memory method designed to enhance the performance of fixed large language model agents without altering their underlying parameters or program structure. NLPG addresses failures in local procedural decisions by diagnosing execution traces, propagating feedback backward through module graphs, and generating route-local natural-language corrections that are aggregated into bounded updates for future executions. Experimental results demonstrate significant improvements across six diverse benchmarks, outperforming strong baselines by an average of 8.71 percentage points while maintaining agent interpretability.

## Key Takeaways
- NLPG operates as an external policy-memory mechanism that enables continual improvement of a frozen agent, circumventing the need for model retraining or structural program modifications often required by existing reinforcement-learning and prompt-optimization techniques.
- The method systematically diagnoses execution traces to propagate downstream feedback backward through the module graph, converting recurring failures into route-local natural-language corrections that are aggregated into bounded policy updates for subsequent agent runs.
- Across six benchmarks spanning memory, reasoning, instruction following, and evidence verification, NLPG achieves an average performance gain of 8.71 percentage points over the strongest listed baselines, proving that procedural experience can be effectively transformed into local and interpretable policy updates.

## Context
Large language model agents increasingly depend on compound programs for complex tasks, yet their reliability is often compromised by errors in local procedural decisions rather than global capability deficits. Current optimization strategies frequently rely on scalar rewards or wholesale prompt modifications, which fail to capture granular procedural nuances or preserve the integrity of a frozen agent. This work addresses a critical gap by providing a mechanism to evolve agent behavior through interpretable, localized corrections without disrupting the core model or workflow architecture.

## Implications
Practitioners can leverage NLPG to iteratively refine agent performance in production environments without incurring the high costs associated with retraining models or rewriting complex program structures. The generation of natural-language corrections offers enhanced interpretability, allowing developers to understand and verify specific procedural adjustments made by the system. This approach establishes a viable pathway for self-evolving agents that accumulate procedural knowledge over time while maintaining stability and transparency in their operations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33379v1)
