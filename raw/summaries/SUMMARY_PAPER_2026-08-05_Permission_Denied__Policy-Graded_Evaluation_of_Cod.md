---
title: Permission Denied: Policy-Graded Evaluation of Coding Agents in Hardened Environments
url: http://arxiv.org/abs/2608.02670v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-02_14-26-12Z_PermissionDenied_Policy_GradedEvaluationofCodingAg.md
generated_at: 2026-08-05 01:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates twelve coding agents on Terminal‑Bench under nested security policies that mimic real enterprise restrictions, showing how performance degrades and how model choice interacts with policy severity. The strictest policy yields an 18.3 point success loss and a 167 % cost increase, indicating that hardening is costly but not uniform across models. It also reveals that agents often grind into timeouts or produce incorrect solutions rather than failing early.

## Key Takeaways
- Under the strictest policy, success losses reach 18.3 points and cost inflation reaches 167.3 %, showing severe performance degradation.
- The two axes of success and efficiency disagree; the model that preserves most success also loses the most efficiency, making model choice policy‑dependent.
- Runs tend to grind into timeouts or generate wrong solutions rather than stopping early, with a mix differing by model.

## Context
Coding agents are increasingly deployed in organizations with strict security controls such as scoped credentials and read‑only filesystems. Existing benchmarks evaluate them only in permissive sandboxes, leaving gaps about real‑world impact of hardening. This work fills that gap by measuring how policies affect solvability and efficiency across diverse models.

## Implications
For practitioners, the findings suggest that model selection should consider both security posture and operational cost, as trade‑offs are not linear. The released Boundary‑Bench plugin enables systematic comparison of agents under realistic constraints, guiding safer deployment decisions in enterprise environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02670v1)
