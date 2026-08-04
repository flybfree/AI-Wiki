# Summary: 2026-08-02_17-11-09Z_KoVRE_TraininganEfficientEmbeddingModelforKoreanVi.md
Saved: 2026-08-04 00:17
Source: 2026-08-02_17-11-09Z_KoVRE_TraininganEfficientEmbeddingModelforKoreanVi.md
Model: None

---

## Summary  
KoVRE is a single‑vector retrieval model designed specifically for Korean visual document queries, aiming to preserve both text and image information that traditional VDR pipelines often discard. The authors train KoVRE on a large bilingual dataset of 708 729 query‑page pairs using positive‑aware hard‑negative mining, which is complemented by analyses of data composition and knowledge distillation. Their model, a 2B‑parameter version, achieves state‑of‑the‑art performance across Korean visual document retrieval benchmarks. The work shows that targeted bilingual supervision can produce highly effective results without resorting to massive backbones or multi‑vector representations.

## Key Contributions  
- [Finding 1] KoVRE attains the best scores on Korean visual document retrieval benchmarks while using a single‑vector representation.  
- [Finding 2] Combining bilingual supervision with positive‑aware hard‑negative mining yields superior training efficiency compared to large monolingual models.  
- [Finding 3] The 2B KoVRE model outperforms both its larger single‑vector counterpart and a strong multi‑vector baseline.

## Methodology  
The authors approached the problem by constructing a comprehensive training recipe that includes data preprocessing, positive‑aware hard‑negative mining, and controlled experiments on data composition, hard‑negative treatment, and reranker‑based knowledge distillation. They trained KoVRE on 708 729 Korean/English query‑page pairs, evaluated the impact of each component, and iteratively refined the model architecture.

## Results  
The 2B‑parameter KoVRE model improves over its base backbone and achieves higher recall@k than both an 8B single‑vector version and a multi‑vector baseline on all benchmark datasets. These gains are consistent across diverse document domains, confirming the effectiveness of the training strategy.

## Significance  
This research demonstrates that Korean visual document retrieval can be solved efficiently with targeted bilingual supervision and carefully designed training methods, alleviating the need for costly English‑centric resources or massive multi‑vector storage.

## Related Concepts  
Visual Document Retrieval (VDR), single‑vector embeddings, bilingual supervision, hard‑negative mining, knowledge distillation, retrieval benchmarks.
