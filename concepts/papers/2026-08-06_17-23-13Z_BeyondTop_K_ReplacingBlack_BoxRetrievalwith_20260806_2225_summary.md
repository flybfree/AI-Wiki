# Summary: 2026-08-06_17-23-13Z_BeyondTop_K_ReplacingBlack_BoxRetrievalwithInterpr.md
Saved: 2026-08-06 22:25
Source: 2026-08-06_17-23-13Z_BeyondTop_K_ReplacingBlack_BoxRetrievalwithInterpr.md
Model: None

---

## Summary  
The authors critique the conventional “top‑k” retrieval approach for long, structured documents such as financial statements and audit reports, showing that it produces systematic errors because chunking ignores document structure. They introduce READ (Reliable Embedding‑free Agentic Document‑search), an interpretable agent that performs three deterministic operations—normalized lexical search, structural navigation, and bounded span reads—to retrieve relevant passages while preserving a full audit trail. Experiments on a 780‑page government report demonstrate that READ outperforms dense retrieval (58.8 % correct) and even tuned top‑k methods (35.3 % correct), whereas the standard top‑k baseline reaches only 27.5 %. The study also shows that BM25 yields no statistically different results from READ, confirming that the gains arise from agentic operations rather than lexical search alone.

## Key Contributions  
- **Finding 1:** A systematic analysis reveals that chunking long documents into fixed‑size blocks creates measurable errors in financial texts, such as misinterpreting lakh vs. crore units due to improper header handling.  
- **Finding 2:** The READ framework replaces black‑box similarity scores with three transparent, deterministic operations that produce a reproducible retrieval trajectory and an audit trail.  
- **Finding 3:** Experiments confirm that READ’s agentic approach yields significantly higher accuracy (58.8 % vs. 15.7 % for dense retrieval) than both top‑k retrieval (27.5 %) and tuned versions, while BM25 shows no advantage over lexical search.

## Methodology  
The authors first constructed a steelman table‑aware chunker that correctly aligns numeric units with their fiscal‑year headers but still leaves many chunks incomplete. To address the remaining issues, they designed READ as an agent operating on the Model Context Protocol (MCP). The agent performs normalized lexical search to locate candidate spans, structural navigation using document metadata (e.g., table rows, figure numbers), and bounded span reads that extract only the necessary text segment. Each operation is logged, allowing a full trace of how a query was answered.

## Results  
On 51 verified questions, READ achieved 58.8 % correct answers versus dense retrieval’s 15.7 % (p_Holm = 2×10⁻⁵). Even after tuning the top‑k tool, READ remains superior at 35.3 %, outpacing it by 23.5 points (p_Holm = 0.017). The standard top‑k baseline scores only 27.5 %. A statistical test shows BM25 is indistinguishable from lexical search, indicating that embedding‑free agentic retrieval delivers distinct performance gains.

## Significance  
This work moves beyond opaque similarity scores toward interpretable, auditable information retrieval for high‑stakes documents where factual precision matters. By exposing the exact steps an agent takes, READ enables verification and accountability, reducing errors that stem from structural ignorance in chunking. The results also highlight a practical gap: embedding‑based methods cannot automatically compensate for poor document modeling.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Top‑k nearest neighbour search  
- Document chunking and normalization  
- Model Context Protocol (MCP)  
- Agentic retrieval frameworks
