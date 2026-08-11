# Summary: 2026-08-02_10-57-53Z_UniHEAR_UnifiedHeterogeneous_SourceAttentiveRetrie.md
Saved: 2026-08-04 00:02
Source: 2026-08-02_10-57-53Z_UniHEAR_UnifiedHeterogeneous_SourceAttentiveRetrie.md
Model: None

---

## Summary  
Knowledge‑Based Visual Question Answering (KB‑VQA) must retrieve entity knowledge from multiple heterogeneous sources, yet current retrieval systems are limited by a single‑source bottleneck and blind reranking that ignores source priors. UniHEAR proposes a unified lightweight framework that jointly learns to extract coarse descriptors for candidate entities and to condition modality attention on these descriptors while preserving source information. The approach integrates contrastive learning with an auxiliary loss that enforces modality preservation, enabling both entity‑level and section‑level retrieval within one model. Experiments show substantial gains over state‑of‑the‑art baselines on E‑VQA and InfoSeek.  

## Semantic links
- [[concepts/papers/2026-08-01_13-21-55Z_Select_And_Extract_ALightweightPluginforRet_summary.md|Summary: 2026-08-01_13-21-55Z_Select_And_Extract_ALightweightPluginforRetrieval_.md]] — 4 title terms overlap; 4 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-22_06-50-53Z_Hypothesis_and_RefinementLearningofOrganicS_summary.md|Summary: 2026-07-22_06-50-53Z_Hypothesis_and_RefinementLearningofOrganicStructur.md]] — 4 title terms overlap; 3 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] UniHEAR introduces Retrieval‑Guided Attentive Modality Gating, which conditions attention weights on a Coarse Retrieval Descriptor to capture source‑specific retrieval priors.  
- [Finding 2] The framework employs Entropy‑Weighted Source Fusion of coarse retrieval priors to balance information from different heterogeneous sources without redundancy.  
- [Finding 3] A hybrid training strategy combines contrastive learning with a modality‑preserving auxiliary loss, unifying entity‑level and section‑level retrieval in a single model.  

## Methodology  
UniHEAR first builds a lightweight retriever that generates a Coarse Retrieval Descriptor for each candidate entity, encoding both content and source metadata. This descriptor is used to compute modality attention weights via the Retrieval‑Guided Attentive Modality Gating mechanism. The Entropy‑Weighted Source Fusion then aggregates these descriptors, weighting them according to their entropy to avoid over‑reliance on any single source. During training, contrastive loss pulls together positive entity‑section pairs while pushing apart negatives, and an auxiliary loss ensures that the model does not discard source information. This joint learning simultaneously optimizes retrieval relevance and source diversity.  

## Results  
On E‑VQA, UniHEAR improves Recall@1 by 6.7 points over the strongest baselines; on InfoSeek it gains 1.2 points. The improvement is achieved with a reranking architecture that remains lightweight compared to previous pointwise models. Ablation studies confirm that both the attention gating and source‑fusion components are essential for these gains, while the hybrid loss contributes significantly to model stability.  

## Significance  
UniHEAR addresses two persistent weaknesses in KB‑VQA: single‑source retrieval and blind reranking, which degrade answer quality and efficiency. By unifying heterogeneous sources through attention gating and entropy‑weighted fusion, the method enables more accurate, diverse, and computationally efficient knowledge integration. This work sets a new benchmark for source‑aware retrieval in visual question answering.  

## Related Concepts  
- Heterogeneous‑source retrieval  
- Attentive modality gating  
- Coarse retrieval descriptor  
- Entropy‑weighted fusion  
- Contrastive learning  
- Modality‑preserving auxiliary loss
