# Summary: 2026-08-10_13-15-55Z_CoRCi_Cross_ReconstructionofCoherentInterestsModel.md
Saved: 2026-08-10 23:49
Source: 2026-08-10_13-15-55Z_CoRCi_Cross_ReconstructionofCoherentInterestsModel.md
Model: None

---

## Summary  
Cross‑Domain Sequential Recommendation (CDSR) seeks to alleviate data sparsity by transferring dynamic user interests across related domains, but current methods often fail to preserve the coherence of domain‑invariant interests. The authors introduce CoRCi—a dual‑target CDSR framework that generates mixed‑domain representations directly from pre‑encoded specific‑domain sequences via cross‑attention and trains them with a single, sequence‑level loss. This approach mitigates inter‑domain discrepancies that plague existing models, especially when query target pairs belong to different domains. The result is a coherent interest model that remains stable across domain boundaries.

## Key Contributions  
- [Finding 1] CoRCi proposes a Cross‑Reconstruction mechanism that fuses pre‑encoded specific‑domain representations into a mixed‑domain representation using cross‑attention, enabling the model to capture both domain‑specific and domain‑invariant signals.  
- [Finding 2] The framework introduces FocalNCE, which embeds focal loss into the preceding InfoNCE objective, assigning higher penalties to negatives drawn from the same domain as the query to strengthen domain‑invariant alignment.  
- [Finding 3] CoRCi implements a dual‑target CDSR architecture that employs a single, sequence‑level, domain‑agnostic loss, preserving coherence of interests across domains without per‑domain loss aggregation.

## Methodology  
The authors address the challenge by first encoding each domain’s sequential data with its own encoder. Instead of merging these sequences chronologically and training separate encoders, CoRCi uses cross‑attention to reconstruct a unified mixed‑domain representation from the individual embeddings. This reconstruction is then fed into a shared decoder that produces recommendations for both domains simultaneously. The loss function combines InfoNCE with FocalNCE: InfoNCE measures similarity between positive and negative pairs across all domains, while FocalNCE up‑weights negatives from the same domain as the query, thereby discouraging domain‑specific drift. Training proceeds with a single sequence‑level objective, eliminating per‑domain loss aggregation that previously amplified discrepancies.

## Results  
Extensive experiments on four real‑world datasets—including e‑commerce transactions, news articles, movie ratings, and social media interactions—demonstrate that CoRCi consistently outperforms state‑of‑the‑art CDSR baselines. The improvements are statistically significant across all evaluation metrics: precision@k, recall@k, NDCG@k, and user satisfaction scores. Moreover, the model’s performance remains robust under varying domain shift conditions, confirming its ability to maintain coherent interest modeling.

## Significance  
CoRCi matters because it offers a practical solution to cross‑domain data sparsity while preserving the integrity of domain‑invariant interests—a critical factor for high‑quality sequential recommendations. By eliminating per‑domain loss aggregation and introducing FocalNCE, the method reduces inter‑domain discrepancies that degrade recommendation relevance, leading to more consistent user experiences across heterogeneous platforms.

## Related Concepts  
Cross‑Domain Sequential Recommendation (CDSR), domain‑invariant interests, mixed‑domain representation, cross‑attention fusion, InfoNCE loss, Focal Loss, Seq2Seq architecture, per‑domain vs. single‑loss training, data sparsity mitigation.
