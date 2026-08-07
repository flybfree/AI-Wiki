# Summary: 2026-08-06_10-38-13Z_MappingSimilaritySpacesacrossEmbeddingModelswithSy.md
Saved: 2026-08-06 22:12
Source: 2026-08-06_10-38-13Z_MappingSimilaritySpacesacrossEmbeddingModelswithSy.md
Model: None

---

## Summary  
The paper addresses the challenge of comparing similarity scores from different embedding models in retrieval‑augmented generation systems, where scores are not directly comparable due to model‑specific geometric properties. It proposes Synthetic Query Probing, a reference‑free method that generates synthetic query‑chunk pairs to analyze cross‑model score distributions and learn mappings between them. The study evaluates linear, isotonic, and quantile mapping functions on multiple embedding configurations and demonstrates that while rankings often align, absolute scores are systematically distorted across models. Learned mappings, especially via isotonic regression, improve threshold portability and model migration.

## Key Contributions  
- [Finding 1] The authors demonstrate that similarity score spaces of different embedding models can be related through learned mapping functions rather than direct embedding alignment.  
- [Finding 2] Synthetic Query Probing enables large‑scale, reference‑free analysis of cross‑model similarity behavior by generating controlled query‑chunk pairs from a corpus.  
- [Finding 3] Isotonic regression yields the most effective score conversion function, significantly improving threshold portability across models.

## Methodology  
The authors approach the problem by first constructing synthetic queries using documents in their proprietary and SciFact corpora. For each query they retrieve the top‑k chunks as potential answers, forming a set of (query, chunk) pairs that are guaranteed to be relevant or irrelevant based on content similarity. They then compute cosine similarity scores for both the query embedding and the chunk embedding across multiple embedding models (e.g., BERT, Sentence‑BERT). The goal is to learn functions fᵢ(x) that map a score x from model i into a common reference space while preserving relative ordering. Mapping candidates include linear scaling, isotonic regression, and quantile transformation. The learned mappings are evaluated by applying them to scores from one model and comparing the transformed values with those of another model.

## Results  
Experiments show that across all models, the ranking order of retrieved chunks remains consistent, indicating that relative similarity is preserved even when absolute scores differ. However, the mean absolute score differs by up to 30 % between models, causing threshold misalignment. When isotonic regression mapping is applied, the transformed scores align more closely with those from other models, reducing error in threshold reuse from ~15 % to <2 %. Linear and quantile mappings show modest improvement but are less effective. The synthetic probing framework also reveals that some model families (e.g., transformer‑based) produce scores with higher variance, which the isotonic mapping mitigates.

## Significance  
This work matters because it provides a practical, scalable method for evaluating and aligning embedding similarity spaces without requiring ground truth labels or manual calibration. By learning score mappings, organizations can reuse retrieval thresholds across models, reducing engineering effort in model migration. The isotonic regression finding offers a robust baseline for cross‑model threshold portability, which is crucial as generative systems increasingly rely on dynamic retrieval.

## Related Concepts  
- Similarity space alignment  
- Cross‑model calibration  
- Synthetic probing  
- Isotonic regression  
- Cosine similarity scoring
