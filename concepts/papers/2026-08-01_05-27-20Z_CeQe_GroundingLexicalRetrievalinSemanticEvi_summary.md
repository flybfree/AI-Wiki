# Summary: 2026-08-01_05-27-20Z_CeQe_GroundingLexicalRetrievalinSemanticEvidence.md
Saved: 2026-08-03 20:22
Source: 2026-08-01_05-27-20Z_CeQe_GroundingLexicalRetrievalinSemanticEvidence.md
Model: None

---

## Summary  
Lexical retrieval methods such as BM25 fail to capture documents that contain semantically equivalent answers expressed with different vocabulary, leading to substantial recall loss on real‑world queries. The authors introduce Cross‑Encoder Query Expansion (CE‑QE), a lightweight augmentation technique that extracts decisive terms from cross‑encoder relevance attributions and appends them to the original BM25 query without modifying the index or hallucinating new tokens. This approach bridges the semantic vocabulary gap, improves recall where query and answer differ, and integrates seamlessly with existing reranking pipelines.  

## Key Contributions  
- CE‑QE seeds query expansion from the semantic retriever’s top passages rather than reusing BM25 results, preventing self‑reinforcing drift.  
- All expansion terms are verbatim copies of retrieved text, guaranteeing that no unseen vocabulary is introduced.  
- The method yields measurable gains on seven BEIR datasets (e.g., NQ Recall@100 ↑ 0.32→0.47) and outperforms score‑fusion alternatives by up to 5.3% nDCG@10.  

## Methodology  
The authors apply a cross‑encoder that outputs per‑token relevance scores on the BM25 top‑k results, then select terms whose cumulative attribution exceeds a threshold as decisive expansion tokens. These tokens are concatenated to the original query string and fed back into BM25 for reranking, forming the CE‑QE pipeline. A score‑fusion variant (SESF) combines BM25 scores with cross‑encoder relevance scores to further boost performance while keeping the index untouched.  

## Results  
On the BEIR benchmark, SESF achieves Recall@100 of 0.47 versus 0.32 for baseline CE‑QE, and nDCG@10 of 0.58 versus 0.53 for score‑fusion, surpassing SPLADEv2 (0.52) and ColBERTv2 (0.51). The underlying BM25 index remains unchanged, confirming that CE‑QE’s benefit stems solely from the query expansion step rather than a full reindex.  

## Significance  
CE‑QE demonstrates that modest, attention‑based augmentation can dramatically improve lexical recall without costly infrastructure changes, offering a practical solution for large‑scale retrieval systems where semantic synonymy is common. By leveraging existing cross‑encoder outputs, it reduces latency and avoids hallucinated terms, making it suitable for production deployment alongside traditional BM25 pipelines.  

## Related Concepts  
- Lexical Retrieval (BM25)  
- Semantic Search / Cross‑Encoder Retrieval  
- Query Expansion / Pseudo‑Relevance Feedback  
- Score Fusion in Retrieval Systems
