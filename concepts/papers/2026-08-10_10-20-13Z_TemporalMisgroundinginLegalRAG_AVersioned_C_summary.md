# Summary: 2026-08-10_10-20-13Z_TemporalMisgroundinginLegalRAG_AVersioned_CorpusBe.md
Saved: 2026-08-10 23:45
Source: 2026-08-10_10-20-13Z_TemporalMisgroundinginLegalRAG_AVersioned_CorpusBe.md
Model: None

---

## Summary  
The paper identifies temporal misgrounding in legal RAG, where a retrieval system returns an earlier or future version of a French tax article instead of the currently in‑force one, and proposes FiscalQA Pro as a benchmark to expose this problem. It builds a fully versioned corpus spanning 1938–2031 (32,436 article‑versions) paired with expert‑scored questions that require selecting the correct temporal version. The study shows that standard RAG treats the corpus as static and fails catastrophically at retrieving date‑applicable answers, while a multi‑version retriever achieves high recall. The work releases data, code, and benchmarks for further research.

## Key Contributions  
- Temporal misgrounding is identified as systematic retrieval of the wrong version in legal RAG.  
- FiscalQA Pro benchmark with 32,436 article‑versions and 209 expert‑scored questions across CGI articles.  
- A multi‑version retriever reaches 98.3% mean strict accuracy; static RAG only 0% correct.

## Methodology  
The authors constructed a versioned corpus of the French tax code covering nine decades, pairing each article with its future and past versions. They created an all‑model‑hard temporal‑reasoning track consisting of 209 expert‑reviewed questions that must select the current version. Evaluation used deterministic atomic ground‑truth nuggets (regex and numeric‑with‑tolerance) rather than LLM judges to avoid inheriting bias.

## Results  
Across eleven models—five frontier closed‑API systems, Gemini 2.5 Pro as a substitute entry, and five open‑weight models—their parametric knowledge yields 3.0% mean strict accuracy; RAG over a static current‑version corpus improves this to 2.7%. The end‑to‑end multi‑version retriever reaches 98.3% mean strict; an oracle‑article ablation gives 99.1%, indicating the bottleneck is first‑stage recall rather than version selection.

## Significance  
This work demonstrates that legal question answering is a temporally indexed retrieval problem, not a static lookup, and provides a benchmark to measure version‑aware performance. By exposing the failure of standard RAG to retrieve date‑applicable articles, it guides the development of more robust systems for dynamic legislation.

## Related Concepts  
- Temporal misgrounding  
- Versioned corpus  
- Legal Retrieval Augmentation (RAG)  
- CGI articles  
- Atomic ground‑truth nuggets  
- Multi‑version index  
- Recall vs. precision trade‑off
