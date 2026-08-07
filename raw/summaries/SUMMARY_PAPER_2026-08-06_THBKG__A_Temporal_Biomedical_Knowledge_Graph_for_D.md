---
title: THBKG: A Temporal Biomedical Knowledge Graph for Decision-Aligned Clinical Advancement Prediction
url: http://arxiv.org/abs/2608.05982v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_12-59-05Z_THBKG_ATemporalBiomedicalKnowledgeGraphforDecision.md
generated_at: 2026-08-06 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces THBKG, a temporal biomedical knowledge graph that records when evidence linking therapeutic targets to diseases changes over time. It creates a decision-aligned benchmark predicting whether Phase II programs advance based on pre-decision evidence and shows that graph propagation outperforms direct‑evidence models by 4.3–4.5 at the top ten pairs per area, especially for pairs lacking direct links.

## Key Takeaways
- THBKG stores 110,396 entities and 11.1 million edges across nineteen relation types, each edge annotated with the year its evidence was updated, enabling a precise historical profile of target‑disease links at any decision point.
- The model’s graph propagation outperforms direct‑evidence reference models by a relative success of 4.3–4.5 on the top ten pairs per therapeutic area, recovering signal for the majority of pairs that have no direct evidence at their decision time.
- A path‑based explainer is applied to the decision‑time subgraph to decompose each prediction into the underlying evidence landscape, providing explainable insights.

## Context
This work addresses a longstanding challenge in clinical trial design where poor target‑disease linkage causes many Phase II failures. By integrating temporal provenance of biomedical knowledge, THBKG enables AI systems to learn from historical evidence evolution rather than static snapshots, aligning predictions with the evidence available at decision time.

## Implications
For researchers and sponsors, THBKG offers a reusable substrate for retrospective validation of therapeutic hypotheses, improving trial planning accuracy. The graph’s explainable path‑based approach also supports transparent model decisions, fostering trust in AI‑driven clinical decision support tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05982v1)
