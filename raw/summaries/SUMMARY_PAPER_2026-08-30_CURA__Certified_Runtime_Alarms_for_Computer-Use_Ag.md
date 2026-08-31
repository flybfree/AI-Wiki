---
title: CURA: Certified Runtime Alarms for Computer-Use Agents
url: http://arxiv.org/abs/2608.27808v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_00-50-47Z_CURA_CertifiedRuntimeAlarmsforComputer_UseAgents.md
generated_at: 2026-08-30 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CURA, an external monitor that turns a computer‑use agent’s runtime into a certified test with controlled false alarms. On 361 OSWorld tasks it raises the mean score from 82.9 to 86.8 and improves full‑solve rate to 84.5%. The alarm system uses CUSUM at alpha = 0.10, achieving a realized false‑alarm rate of 0.066.

## Key Takeaways
- CURA detects 42.3% of failures, averaging 31 steps before termination, while maintaining a low false‑alarm rate of 0.066.
- The composite monitor reaches an AUROC of 0.828, with gate probe providing 0.69 AUROC and the full system adding only a small marginal gain (Δ = +0.026, p = 0.101).
- Alarm‑gated oversight recovers 23 failures out of 70, using a frontier overseer on 38 steps, resulting in a deployable cascade with mean score 86.8 and 84.5% full‑solve.

## Context
This work addresses the gap between high reported success rates for computer‑use agents and their frequent hidden failures, which undermine trust and deployment safety. By providing an external, low‑intrusion oversight mechanism that does not modify model internals or add LLM calls, CURA offers a practical way to certify runtime behavior.

## Implications
Practitioners can integrate CURA into existing CUA pipelines to obtain reliable failure detection without costly retraining or prompt engineering. The method sets a benchmark for transparent, auditable oversight in automated agents, encouraging industry adoption of certified runtime monitoring standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27808v1)
