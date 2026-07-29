---
title: Entangled by Design: Spurious Intra-Variable Signal Routing in Tabular In-Context Learners
url: http://arxiv.org/abs/2607.25532v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_10-17-59Z_EntangledbyDesign_SpuriousIntra_VariableSignalRout.md
generated_at: 2026-07-28 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper identifies a problem where tabular in‑context learners misinterpret features that contain both the true health signal and a spurious artefact, leading to silent routing errors when deployed elsewhere. It shows that even with large contexts, linear models cannot separate these signals, and that more expressive TabPFN models amplify this issue. The authors provide a closed‑form ratio of spurious to causal routing and demonstrate how lightweight mitigations can dramatically reduce the error.

## Key Takeaways
- The in‑context learner routes predictions through the artefact S rather than the true signal C, producing a CSR proportional to ρ_S/ρ_C that is high even with large contexts.  
- Larger context sizes increase commitment to the dominant spurious signal, raising CSR by up to 1.74× and worsening performance in the high‑entanglement regime.  
- S‑swap augmentation reduces spurious routing by 74% for linear ICL and 98.8% for TabPFN while boosting causal sensitivity eightfold.

## Context
The work highlights a fundamental limitation of current tabular in‑context models: they treat feature embeddings as opaque composites, making them vulnerable to systematic artefacts that are not captured by the data alone. This issue is especially relevant for medical and clinical AI where equipment noise can masquerade as patient pathology.

## Implications
For practitioners deploying predictive models across different facilities, this research warns against assuming model robustness without environmental awareness. Mitigation strategies like environment‑stratified context construction can improve reliability and reduce costly failures in real‑world settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25532v1)
