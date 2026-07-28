# Summary: 2026-07-24_18-31-11Z_Language_RoutedRAGandDirectOptionScoringforMultili.md
Saved: 2026-07-27 23:24
Source: 2026-07-24_18-31-11Z_Language_RoutedRAGandDirectOptionScoringforMultili.md
Model: None

---

## Summary  
The paper introduces DS@GT, a language‑routed retrieval‑augmented pipeline designed to tackle multilingual financial question answering on the FinMMEval benchmark. It combines BGE‑M3 embeddings with FAISS indexing and Retrieval‑Augmented Direct Scoring (RADS) that scores answer options directly via next‑token log‑probabilities rather than generating free‑form text. The system selects a model per language—Qwen3 for Arabic, Chinese, Hindi; Qwen2.5‑14B for English; Llama‑3.1‑8B for Greek—based on empirical ablations that reveal large language‑asymmetric performance gaps. Low‑resource languages benefit from fused retrieval indices using weighted Reciprocal Rank Fusion.

## Key Contributions  
- [Finding 1] The Retrieval‑Augmented Direct Scoring (RADS) framework outperforms conventional RAG by directly evaluating answer options through next‑token log‑probabilities, yielding higher accuracy without free‑text generation.  
- [Finding 2] Fusing per‑language and cross‑lingual retrieval indices with weighted Reciprocal Rank Fusion improves recall for low‑resource languages such as Greek, Hindi, and Arabic.  
- [Finding 3] Empirical routing analysis shows Qwen3 excels in Arabic/Chinese/Hindi while Llama‑3.1 is optimal for Greek; chain‑of‑thought prompting harms performance, especially in Greek where accuracy drops from 90.7 % to 20.9 %.

## Methodology  
The authors built a multilingual knowledge base containing 30,209 entries and encoded queries and documents with BGE‑M3 embeddings for semantic similarity. FAISS was used to index the corpus and retrieve top‑k exemplars per query. Language routing was determined through ablation studies comparing model outputs across languages; retrieval‑augmented direct scoring reads next‑token log‑probabilities over candidate answer letters instead of producing free text. For low‑resource languages, a weighted Reciprocal Rank Fusion combines language‑specific and cross‑lingual indices to boost recall.

## Results  
The system achieved DS@GT scores above 85 % on English queries, >70 % on Arabic, Chinese, and Hindi, and around 62 % on Greek (though chain‑of‑thought prompting reduces it to ~21 %). Enabling Qwen3’s default thinking mode collapses Arabic RADS performance to near‑chance. The fusion approach lifts Greek recall from 48 % to 62 %, demonstrating significant gains for low‑resource languages.

## Significance  
This work bridges the gap between generic NLP benchmarks and domain‑specific financial reasoning across multiple languages, proving that language‑aware retrieval, model selection, and scoring strategies are essential for reliable multilingual QA. By showing how routing and fused indexing can mitigate performance asymmetries, DS@GT offers a practical blueprint for deploying robust, multilingual answer systems in certification exams.

## Related Concepts  
Retrieval‑Augmented Generation (RAG), Retrieval‑Augmented Direct Scoring (RADS), language routing, Reciprocal Rank Fusion, BGE‑M3 embeddings, FAISS indexing, chain‑of‑thought prompting.
