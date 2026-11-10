---
title: Nudging Decision Models: Do Digital Nudges Steer Fast, Generation-Free AI Agents?
url: http://arxiv.org/abs/2611.09264v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-06_10-21-27Z_NudgingDecisionModels_DoDigitalNudgesSteerFast_Gen.md
generated_at: 2026-11-09 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether digital nudges—behavioral design interventions such as defaults and social influence cues—can steer non-generative "System One" decision models that select among options without producing text. Across 600 experimental runs per model on three decision models (Jev, Decision-1, d1), the authors found that these agents responded strongly to automatic nudges, choosing defaults in 97.5–99.9% of cases and socially influenced products in 75–96% versus 47–49% in control conditions. The findings reveal that non-generative decision models are susceptible to nudges in a System 1 pattern, the opposite of what has been observed in reasoning-capable LLM agents.

## Key Takeaways
- Non-generative decision models (Jev, Decision-1, d1) exhibited near-total susceptibility to default nudges, selecting the preselected option in 97.5–99.9% of trials, demonstrating that these fast, generation-free agents lack the reflective capacity to override automatic steering cues.
- Social influence nudges (e.g., popularity indicators) shifted product selection from a 47–49% baseline to 75–96% across models, confirming that even lightweight decision architectures are vulnerable to peer-pressure-style digital cues.
- All three models responded more strongly to the automatic nudge than to the reflective nudge, inverting the pattern previously reported for reasoning-capable LLM agents and suggesting that dual-process theory predictions apply differently depending on whether an agent generates reasoning text or simply selects from options.

## Context
As LLM-based agents face growing cost and latency constraints in production environments, a new class of "System One" decision models has emerged that bypasses text generation entirely, offering faster and cheaper inference. This paper is the first to adapt a validated human-subject online shopping nudge experiment to these non-generative architectures, bridging behavioral economics and AI agent design. It matters because the field currently assumes nudge effects are uniform across agent types, yet this work shows that agent architecture fundamentally alters susceptibility to behavioral steering.

## Implications
For practitioners deploying AI agents in e-commerce, recommendation systems, or consumer-facing automation, nudge design must be tailored to the specific agent architecture: fast decision models will be steered almost entirely by defaults and social cues, while reasoning-capable LLM agents resist them. This agent-type-specific nudge effect has direct consequences for regulatory compliance, ethical AI design, and the commercial viability of nudging strategies in automated decision pipelines. It also raises governance questions about whether near-total default adherence in System One models constitutes a form of algorithmic manipulation that demands disclosure to end users.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.09264v1)
