---
title: Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales
published: 2026-07-28T07:16:12Z
authors: Genliang Zhu, Chu Wang
url: http://arxiv.org/abs/2607.25364v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales

## Abstract
Tool-using agents expose structured calls but commonly attach free-form rationales. Such rationales are neither authorization nor reliable introspection. We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts. EBTE cannot widen baseline authority: conflicts deny, incomplete or uncertain claims review, and only matching claims remain eligible for governed execution. We formalize this composition under explicit mediation and trusted-fact assumptions and implement a versioned reference profile with minimized audit packets. Across 136 authored conformance scenarios, the full profile matches all specified dispositions, admits none of 96 designated hard contradictions, and passes 232 metamorphic checks; these results validate the included profile rather than population performance. A draft-only reference integration forwards none of 48 authored hard cases under EBTE while preserving all 16 soft-review and 4 aligned draft paths. In a frozen 2026-07-12 exploratory 224-attempt hosted-model record, the historical generation/runner agreement counts are 71/96, 66/96, and 19/32; a separately labeled zero-call post-hoc revalidation of the preserved minimized claims under the current pipeline yields 70/96, 65/96, and 17/32. In an AgentDojo-derived semantic check, existing high-risk controls already make all 12 attack proposals non-allow; EBTE additionally resolves them as deny. These results support the feasibility and diagnostic value of server-checked action claims, not rationale faithfulness, human-review benefit, representative attack resistance, or production safety.

## Metadata
- **Published**: 2026-07-28T07:16:12Z
- **Authors**: Genliang Zhu, Chu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25364v1)