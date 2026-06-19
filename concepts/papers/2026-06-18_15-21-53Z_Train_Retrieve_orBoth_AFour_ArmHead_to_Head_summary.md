# Summary: 2026-06-18_15-21-53Z_Train_Retrieve_orBoth_AFour_ArmHead_to_HeadforCorr.md
Saved: 2026-06-18 21:01
Source: 2026-06-18_15-21-53Z_Train_Retrieve_orBoth_AFour_ArmHead_to_HeadforCorr.md
Model: None

---


## Summary  
The authors investigate whether a purely fine‑tuned model can provide correct statutory citations under the Ontario Residential Tenancies Act or if retrieval assistance is required. They evaluate four variants of Qwen2.5‑7B‑Instruct—zero‑shot, LoRA SFT‑only, RAG‑only, and an SFT + RAG hybrid—on a small human‑verified evaluation set measuring exact‑match citation (section + subsection). The study shows that retrieval is indispensable for accurate citations, while the hybrid approach eliminates hallucinations and achieves the best performance without costly large models or massive datasets.  

## Key Contributions  
- Retrieval is essential for correct statutory citation; pure fine‑tuning alone cannot produce valid citations.  
- A lightweight SFT + RAG hybrid reaches 0.481 exact‑match with zero hallucinated citations, outperforming both pure retrieval and larger RAG pipelines.  
- The hybrid’s performance does not improve with more data or specialized retrieval models; a cheap bge‑small embedder suffices.  

## Methodology  
The authors conduct a four‑arm head‑to‑head experiment on Qwen2.5‑7B‑Instruct, comparing: (1) base zero‑shot generation, (2) LoRA SFT‑only fine‑tuning, (3) RAG‑only augmentation using a standard retriever, and (4) an SFT + RAG hybrid that combines the two. All models generate responses to queries about the Ontario Residential Tenancies Act 2006 and its core regulation; each response is scored on exact‑match citation against human‑verified sections of the law.  

## Results  
- The zero‑shot model never cites any section, confirming that retrieval is necessary.  
- LoRA SFT‑only misrecalls sections, indicating insufficient provision selection.  
- Retrieval alone drives hallucination to zero but still fails on exact‑match because it may select irrelevant passages.  
- The SFT + RAG hybrid achieves the highest score (0.481) with no hallucinated citations, outperforming a larger RAG pipeline that uses a bigger embedder and cross‑encoder reranker.  
- Adding more data or using a more specialized retrieval model yields no further gains; performance plateaus at 0.481 exact‑match.  

## Significance  
The work demonstrates that hybrid SFT + RAG can reliably produce correct statutory citations in a legal domain, eliminating hallucinations and meeting the “lift‑over‑base” benchmark without expensive resources. It provides a practical template for low‑cost, high‑accuracy retrieval augmentation in knowledge‑intensive tasks where precise citation is critical.  

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Supervised fine‑tuning (SFT) and LoRA adapters  
- Exact‑match scoring for legal citations  
- Hallucination in generative models  
- Low‑cost embedding models (bge‑small)
