---
title: SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation
url: http://arxiv.org/abs/2608.21500v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-21_16-14-07Z_SecOPD_MitigatingAdaptivePromptInjectionsbyOn_Poli.md
generated_at: 2026-08-24 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Secure On‑Policy Distillation (SecOPD), a method that supplies token‑level feedback to secure large language models against adaptive prompt injections. By training on rollouts scored by an initialization model, SecOPD reduces the attack success rate of the SoTA PISmith suite from 94 % to 9.0 %, demonstrating strong generalization across unseen domains such as agentic tool calling.

## Key Takeaways
- The prior defense approaches treat whole outputs equally, limiting learning of insecure token positions.
- SecOPD provides fine‑grained feedback that distinguishes secure versus compromised tokens during distillation.
- The defended Qwen3.6‑27B model achieves 9.0 % ASR against PISmith, compared to 94.0 % for Meta‑SecAlign.

## Context
Adaptive prompt injection remains the leading threat to AI agents that consume external data, prompting a need for defenses beyond simple output filtering. Existing methods relying on sequence‑level signals cannot pinpoint which tokens are compromised, leaving models vulnerable despite high training effort.

## Implications
Fine‑grained token feedback can significantly improve model security without sacrificing performance, offering a scalable solution for developers and enterprises seeking robust AI agents. This work sets a new benchmark for prompt injection resistance across diverse application scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21500v1)
