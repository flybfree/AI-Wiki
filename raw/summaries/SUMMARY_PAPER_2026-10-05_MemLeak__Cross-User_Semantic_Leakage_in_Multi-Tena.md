---
title: MemLeak: Cross-User Semantic Leakage in Multi-Tenant AI Agent Memory
url: http://arxiv.org/abs/2610.04195v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-03_01-16-05Z_MemLeak_Cross_UserSemanticLeakageinMulti_TenantAIA.md
generated_at: 2026-10-05 22:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates cross-user semantic leakage in multi-tenant AI agent memory systems, where shared vector stores enable one user's query to retrieve another user's semantically adjacent memories through standard cosine-similarity retrieval. The authors formalize this phenomenon as "cross-user admissibility failure" and demonstrate through six experiments and ablations that leakage rates reach 70–100% under pooled same-team retrieval, with adversarial memories achieving 90–100% top-k placement. They evaluate three architectural mitigations and find that only hard post-retrieval ownership gating consistently restores a clean baseline at a modest latency cost of approximately 1.4ms per query.

## Key Takeaways
- Non-adversarial, incidental cross-user leakage reaches 70–100% under pooled same-team retrieval, meaning that in typical enterprise deployments sharing a common embedding space, a user's ordinary query routinely surfaces memories belonging to other users without any adversarial manipulation or security exploit being required.
- Adversarially crafted memories achieve 90–100% top-k placement and produce score lifts of +0.416 to +0.511 under production-faithful dense retrieval using MiniLM-L6-v2, exceeding weaker keyword-based attacker baselines and demonstrating that the vulnerability is exploitable beyond incidental overlap.
- End-to-end response contamination reaches 5.00/5 under a production retrieval path and 4.67/5 with Claude Sonnet 4.5, and contaminated responses frequently score as helpful or more helpful than clean ones—a gap validated against human judgment—meaning users may not even recognize that their agent's output has been contaminated by another user's private memories.
- Among three tested architectural mitigations, only hard post-retrieval ownership gating consistently restores the clean baseline of 1.00/5 across two generation models, at a measured latency overhead of roughly 1.4ms per query, suggesting that soft or probabilistic filtering approaches are insufficient.

## Context
As personal AI agents proliferate in enterprise settings, multi-tenant architectures that share a single vector store for long-term memory have become a practical cost-saving design. This paper addresses a security and privacy gap that has received limited attention: the assumption that semantic similarity retrieval is inherently safe when multiple users' memories coexist in the same embedding space. By formalizing cross-user admissibility failure and testing it under both sparse TF-IDF and production-faithful dense retrieval, the work bridges the gap between theoretical retrieval security and the operational reality of deployed agent platforms.

## Implications
For practitioners deploying multi-tenant AI agents, this research demonstrates that even non-adversarial, everyday queries can leak private memories across users at rates approaching 100%, and that contaminated outputs may be perceived as equally or more helpful than clean ones, masking the privacy violation from end users. The finding that only hard ownership gating reliably prevents leakage—while softer mitigations fail—carries direct architectural guidance for platform engineers: per-query ownership checks at the retrieval layer are not optional but essential, and the associated latency cost of roughly 1.4ms is negligible relative to the privacy risk. This work should inform enterprise AI governance policies, vendor security certifications, and the design of compliance frameworks for agent-based systems handling sensitive user data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.04195v1)
