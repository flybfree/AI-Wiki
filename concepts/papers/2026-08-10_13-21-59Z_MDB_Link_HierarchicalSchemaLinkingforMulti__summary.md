# Summary: 2026-08-10_13-21-59Z_MDB_Link_HierarchicalSchemaLinkingforMulti_Databas.md
Saved: 2026-08-10 23:50
Source: 2026-08-10_13-21-59Z_MDB_Link_HierarchicalSchemaLinkingforMulti_Databas.md
Model: None

---

## Summary  
Traditional Text‑to‑SQL systems assume a single known target database and ignore the challenge of locating that database among many heterogeneous sources. MDB‑Link tackles this by introducing a hierarchical schema‑linking framework that first discovers the relevant database, then builds a compact, SQL‑relevant schema for query generation. The approach combines global index retrieval with evidence aggregation to shortlist candidate databases and leverages a budget‑aware large language model (LLM) for reranking, table selection, and column grounding. Experiments show that MDB‑Link not only improves exact match scores dramatically across several benchmarks but also runs faster than prior methods.  

## Key Contributions  
- [Finding 1] A hierarchical schema‑linking pipeline that integrates global index retrieval with evidence aggregation to shortlist databases in a multi‑database setting.  
- [Finding 2] A budget‑aware LLM that performs database reranking, table selection, and column grounding while respecting a limited token budget.  
- [Finding 3] Empirical improvements: exact match rises from 16.88 to 51.41 on MMQA, 2.50 to 9.17 on Spider2‑Snow, and 12.52 to 38.01 on BIRD‑dev; MDB‑Link also outperforms LinkAlign and AutoLink in speed.  

## Methodology  
The authors first extract question‑relevant columns from a global index that indexes all tables across the database collection, creating a candidate set of potential databases. They then aggregate retrieval evidence to rank these candidates and feed the top‑k into a budget‑aware LLM. The LLM is constrained by a token budget to generate reranked orderings, select appropriate tables, and ground column references to the chosen schema. This hierarchical process reduces the schema size to match gold standards while preserving SQL relevance.  

## Results  
Exact match scores improve significantly: MMQA from 16.88 % to 51.41 %, Spider2‑Snow from 2.50 % to 9.17 %, BIRD‑dev from 12.52 % to 38.01 %. MDB‑Link also demonstrates faster inference times compared with LinkAlign and AutoLink, confirming that hierarchical schema reduction benefits downstream SQL generation without sacrificing performance.  

## Significance  
MDB‑Link addresses a critical gap in Text‑to‑SQL research by handling heterogeneous database collections, enabling systems to locate the correct database automatically. The hierarchical design reduces schema complexity, making downstream LLM inference more efficient and scalable. By achieving higher exact matches and faster runtimes, MDB‑Link sets a new benchmark for multi‑database text‑generation tasks.  

## Related Concepts  
Text‑to‑SQL, Schema Linking, Multi‑Database Retrieval, Global Index Construction, Evidence Aggregation, Budget‑Aware LLM, Reranking, Table Selection, Column Grounding, Heterogeneous Database Collection.
