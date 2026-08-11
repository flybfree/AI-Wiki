# Summary: 2026-08-10_10-20-13Z_TemporalMisgroundinginLegalRAG_AVersioned_CorpusBe.md
Saved: 2026-08-11 00:01
Source: 2026-08-10_10-20-13Z_TemporalMisgroundinginLegalRAG_AVersioned_CorpusBe.md
Model: None

---

## Summary  
The paper identifies a systematic problem called *temporal misgrounding* in legal retrieval‑augmented generation (RAG): models retrieve the currently in‑force version of a French tax article only 0 % of the time and instead cite earlier or future versions. To address this, the authors introduce **FiscalQA Pro**, a benchmark that pairs a versioned corpus of 32 436 article‑versions (1938–2031) with an expert‑scored temporal‑reasoning track of 209 questions across CGI articles. The study demonstrates that even the best models achieve only modest gains over static baselines, highlighting a critical gap in legal QA systems.

## Key Contributions  
- **Finding 1:** Temporal misgrounding is a systematic issue where retrieval returns non‑applicable versions of legal texts instead of the current version.  
- **Finding 2:** The authors introduce **FiscalQA Pro**, a versioned corpus and expert‑scored benchmark that quantifies this problem across 32 436 article‑versions and 209 CGI articles.  
- **Finding 3:** Even state‑of‑the‑art RAG models retrieve the wrong version 100 % of the time, yielding only a modest (≈3 %) strict accuracy improvement over static baselines.

## Methodology  
The authors built a multi‑year French tax code corpus spanning 93 years (1938–2031) and paired each article‑version with its corresponding CGI articles. They created an “all‑model‑hard temporal‑reasoning” track containing 209 expert‑reviewed questions, scored deterministically using atomic ground‑truth nuggets (regex patterns and numeric tolerances). Evaluation was performed both closed‑book (no LLM judge) and end‑to‑end retrieval with a multi‑version index. The pipeline includes the full corpus, benchmark data, model responses, and code.

## Results  
Parametric knowledge alone yields a mean strict accuracy of **3.0 %**. When using RAG over a static current‑version corpus, performance improves by **2.7 %** (≈5.7 %). An end‑to‑end retriever over the multi‑version index reaches **98.3 %** mean strict accuracy; an oracle‑article ablation raises it to **99.1 %**, indicating that the bottleneck lies in first‑stage recall rather than version selection. Crucially, static RAG cites a real but inapplicable version **0 %** of the time.

## Significance  
The work shows that legal question answering is fundamentally a temporally indexed retrieval problem and provides the first comprehensive benchmark for *temporal misgrounding* in French tax law. By quantifying how often models retrieve outdated or future versions, it drives research toward temporal indexing solutions and improves reproducibility across the community.

## Related Concepts  
- Temporal misgrounding  
- Versioned corpus  
- Legal RAG (Retrieval‑Augmented Generation)  
- CGI articles (Cahiers de l’Informatique et des Jeux)  
- Atomic ground‑truth nuggets  
- Recall bottleneck  
- Static vs. dynamic retrieval
