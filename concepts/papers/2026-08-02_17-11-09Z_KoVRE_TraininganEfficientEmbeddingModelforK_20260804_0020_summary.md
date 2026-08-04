# Summary: 2026-08-02_17-11-09Z_KoVRE_TraininganEfficientEmbeddingModelforKoreanVi.md
Saved: 2026-08-04 00:20
Source: 2026-08-02_17-11-09Z_KoVRE_TraininganEfficientEmbeddingModelforKoreanVi.md
Model: None

---

## Summary  
The paper introduces KoVRE, a single‑vector embedding model for Korean visual document retrieval that achieves high performance without large backbones or multi‑vector representations. It trains on 708 k bilingual query‑page pairs using positive‑aware hard‑negative mining and analyses training strategies to improve retrieval across diverse domains.  

## Key Contributions  
- KoVRE demonstrates that a compact single‑vector model can outperform larger 2B and 8B backbones on Korean VDR benchmarks.  
- The study identifies effective bilingual supervision and hard‑negative mining as key factors enabling strong performance.  
- A comprehensive training recipe, including controlled analyses of data composition and knowledge distillation, is provided.  

## Methodology  
KoVRE was built by fine‑tuning a lightweight backbone on a large corpus of Korean visual documents paired with English queries. The authors employ positive‑aware hard‑negative mining to select informative negatives, conduct systematic experiments varying data composition, apply reranker‑based knowledge distillation, and evaluate retrieval quality using standard VDR metrics.  

## Results  
On multiple Korean visual document retrieval benchmarks, KoVRE’s 2B single‑vector model surpasses the base backbone, its 8B counterpart, and a strong multi‑vector baseline. The improvements are consistent across diverse document types, indicating robustness of the training recipe.  

## Significance  
This work shows that targeted bilingual supervision and careful negative mining can yield high‑quality embeddings for Korean documents without costly scaling or complex vector representations, offering an efficient alternative to massive multilingual VDR systems.  

## Related Concepts  
- Visual Document Retrieval (VDR)  
- Single‑vector retrieval  
- Hard‑negative mining  
- Knowledge distillation via rerankers  
- Bilingual supervision  
- Compact backbone models
