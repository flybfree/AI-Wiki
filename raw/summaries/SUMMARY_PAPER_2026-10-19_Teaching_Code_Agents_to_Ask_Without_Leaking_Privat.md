---
title: Teaching Code Agents to Ask Without Leaking Private Code
url: http://arxiv.org/abs/2610.24824v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_19-13-56Z_TeachingCodeAgentstoAskWithoutLeakingPrivateCode.md
generated_at: 2026-10-19 20:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Utility-Verified Abstraction (UVA), a training method that teaches local coding agents to formulate questions to stronger cloud models while minimizing disclosure of private code, identifiers, and file paths. The approach rewrites consultation questions from solved repair trajectories into role-and-type descriptions of private entities, retaining only the technical details an expert needs to provide a useful answer. The trained agent achieves a 37.6% issue-resolution rate on repository-level repair tasks compared to 25.3% when operating alone, while disclosing 3.7-fold fewer private entities and 1.4-fold less verbatim code than an untrained agent.

## Key Takeaways
- UVA addresses a fundamental tension in hybrid local-cloud coding agent architectures: host-side masking can hide recognized identifiers but leaves surrounding code and the agent's phrasing intact, while naive training to reduce disclosure risks suppressing consultation entirely or producing questions too vague for the expert to answer. UVA resolves this by teaching the agent to describe private entities through their functional role and type rather than their literal names or code snippets.
- The training pipeline constructs supervision from solved repair trajectories, rewriting each consultation question into an abstracted form and retaining the rewrite only under a dual criterion: the rewritten question must disclose strictly fewer private entities AND the repair must still succeed when replayed from the same execution state. This utility-verification step ensures that abstraction does not degrade answer quality.
- Across two benchmarks, the UVA-trained agent consults the cloud model more frequently than the untrained baseline, demonstrating that privacy-preserving questioning does not suppress the agent's willingness to seek help. The performance gain from 25.3% to 37.6% is attributed to the training as a whole rather than to consultation access alone, indicating that learning how to ask effectively is itself a critical capability.

## Context
Hybrid coding agent architectures that pair lightweight local models with powerful cloud LLMs are increasingly common in developer tooling and enterprise code assistants. However, the privacy and intellectual-property risks of sending proprietary source code, internal identifiers, and file paths to third-party cloud services have become a major adoption barrier, particularly in regulated industries and organizations with strict data-governance policies. This paper contributes to the growing body of work on privacy-preserving AI delegation by moving beyond static masking heuristics toward a learned, task-aware abstraction strategy that is validated against downstream utility rather than evaluated solely on disclosure metrics.

## Implications
For practitioners building enterprise coding assistants, UVA provides a concrete training recipe that can be applied to existing agent pipelines to reduce data-leakage risk without sacrificing repair performance, potentially enabling organizations to adopt cloud-assisted coding workflows under stricter compliance constraints. For the broader AI research community, the utility-verified rewriting approach offers a general template for teaching language models to communicate abstractly about private data while preserving task effectiveness, a pattern that could extend to domains beyond code repair such as medical or legal AI assistants where sensitive information must be referenced without being transmitted verbatim.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24824v1)
