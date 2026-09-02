---
title: AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes
url: http://arxiv.org/abs/2609.00052v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-30_08-22-12Z_AgentProv_AuditingAgenticLLMAPIProvidersviaTool_us.md
generated_at: 2026-09-01 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces AgentProv, an action‑based audit method for agentic LLM APIs that verifies the identity of the underlying model by analyzing categorical tool‑call distributions. The authors demonstrate that AgentProv correctly identifies every substituted checkpoint (100% detection) while keeping false‑positive rates low even when system prompts are injected.

## Key Takeaways
- AgentProv uses an MMD permutation test on the distribution of categorical tool calls to fingerprint a model, providing a reliable identity audit. - The method achieves 100% detection across 630 checkpoint pairs, outperforming text‑based tests that suffer from serving‑stack changes. - False‑positive rates drop to 7% under system‑prompt injection, compared with 67% for MET and 53% for RUT.

## Context
Agentic LLM APIs increasingly rely on tool use rather than textual outputs, making traditional audits based on text fragile. Providers may silently replace models or inject prompts, which can evade detection methods that depend on visible text. AgentProv addresses this by focusing on the invariant categorical actions exposed by the serving stack.

## Implications
For developers and auditors, AgentProv offers a robust way to verify model provenance without relying on potentially altered output text. The low false‑positive rate ensures trustworthy verification even in adversarial prompt scenarios, encouraging more transparent and accountable AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00052v1)
