---
title: Silent Alarm: A J-Space Protocol for Comparing Danger Recognition Across Models and Quantization Levels
url: http://arxiv.org/abs/2607.12792v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-14_14-08-18Z_SilentAlarm_AJ_SpaceProtocolforComparingDangerReco.md
generated_at: 2026-07-23 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces JADR, a protocol that evaluates the internal safety mechanisms of language models by measuring their Jacobian space representation before any token is emitted. By comparing top‑k J‑space tokens from danger and safe prompts, the authors develop SafetyAUC with confidence intervals to quantify model robustness across architectures and quantization levels.

## Key Takeaways
- The method extracts the top‑k Jacobian‑space tokens at each layer, providing a direct view of the model’s internal representation of safety concepts.
- It evaluates models against a local SafeREJECT danger sample using only their own activations, eliminating reliance on an external judge and allowing fair comparison between quantization schemes.
- SafetyAUC with bootstrap confidence intervals reliably separates strong from weak internal safety mechanisms with statistical significance.

## Context
Traditional LLM‑based safety benchmarks depend on subjective human grading, which can mask subtle failures. This work offers a local, model‑agnostic metric that captures hidden fragility without external judgments.

## Implications
The protocol enables industry stakeholders to benchmark quantization and fine‑tuning effects on safety objectively, guiding decisions about trade‑offs between efficiency and robustness in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.12792v1)
