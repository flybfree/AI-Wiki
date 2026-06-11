---
title: OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics
url: http://arxiv.org/abs/2606.09826v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-08_17-59-43Z_OmniGameArena_AUnifiedUE5BenchmarkforVLMGameAgents.md
generated_at: 2026-06-11 10:55
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces OmniGameArena, a unified Unreal Engine 5 benchmark that evaluates twelve newly built games across Solo, PvP, and Coop modes with consistent action interfaces. It also presents the Improvement Dynamics Curve (IDC), an automated harness where tool-using reflectors refine prompts over multiple rounds to track skill evolution. The study reports cold-start leaderboard scores for twelve VLM agents and detailed IDC observables for four top agents.

## Key Takeaways
- Cold-start leaderboard scores are measured per (agent, game) pair using a single first-attempt performance metric.
- The Improvement Dynamics Curve records how agent scores evolve across reflection rounds and how learned skills perform on held-out task variants.
- OmniGameArena includes twelve games spanning Solo, PvP, and Coop with unified action interfaces to support heterogeneous evaluation.

## Context
VLM agents operate in diverse gaming contexts where existing benchmarks lack unifying protocols for comparing commercial, open-weight, and specialized policies. This gap hampers progress toward robust, adaptable game-playing models.

## Implications
A single benchmark enables fair comparison across model types and improves transparency of skill refinement processes. Practitioners can leverage IDC insights to design agents that learn iteratively within bounded prompts, advancing both research and industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.09826v1)
