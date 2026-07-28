---
title: Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool Calls
url: http://arxiv.org/abs/2607.24343v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_12-21-18Z_BeyondAggregateRisk_Role_StratifiedConformalRiskCo.md
generated_at: 2026-07-27 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes role‑stratified conformal risk control as a calibration layer that separates the risk assessment of individual semantic arguments within structured tool calls rather than treating them as a single aggregate action. The method demonstrates that per‑role guarantees can be achieved with tighter budgeting, and empirical results show improved utility compared to traditional approaches across multiple language models.

## Key Takeaways
- Role‑stratified calibration uses separate thresholds for each argument role, allowing rare high‑risk fields such as credentials to be protected without inflating the risk of benign arguments.  
- The method replaces aggregate‑only certification with a finite‑sample guarantee per role, pooling only when a role is under‑represented, which reduces the “price of coarseness.”  
- Experiments on AgentDojo and InjecAgent show that this approach yields more consistent budget compliance across model variations, attack types, detector noise, drift, unseen tool suites, and adaptive attacks.

## Context
Current risk mitigation for AI agents focuses on the whole call, which can hide dangerous inputs in low‑risk fields. As LLM tools become more prevalent, ensuring safety at the level of individual semantic arguments is essential to prevent unintended high‑impact failures that could affect users or systems.

## Implications
Practitioners should adopt role‑level certification when deploying tool‑calling agents to balance safety and performance, especially in regulated environments where specific data types must be protected. This shift can lead to more reliable deployments and reduced liability risks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24343v1)
