# Summary: 2026-08-10_13-21-59Z_MDB_Link_HierarchicalSchemaLinkingforMulti_Databas.md
Saved: 2026-08-11 00:09
Source: 2026-08-10_13-21-59Z_MDB_Link_HierarchicalSchemaLinkingforMulti_Databas.md
Model: None

---

## Summary  
The paper tackles the challenge of linking query‑relevant database schemas when a user’s question may refer to any table in a large, heterogeneous collection of databases. Traditional Text‑to‑SQL systems assume a single known target schema, which limits their applicability to multi‑database scenarios. MDB‑Link proposes a hierarchical framework that first narrows down candidate databases using a global index and evidence aggregation, then selects the most relevant database with a budget‑aware large language model (LLM) for reranking, table choice, and column grounding. The approach reduces schema size while preserving SQL relevance, enabling faster downstream generation compared to prior methods.

## Key Contributions  
- [Finding 1] MDB‑Link introduces a hierarchical schema‑linking pipeline that separates database localization from column selection, improving modularity and efficiency.  
- [Finding 2] The framework employs a global index to retrieve question‑relevant columns across all databases, providing evidence for shortlisting candidate databases.  
- [Finding 3] A budget‑aware LLM is used for reranking and schema construction, achieving exact match improvements on benchmark datasets.

## Methodology  
The authors first construct a global index that maps each column to its containing database, enabling rapid retrieval of columns that appear in the user query. This evidence is aggregated per candidate database to produce a shortlist. The LLM then receives this shortlist along with a budget constraint (e.g., maximum schema size) and outputs a compact set of tables and columns that best satisfy the query while staying within the budget. Table selection is performed by evaluating which tables together cover the most retrieved columns, and column grounding follows from selecting the top‑scoring columns for each chosen table.

## Results  
Exact match scores were significantly improved: MMQA rose from 16.88 to 51.41, Spider2‑Snow from 2.50 to 9.17, and BIRD‑dev from 12.52 to 38.01. MDB‑Link also outperformed LinkAlign and AutoLink in terms of speed, showing faster inference times despite the additional hierarchical steps.

## Significance  
By enabling robust schema linking across multiple databases, MDB‑Link expands the applicability of Text‑to‑SQL systems beyond single‑database settings, supporting real‑world applications where data is distributed. The hierarchical design reduces computational load and improves exactness, offering a practical path toward scalable, user‑friendly SQL generation.

## Related Concepts  
- Schema linking (linking query to database tables)  
- Multi‑database Text‑to‑SQL  
- Global index for cross‑database column retrieval  
- Budget‑aware large language model inference  
- Hierarchical information processing
