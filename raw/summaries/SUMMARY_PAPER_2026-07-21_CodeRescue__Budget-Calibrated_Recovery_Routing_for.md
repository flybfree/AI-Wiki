---
title: CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents
url: http://arxiv.org/abs/2607.19338v1
type: paper-summary
date: 2026-07-21
source_paper: 2026-07-21_17-56-49Z_CodeRescue_Budget_CalibratedRecoveryRoutingforCodi.md
generated_at: 2026-07-21 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CodeRescue, a budget-calibrated recovery routing method for coding agents that decides when to retry cheap models versus escalate to expensive ones after execution failures. It trains a supervised router on rollout data and adds a Conformal Risk Control layer that selects deployment-time cost penalties without retraining, enabling marginal expected-cost control under exchangeability. Experiments show the calibrated frontier outperforms fixed actions, prompt-only routers, and binary cascade baselines, achieving higher success rates while using only 35% of mean recovery cost in GPT-5.4-nano/GPT-5.4 setting.

## Key Takeaways
- The router learns from execution rollouts to route cheap recovery attempts after failures, balancing cost and success probability.
- Conformal Risk Control provides a deployment-time cost penalty that controls expected cost without retraining, preserving flexibility under budget changes.
- In GPT-5.4-nano/GPT-5.4, the calibrated frontier exceeds always-escalate solve rate while using only 35% of mean recovery cost.

## Context
Coding agents face a trade‑off between computational expense and problem resolution after an attempt fails. Traditional cost‑aware strategies either cascade to expensive models or abandon cheap attempts, limiting efficiency. This work addresses the need for adaptive routing that can dynamically allocate budget across heterogeneous actions based on real feedback.

## Implications
The approach offers practitioners a scalable way to manage agent budgets in production coding environments, improving resource utilization without sacrificing performance. By decoupling cost control from model selection, it enables continuous deployment of recovery systems under varying financial constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19338v1)
