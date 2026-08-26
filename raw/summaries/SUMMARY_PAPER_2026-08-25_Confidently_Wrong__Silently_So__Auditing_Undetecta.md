---
title: Confidently Wrong, Silently So: Auditing Undetectable Failures of a Deployed On-Device Language Model
url: http://arxiv.org/abs/2608.23663v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_16-55-09Z_ConfidentlyWrong_SilentlySo_AuditingUndetectableFa.md
generated_at: 2026-08-25 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits on‑device language models to see if users can detect when the model is wrong. It shows that guardrails misbehave in opposite ways across tasks and confidence scores are uninformative, making failures hard to spot at inference time.

## Key Takeaways
- The model confabulates on 69 % of false premises while refusing only 18 % of benign inputs, revealing a task‑asymmetric miscalibration. - Its self‑reported confidence is low (AUROC 0.47) and non‑discriminative, so it cannot reliably flag errors. - A classifier on user‑visible features separates correct from wrong outputs at only AUROC 0.55, confirming surface indistinguishability.

## Context
Current AI deployments rely heavily on on‑device models that lack server‑side moderation, raising concerns about hidden failures. This work addresses the need for transparent reliability checks without requiring access to the model’s internals or additional infrastructure.

## Implications
For developers, the audit protocol provides a low‑cost way to verify model trustworthiness before release. For users, it highlights that current confidence signals are insufficient, urging better guardrails and consistency across tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23663v1)
