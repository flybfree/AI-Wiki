---
title: Do Coding Agents Understand Least-Privilege Authorization?
url: http://arxiv.org/abs/2605.14859v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-14_14-05-58Z_DoCodingAgentsUnderstandLeast_PrivilegeAuthorizati.md
generated_at: 2026-06-11 10:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether coding agents can infer least‑privilege authorization when operating in terminal environments, introducing Permission‑Boundary Inference and the AuthBench benchmark. It finds that frontier models often grant unnecessary or missing permissions, leading to a mismatch between required and granted accesses. The proposed Sufficiency‑Tightness Decomposition improves task success by up to 15.8% for tight‑bias models while reducing attacks.

## Key Takeaways
- Models generate authorization policies that are either overly permissive or too restrictive, causing both security gaps and execution failures.
- Inference time does not fix the problem; instead each model converges on a specific failure pattern of its own kind.
- The Sufficiency‑Tightness Decomposition separates coverage generation from sensitivity auditing to achieve better outcomes.

## Context
Current AI agents interact with code repositories and user files, making fine‑grained permission control essential for safe operation. This work addresses the challenge of aligning model policy generation with real‑world security constraints in a realistic terminal setting.

## Implications
For practitioners deploying coding assistants, this research highlights that automated policies must be both comprehensive and minimal to avoid exposing sensitive data or enabling attacks. The proposed decomposition offers a practical path toward more secure AI agents without sacrificing task completion.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.14859v1)
