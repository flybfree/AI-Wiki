---
title: AgentWorld: Personality-Aware Reliability Evaluation for Agentic Information Retrieval
url: http://arxiv.org/abs/2608.24076v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_05-15-33Z_AgentWorld_Personality_AwareReliabilityEvaluationf.md
generated_at: 2026-08-25 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AgentWorld, a simulation framework that evaluates agentic information retrieval with personality diversity and adversarial robustness. It combines Big Five personality profiles with tool-use environments and uses pass^k consistency metrics to measure reliability across user personas and task variations. Experiments show significant performance gaps linked to personality variation and latent brittleness.

## Key Takeaways
- The framework reveals that the same task yields different pass rates (50% vs 100%) across personas, exposing cross-domain leakage and contextual drift as failure modes not caught by uniform testing.
- Pass^k alone cannot capture trajectory-level brittleness; the adversarial Risk Analyser quantifies risk via ΔP/ΔT scoring, Dempster–Shafer fusion, and Shapley attack attribution, revealing system and action vulnerabilities.
- Personality-driven user populations expose a 0.27-point quality gap compared to uniform testing, demonstrating that personality diversity is essential for reliable agentic retrieval.

## Context
Current AI evaluation often assumes homogeneous users and ignores personality or adversarial failures, limiting trust in agentic systems. This work addresses the need for models that perform consistently across diverse human interactions and can be stress-tested against realistic perturbations.

## Implications
For practitioners, AgentWorld provides a repeatable method to benchmark agents under real-world persona diversity, guiding design toward robustness. Industries relying on conversational AI must adopt such evaluations to prevent hidden failures that degrade user experience at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24076v1)
