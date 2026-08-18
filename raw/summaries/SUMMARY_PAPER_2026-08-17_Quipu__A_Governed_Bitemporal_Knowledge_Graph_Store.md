---
title: Quipu: A Governed Bitemporal Knowledge Graph Store
url: http://arxiv.org/abs/2608.16813v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_17-04-29Z_Quipu_AGovernedBitemporalKnowledgeGraphStore.md
generated_at: 2026-08-17 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Quipu, a governed bitemporal knowledge graph store that addresses the limitations of traditional stores by enforcing strict governance rules. It demonstrates that gating writes and treating facts as bitemporal reduces defects in automated lifecycle systems. The study shows that gated stores end with zero of six planted defects versus six in ungated ones.

## Key Takeaways
- The store requires a gate where predicates evaluate pending post-state before any fact enters, preventing invalid entries.
- Trust labels, verdicts, rules, and the audit specification are all bitemporal facts that govern data admission.
- Composition of named graphs follows a lattice invariant that never widens trust or authority.

## Context
Traditional knowledge graph stores lack formal governance, leading to drift between written and stored facts. Agent workloads amplify this problem as writes accumulate without validation. This work provides a formal framework for auditable AI systems. Such formalism aligns with emerging standards for AI data integrity.

## Implications
Practitioners can embed governance directly into data pipelines, reducing misreporting in AI reasoning tasks. The approach also clarifies accountability by making audit queries verifiable within the store itself. Future systems can rely on these contracts to ensure compliance without external dashboards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16813v1)
