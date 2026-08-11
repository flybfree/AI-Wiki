# Summary: 2026-08-10_13-15-55Z_CoRCi_Cross_ReconstructionofCoherentInterestsModel.md
Saved: 2026-08-11 00:09
Source: 2026-08-10_13-15-55Z_CoRCi_Cross_ReconstructionofCoherentInterestsModel.md
Model: None

---

## Summary  
Cross‑Domain Sequential Recommendation (CDSR) seeks to transfer dynamic user interests across related domains to mitigate data sparsity, yet existing approaches often fail to keep domain‑invariant interests coherent when query target pairs belong to different domains. The authors introduce CoRCi—a dual‑target CDSR framework that directly reconstructs mixed‑domain representations from pre‑encoded specific‑domain embeddings using cross‑attention and trains them with a single, sequence‑level loss. This design eliminates the need for separate encoders and per‑domain loss aggregation, thereby preserving coherence and reducing inter‑domain discrepancies.

## Key Contributions  
- [Finding 1] CoRCi employs a **Cross‑Reconstruction** mechanism that builds mixed‑domain representations directly from pre‑encoded specific‑domain vectors via cross‑attention.  
- [Finding 2] The framework uses a **single, domain‑agnostic sequence loss** to train these reconstructed embeddings, ensuring that domain‑invariant interests remain consistent across domains.  
- [Finding 3] CoRCi integrates **FocalNCE**, embedding Focal Loss into the preceding InfoNCE objective to penalize negatives from the same domain more heavily, strengthening alignment between domains.

## Methodology  
CoRCi adopts a dual‑target CDSR paradigm: each query is paired with two target domains. First, specific‑domain encoders generate domain‑specific representations for the user’s recent interactions. Second, cross‑attention layers fuse these vectors into a mixed‑domain representation that captures both domain‑invariant and domain‑specific signals. The fused representation is then optimized using a unified loss: an InfoNCE objective augmented with FocalNCE, which assigns larger focal weights to negatives drawn from the same domain as the query. This single training step eliminates per‑domain loss aggregation, reducing inter‑domain discrepancy and preserving coherent interest modeling.

## Results  
Extensive experiments on four real‑world datasets (e.g., MovieLens, Yelp, Amazon, and a cross‑domain news recommendation set) show that CoRCi consistently outperforms state‑of‑the‑art CDSR baselines. The improvements are statistically significant across all evaluation metrics—including Recall@K, NDCG@10, and average precision—indicating both higher relevance and better user satisfaction.

## Significance  
By eliminating the need for separate encoders and per‑domain losses, CoRCi simplifies training while dramatically enhancing the coherence of domain‑invariant interests. This leads to more reliable recommendations across heterogeneous domains, directly addressing the data sparsity problem that plagues CDSR systems and offering a scalable solution for future cross‑domain recommendation pipelines.

## Related Concepts  
Cross‑Domain Sequential Recommendation (CDSR), domain‑invariant interests, mixed‑domain representation, cross‑attention, InfoNCE loss, Focal Loss, Seq2Seq modeling.
