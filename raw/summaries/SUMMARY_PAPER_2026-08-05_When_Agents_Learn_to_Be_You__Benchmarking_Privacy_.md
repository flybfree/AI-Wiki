---
title: When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills
url: http://arxiv.org/abs/2608.03700v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_14-04-56Z_WhenAgentsLearntoBeYou_BenchmarkingPrivacyLeakage_.md
generated_at: 2026-08-05 01:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AntiSkillBench, a benchmark to evaluate privacy leakage, impersonation risk, and defenses in persona skills. Experiments across three agents reveal persistent risks from explicit attributes to communication styles. Existing defenses are limited and depend on distillation protocols.

## Key Takeaways
- The dataset contains 7,500 dialogue traces built from 50 profiles covering diverse tasks, enabling evaluation of privacy leakage at skill level.
- Privacy leakage persists beyond explicit attribute disclosure, affecting communication style and personality traits across agents.
- Defenses show limited effectiveness that varies with distillation strategy, failing to generalize across risk and protocol.

## Context
Persona skills aggregate personal interaction data into executable artifacts used for personalization. This concentration of fragmented signals creates new attack surfaces not addressed by traditional individual record protections.

## Implications
For developers, the findings stress the need for privacy-preserving pipelines that protect both skill content and its downstream use. Practitioners must adopt defenses that are robust across different agents and distillation methods to maintain authenticity and confidentiality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03700v1)
