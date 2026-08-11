---
title: SHE: Trajectory-driven Safety Harness Evolution for LLM Agents
url: http://arxiv.org/abs/2608.09885v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_17-35-08Z_SHE_Trajectory_drivenSafetyHarnessEvolutionforLLMA.md
generated_at: 2026-08-10 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Safety Harness Evolution (SHE), a framework that treats the safety harness of LLM agents as an evolving artifact rather than a static deployment. By decomposing the harness into four components and learning from rollout trajectories, SHE reduces unsafe responses by 3.1‑fold while preserving utility. The evolved harness also generalizes to new risks across models without retraining.

## Key Takeaways
- SHE learns evolving safe boundaries directly from trajectory failures, converting them into structured diagnoses that guide artifact‑specific refinements.  
- The framework assigns clear safety responsibilities to the System Prompt, Rule Bank, Safety Memory, and Tool Policy, enabling localized evolution of each component independently.  
- Experiments on Agent‑SafetyBench show a 3.1× reduction in ASR compared with static SafeHarness, alongside improved benign utility.

## Context
Current LLM safety research often assumes the harness is immutable, which hampers adaptation to new threats. This limitation can lead to brittle safety guarantees and inefficient updates as risk landscapes shift. SHE addresses these challenges by modeling the harness as a dynamic system that can be iteratively refined.

## Implications
For practitioners, SHE offers a practical pathway to continuously improve LLM safety without sacrificing performance, reducing reliance on costly retraining cycles. In industry, adopting such evolution‑driven approaches could lead to more resilient AI systems that stay safe across diverse operational contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09885v1)
