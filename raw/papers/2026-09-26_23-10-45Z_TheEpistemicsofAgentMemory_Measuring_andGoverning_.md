---
title: The Epistemics of Agent Memory: Measuring, and Governing, the Consolidation Decision in Long-Horizon LLM Agents
published: 2026-09-26T23:10:45Z
authors: Sasank Annapureddy, Anjaneya Prasad Thamatani
url: http://arxiv.org/abs/2609.33013v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Epistemics of Agent Memory: Measuring, and Governing, the Consolidation Decision in Long-Horizon LLM Agents

## Abstract
Long-horizon LLM agents must convert accumulated experience into durable memory, deciding what to keep, compress, abstract into reusable skills and rules, or forget. We report a four-phase research program on this consolidation problem whose central finding is a shift in what is measured: from how much an agent remembers, to whether its consolidation decisions are any good, to whether those decisions can be trusted.   Phase 1 learns episodic boundaries from agent traces by downstream utility; an honest near-miss (oracle correlation 0.691 vs a 0.70 bar) whose lasting output is a three-gate anti-leakage protocol. Phase 2 learns when to promote experience and to which abstraction level under a token budget, achieving a verified +22.7% task-success improvement with 7x compression, but exposing a degenerate-forgetting failure and a distribution-shift failure mode we name lambda-prevalence coupling. Phase 3 introduces ConsolidationBench, an oracle-by-construction benchmark that scores consolidation decisions against a known optimum on three non-circular axes; production retrieval systems retain information yet score zero on cross-level transfer. Phase 4 introduces governed consolidation: the decision wrapped in poison-resistance, reversibility, and auditability guarantees with a quality gate. Governance is statistically distinct from the quality score ($r^2 = 0.43$; partial $r = 0.27$; identical-quality policies differ threefold in governance), so the contribution survives independently of the metric's external validity. On that question we report a resolved negative: after a graded-reuse redesign removed a structural ceiling, a two-benchmark study with 2,532 real answer cells finds the quality score does not predict real transfer accuracy (pooled Spearman $ρ= -0.24$, n = 12, CI spanning zero). An adversarial self-critique pass cleared the final claim set with zero surviving overclaims.

## Metadata
- **Published**: 2026-09-26T23:10:45Z
- **Authors**: Sasank Annapureddy, Anjaneya Prasad Thamatani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33013v1)