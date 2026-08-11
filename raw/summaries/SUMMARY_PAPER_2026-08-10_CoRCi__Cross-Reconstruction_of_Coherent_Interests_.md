---
title: CoRCi: Cross-Reconstruction of Coherent Interests Modeling in Cross-Domain Sequential Recommendation
url: http://arxiv.org/abs/2608.09580v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_13-15-55Z_CoRCi_Cross_ReconstructionofCoherentInterestsModel.md
generated_at: 2026-08-10 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
CoRCi introduces a dual‑target Cross‑Domain Sequential Recommendation framework that directly generates mixed‑domain representations from pre‑encoded specific‑domain sequences using cross‑attention, then trains them with a single sequence‑level loss to keep domain‑invariant interests coherent. Experiments on four real‑world datasets show CoRCi consistently beats state‑of‑the‑art CDSR methods and achieves statistically significant improvements.

## Key Takeaways
- Cross‑Reconstruction creates mixed‑domain representations directly from pre‑encoded specific‑domain sequences via cross‑attention.
- A single, sequence‑level, domain‑agnostic loss is used to preserve the coherence of domain‑invariant interests across domains.
- FocalNCE embeds Focal Loss into the preceding InfoNCE objective, giving higher penalties to negatives from the same domain as the query.

## Context
Cross‑Domain Sequential Recommendation tackles data sparsity by transferring user interests between related domains. Existing approaches often merge sequences chronologically and use separate encoders with per‑domain losses, which can amplify inter‑domain discrepancies. CoRCi’s cross‑reconstruction method offers a more unified way to align domain‑specific knowledge.

## Implications
For practitioners, CoRCi provides a reliable recommendation pipeline when users move between domains, reducing the risk of incoherent or contradictory suggestions. The approach improves personalization accuracy and can be applied across e‑commerce, social media, and content platforms where cross‑domain interactions are common.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09580v1)
