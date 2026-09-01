---
title: Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection
url: http://arxiv.org/abs/2608.30041v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_20-57-47Z_Reachability_BasedCapabilityConfinementforLLMAgent.md
generated_at: 2026-08-31 21:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SkillGuard, a harness-level enforcement layer that treats contamination from untrusted data as a security event and restricts future agent capabilities to prevent forbidden states. It builds a Skill Impact Graph, uses steerability signatures for skill parameters, and mediates invocations with an inline reference monitor. Experiments show SkillGuard eliminates attack success on three of four suites and reduces it to low percentages, outperforming baselines while preserving utility.

## Key Takeaways
- SkillGuard treats untrusted data entry as contamination and enforces capability restrictions based on a computed Skill Impact Graph rather than simple classification.
- It restricts future skill invocations using binary, fractional, or fractional-flow strategies without requiring additional language-model inference.
- The approach reduces attack success rates to 4.8% (Slack) and 14.3% for Gemini, outperforming all baselines while maintaining high benign utility.

## Context
LLM agents increasingly rely on external skills that can be influenced by attacker-controlled data, creating vulnerabilities where contamination propagates through state changes. Current defenses often focus on input filtering or operation authorization but do not model how future authority should adapt to contaminated inputs, leaving a gap in holistic security enforcement.

## Implications
SkillGuard provides a practical framework for dynamically adjusting agent capabilities based on trustworthiness of internal state, offering a scalable defense that integrates with existing skill pipelines. This could help organizations mitigate indirect prompt injection attacks without sacrificing performance or requiring costly model calls.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30041v1)
