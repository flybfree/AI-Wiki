# Summary: 2026-08-06_17-23-13Z_BeyondTop_K_ReplacingBlack_BoxRetrievalwithInterpr.md
Saved: 2026-08-06 22:25
Source: 2026-08-06_17-23-13Z_BeyondTop_K_ReplacingBlack_BoxRetrievalwithInterpr.md
Model: None

---

## Summary  
The conventional top‑k retrieval design for long documents is shown to be structurally unsound, especially in financial statements where chunk boundaries cause unit mismatches and misaligned fiscal‑year headers. The authors propose READ, an interpretable agentic system that replaces black‑box similarity search with three deterministic operations to produce reliable answers. Experiments on a 780‑page government report demonstrate that this approach yields substantial gains over the standard method.

## Key Contributions  
- Finding 1: Top‑k retrieval is structurally unsound for financial documents, leading to errors such as lakh/crore unit mismatches and missing fiscal‑year headers.  
- Finding 2: READ’s three deterministic operations—normalized lexical search, structural navigation, bounded span reads—provide a reproducible audit trail and outperform top‑k retrieval by 35.3 % on the test set.  
- Finding 3: Embedding‑based similarity (BM25) is statistically indistinguishable from pure lexical search, indicating that gains stem from agentic operations rather than richer embeddings.

## Methodology  
READ is built as an interface to the Model Context Protocol, integrating three sequential steps: (1) normalized lexical search across tokenized text, (2) structural navigation using document hierarchy (tables, headers) to locate relevant spans, and (3) bounded span reads that extract exact substrings. Each step is logged as a trajectory, creating an interpretable audit trail.

## Results  
On 51 verified questions from the 780‑page report, READ achieved 58.8 % answer accuracy versus dense retrieval’s 15.7 % (p_Holm = 2×10⁻⁵). Even with top‑k tuning, READ leads by 23.5 points over the standard approach.

## Significance  
This work shows that replacing opaque similarity scores with transparent agentic workflows can dramatically improve performance on structured long documents, offering a path toward more reliable AI systems in finance and compliance where errors have real‑world consequences.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Top‑k nearest neighbour retrieval  
- Embedding‑based similarity search (BM25, dense retrieval)  
- Model Context Protocol (MCP)  
- Agentic operations  
- Structured navigation of document hierarchy
