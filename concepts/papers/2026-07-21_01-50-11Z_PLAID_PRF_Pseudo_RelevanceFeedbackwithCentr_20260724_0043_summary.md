# Summary: 2026-07-21_01-50-11Z_PLAID_PRF_Pseudo_RelevanceFeedbackwithCentroid_lik.md
Saved: 2026-07-24 00:43
Source: 2026-07-21_01-50-11Z_PLAID_PRF_Pseudo_RelevanceFeedbackwithCentroid_lik.md
Model: None

---

## Summary  
PLAID‑PRF (Pseudo‑Relevance Feedback) extends the centroid‑based retrieval framework of PLAID by applying a lightweight feedback loop that refines query vectors using only the most informative expansion tokens rather than full document‑token clustering. The method treats high‑utility centroid vectors as pseudo‑tokens, appends them to the original query, and reruns PLAID to generate better candidate sets while preserving the speed benefits of centroid quantisation. This approach yields noticeable gains in retrieval quality without sacrificing the low‑cost nature of PCA‑style indexing.  

## Key Contributions  
- [Introduces a centroid‑aware pseudo‑relevance feedback (PRF) mechanism that operates within the PLAID framework, avoiding expensive query‑time document‑token clustering.]  
- [Selects a small, diverse set of high‑utility expansion vectors as pseudo‑tokens to improve candidate generation and final scoring.]  
- [Achieves up to 7.3 % MRR@10 improvement over baseline methods while introducing substantially less computational overhead than prior PRF approaches.]  

## Methodology  
The authors first compute centroid vectors for each token in the query, then rank these centroids by their relevance to the top‑retrieved results. The top‑k high‑utility centroids are selected as “expansion tokens” and concatenated to the original query vector. This augmented query is fed into PLAID again, which performs a second round of centroid quantisation and candidate generation. The final scores combine the original query’s centroid representation with the feedback from the expansion tokens, effectively simulating token‑level interactions without reconstructing full document embeddings.  

## Results  
Extensive experiments on the in‑domain MSMARCO benchmark and four out‑of‑domain BEIR datasets confirm that PLAID‑PRF consistently outperforms both plain PLAID and other PRF baselines. The method improves nDCG@10 by up to 4.3 % and MRR@10 by up to 7.3 %, with the latter metric being the most sensitive indicator of ranking quality. Crucially, the computational cost increase is minimal: only a single extra PCA step per query is required, preserving the low‑latency performance characteristic of centroid‑based indexing.  

## Significance  
By integrating pseudo‑relevance feedback into a centroid‑centric retrieval pipeline, PLAID‑PRF demonstrates that quality can be enhanced without resorting to costly full‑document embedding updates or token‑level clustering at query time. This lightweight mechanism is especially valuable for large‑scale systems where every millisecond of latency matters, offering a practical path toward better ranking while maintaining the efficiency of existing dense retrieval indexes.  

## Related Concepts  
- **PLAID**: centroid‑based quantisation of token vectors to reduce index size and accelerate retrieval.  
- **Pseudo‑Relevance Feedback (PRF)**: a technique that refines query vectors using feedback from retrieved documents without altering the original embeddings.  
- **Centroid vectors**: low‑dimensional approximations derived from high‑dimensional token embeddings, used as proxies for tokens in PRF.  
- **Dense retrieval**: models such as ColBERT that capture fine‑grained semantic interactions between queries and documents.
