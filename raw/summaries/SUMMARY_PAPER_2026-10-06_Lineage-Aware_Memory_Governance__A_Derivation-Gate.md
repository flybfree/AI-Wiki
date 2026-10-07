---
title: Lineage-Aware Memory Governance: A Derivation-Gated Framework for Privacy-Preserving Column-Level Access Control in Enterprise AI Agents
url: http://arxiv.org/abs/2610.07258v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_18-56-56Z_Lineage_AwareMemoryGovernance_ADerivation_GatedFra.md
generated_at: 2026-10-06 21:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Lineage-Aware Memory Governance, a framework for privacy-preserving column-level access control in enterprise AI agents that share a memory store. It proposes the Analytical Memory Unit, a memory schema that records the full derivation lineage of cached results and gates retrieval so that a requester can only access results derived from columns they are authorized to see. The authors argue that lineage-gated retrieval can prevent leakage through legitimately computed insights and detect conflicting departmental definitions of same-named KPIs.

## Key Takeaways
- Existing agent-memory systems often gate retrieval by content, ownership, or role, but not by derivation lineage, which allows sensitive information to leak through cached results that embed forbidden columns even when the requester could not directly access those columns. The paper addresses this gap by attaching a full derivation graph to every cached result and enforcing access only when the requester is authorized for every column touched by that derivation.
- The framework provides a conditional design guarantee rather than an empirical claim: if lineage recording is complete, the retrieval policy blocks access to results derived from sensitive columns outside the requester’s permissions, with worst-case overhead of O(n). However, the authors note that measured leakage elimination required 75 to 90 percent lineage completeness, so 90 percent is treated as a conservative deployment target.
- Across six experiments, lineage-gated retrieval removes the 18.8 to 25.5 percent cross-department leakage seen in naive content-gated memory while preserving 81.5 to 82.6 percent of memory reuse and adding only 13.8 microseconds of worst-case overhead. A real-agent proof-of-concept using LLM-generated SQL showed zero leaks over nine round-trips and automatically caught two conflicting KPI definitions, though this is presented as a feasibility demonstration rather than proof of production readiness.

## Context
Enterprise AI agents increasingly rely on shared memory stores to reuse prior computations, retrieve cached insights, and coordinate across departments. This improves efficiency but creates governance risks when cached results combine sensitive data or when different teams compute the same metric using conflicting logic. The paper matters because it shifts access control from simple content or role checks to derivation-aware governance, which is necessary for column-level privacy and trustworthy enterprise analytics.

## Implications
For practitioners, this approach offers a practical governance layer for shared agent memory that complements source-layer access control and helps organizations manage privacy risks in AI-assisted analytics. It is especially relevant for regulated environments where AI agents must respect data permissions, avoid unauthorized derived insights, and support compliance requirements such as those under the EU AI Act. The work suggests that lineage recording and retrieval gating can be a feasible foundation for safer, auditable, and more accountable enterprise AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07258v1)
