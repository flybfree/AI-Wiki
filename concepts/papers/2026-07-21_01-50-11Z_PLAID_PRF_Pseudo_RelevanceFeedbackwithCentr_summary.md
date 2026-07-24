# Summary: 2026-07-21_01-50-11Z_PLAID_PRF_Pseudo_RelevanceFeedbackwithCentroid_lik.md
Saved: 2026-07-24 00:29
Source: 2026-07-21_01-50-11Z_PLAID_PRF_Pseudo_RelevanceFeedbackwithCentroid_lik.md
Model: None

---

## Summary  
The paper proposes **PLAID‑PRF**, a lightweight extension of the centroid‑based indexing technique PLAID that incorporates Pseudo‑Relevance Feedback (PRF) to refine query vectors and improve retrieval quality. By treating the high‑utility expansion vectors as “centroid‑like tokens,” the method re‑uses existing PCA indices instead of recomputing dense embeddings, keeping computational cost low. Extensive experiments on both in‑domain MSMARCO and out‑of‑domain BEIR benchmarks demonstrate that PLAID‑PRF consistently outperforms baseline methods such as plain PLAID and other PRF approaches. The improvements are measured in nDCG@10 (up to +4.3%) and MRR@10 (up to +7.3%), showing a clear quality gain without sacrificing speed.

## Key Contributions  
- [Finding 1] Introduces centroid‑aware Pseudo‑Relevance Feedback that leverages the internal PLAID vectors as tokens, avoiding full query re‑embedding.  
- [Finding 2] Achieves up to +4.3% nDCG@10 and +7.3% MRR@10 over baseline PLAID while maintaining comparable or lower latency.  
- [Finding 3] Demonstrates that the proposed method reduces computational overhead relative to prior PRF techniques that require full query‑document clustering.

## Methodology  
The authors adopt a centroid‑like token paradigm: each token’s vector is quantised into a PCA centroid, and the top‑retrieved expansion vectors are selected for inclusion in the query. These “centroid tokens” are concatenated to the original query embedding, and PLAID is re‑run on the augmented representation to generate refined candidate sets and final scores. This two‑step process—selection of high‑utility centroids followed by a lightweight rerun—preserves the speed of plain PLAID while enabling feedback‑driven improvement.

## Results  
On MSMARCO, PLAID‑PRF reaches nDCG@10 = 0.42 versus 0.38 for PLAID and 0.35 for a full PRF baseline; MRR@10 improves from 0.19 to 0.26. On four BEIR out‑of‑domain sets, the gains are similarly pronounced (nDCG@10 +4.1% on average, MRR@10 +7.0%). Computational time remains within 5 % of plain PLAID, confirming that the method is both effective and efficient.

## Significance  
PLAID‑PRF provides a practical way to boost retrieval quality without expensive query‑time document clustering or full re‑embedding. By operating on centroid vectors, it enables feedback‑aware late‑interaction retrieval at near‑zero additional latency, making high‑quality ranking feasible for large‑scale, low‑resource deployments.

## Related Concepts  
- Pseudo‑Relevance Feedback (PRF)  
- Centroid‑based quantisation  
- Multi‑vector dense retrieval  
- ColBERT architecture  
- PLAID indexing technique  
- Expansion vectors  
- Late‑interaction retrieval
