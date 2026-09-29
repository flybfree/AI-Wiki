---
title: When Valid Tool Calls Change Meaning: Formation-Consistent Dispatch for LLM Agents
published: 2026-09-28T13:04:04Z
authors: Geonwoo Kim, Brent ByungHoon Kang
url: http://arxiv.org/abs/2609.35088v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Valid Tool Calls Change Meaning: Formation-Consistent Dispatch for LLM Agents

## Abstract
Tool-enabled agents form calls from model-visible interfaces, while hosts later select their implementation. Standard dispatch omits the descriptor-handler relation. An unchanged and schema-valid call can therefore acquire a different security effect during rollout, reconnect, or delayed approval. We call this failure schema-epoch drift. We present formation-consistent dispatch (FCD), which connects implementation analysis to execution authority. Reviewed profiles produce provenance-bound over-approximations of declared in-scope effects from official source. Under a closed-target approval policy, a verifier applies each formed call to a summary and captures a successor only when its effects fit the call's security contract. Atomic admission and a final-hop fence preserve this decision to the effect. The exact source retains priority, and the captured successor becomes eligible only after source retirement. Stock releases and deployment changes reproduced the failure. Four profiles covered 32 official releases: 29 required no release-specific change and three escalated. A frozen 16-release expansion matched a separate source oracle. In a preregistered stock comparison, FCD completed all three pending calls whose effect remained private and blocked all three whose omission became public. Exact pinning and release-wide denial stopped all six calls, while release-wide approval completed all six but produced three public effects. A separate lifecycle experiment carried a formation-captured certificate across source retirement. The same safe certificate installed later governed new formations without expanding the pending call's authority.

## Metadata
- **Published**: 2026-09-28T13:04:04Z
- **Authors**: Geonwoo Kim, Brent ByungHoon Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35088v1)