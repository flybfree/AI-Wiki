---
title: Replication or Corroboration? An Axiomatic Framework for Evidential Dependence in Multi-Agent Debate
url: http://arxiv.org/abs/2610.36151v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_18-53-17Z_ReplicationorCorroboration_AnAxiomaticFrameworkfor.md
generated_at: 2026-10-27 20:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper formalizes the critical distinction between replication (agents repeating the same underlying evidence) and corroboration (agents independently producing separate evidential roots that support the same claim) in multi-agent debate settings. The authors develop an axiomatic framework called root replication invariance (RRI) that provably ensures a judge's verdict is unaffected by mere replication while remaining responsive to genuinely new evidence, and they introduce a mathematical construct called the lineage quotient to preserve this distinction across arbitrary wording, identity, and naming variations. Empirical audits over tens of thousands of argumentation profiles validate the predicted separation between replication and corroboration under a supplied partition.

## Key Takeaways
- The paper proves that root replication invariance (RRI) is exactly equivalent to threshold-uniform replication immunity, meaning that under RRI, replication-only deviations cannot alter a judge's verdict and positive-cost replication is strictly dominated. In contrast, occurrence-sensitive judges (which count report occurrences) and content-keyed judges (which merge matching content) both admit profitable deviations, demonstrating that naive counting or naive merging strategies are fundamentally flawed for evidential assessment.
- An information boundary theorem establishes that if a judge's observation interface cannot distinguish a replica from a matched fresh root, then no judge can simultaneously ignore the replica and respond strictly to the fresh root. This impossibility result motivates the introduction of the lineage quotient, which strips away wording, identity, occurrence multiplicity, and arbitrary root names while keeping distinct roots separate, and is proven to be the coarsest sufficient representation on orbit-connected domains for every deterministic judge invariant to replication and root-label renaming.
- The framework is lifted to quantitative bipolar argumentation frameworks (QBAFs), where the authors characterize strict fresh-root response, prove its propagation along sign-consistent paths under the DF-QuAD evaluation semantics, and derive a tight closed-form response modulus. Exhaustive audits spanning 28,224 direct-star profiles, 2,052 multi-layer DAGs, and 277 AVeriTeC-derived profiles with matched interventions empirically confirm the theoretical separation between replication and corroboration.

## Context
Multi-agent debate systems, where multiple LLM agents produce independent assessments that a judge aggregates, are increasingly deployed for fact-checking, scientific review, and decision support. A persistent vulnerability in these systems is that apparent agreement among agents may reflect shared training data, prompt leakage, or relayed sources rather than genuinely independent evidence. This paper addresses that vulnerability at a foundational level by providing a formal axiomatic treatment of evidential dependence, bridging social-choice-theoretic judgment games with argumentation-theoretic evaluation semantics. It sits at the intersection of formal epistemology, multi-agent systems, and quantitative argumentation theory, offering a principled alternative to heuristic deduplication or naive vote counting.

## Implications
For practitioners building multi-agent debate pipelines, the lineage quotient provides a concrete, implementable preprocessing step that strips superficial variation while preserving genuine evidential independence, enabling judges to weight corroboration correctly without inflating replicated claims. For the broader AI safety and reliability community, the impossibility boundary result clarifies a hard limit on what any judge can achieve given its observation interface, guiding the design of agent architectures that expose distinct evidential roots rather than mere textual outputs. The closed-form response modulus under QBAF semantics also offers a computable diagnostic for auditing whether a deployed judge is truly replication-immune or merely appearing so due to interface limitations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36151v1)
