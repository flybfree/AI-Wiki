# Summary: 2026-07-18_15-09-58Z_BeyondMemoryLeaderboards_EvaluatingScientificMemor.md
Saved: 2026-07-24 00:05
Source: 2026-07-18_15-09-58Z_BeyondMemoryLeaderboards_EvaluatingScientificMemor.md
Model: None

---

## Summary  
The authors introduce two full‑text scientific‑memory benchmarks—Public AI Memory (PAIM) and Public Transformers (PTr)—to evaluate how language models restore evidence from research papers under realistic retrieval budgets. Their work shows that memory leaderboards are misleading because they ignore critical factors such as ingestion granularity, raw‑text preservation, retrieval modality, and judge choice. By exposing these variables, the study demonstrates that performance can shift dramatically when a budget is fixed or when hybrid sparse‑dense retrieval is employed. The authors release all data, code, and judgments to enable reproducible research on scientific memory tasks.

## Key Contributions  
- [Finding 1] Memory leaderboards are not interpretable without the full protocol; results vary widely depending on ingestion granularity, raw‑text preservation, retrieval budget, modality, rubric audit, and judge choice.  
- [Finding 2] Retrieval budget heavily influences outcomes: for example, Graphiti leads PAIM but consumes 2.6 M characters per query, and its advantage disappears when the budget is controlled.  
- [Finding 3] On PTr, hybrid sparse‑dense retrieval variants of Simple RAG, Mem0, and Theoria tie for the top performance within a 0.03‑point margin, aligning closely with human evaluation.

## Methodology  
The authors created PAIM (81 papers, 66 questions) and PTr (252 papers, 98 questions), each representing full scientific articles. Eight memory/retrieval systems were tested: Theoria (a novel retrieval‑augmented generation model), a no‑retrieval baseline, and several standard RAG implementations. Ingestion was performed at sentence granularity with raw text retained; retrieval budgets ranged from 2 K to 5 M characters per query; modalities included BM25 and dense vector search. Human judges scored outputs on a ten‑point scale, and multi‑judge consistency was measured.

## Results  
The no‑retrieval baseline consistently underperformed across both benchmarks. On PAIM, Graphiti’s lead vanished after budget control, while hybrid sparse‑dense retrieval led PTr within 0.03 points of the best single‑stage model. Multi‑judge calibration revealed that LLM‑as‑a‑judge rankings are stable across frontier models and agree with human scores, resolving roughly one point on a ten‑point scale.

## Significance  
This study reframes scientific memory evaluation as budgeted, modality‑aware context restoration rather than an unconstrained architecture leaderboard. It highlights the need for standardized protocols that control retrieval cost and raw‑text fidelity to obtain trustworthy performance metrics. By releasing datasets and code, the authors provide a reusable framework for future research on LLM agents that must retrieve evidence from full‑length papers.

## Related Concepts  
- Memory retrieval in LLMs  
- Retrieval‑augmented generation (RAG)  
- Budget constraints on context length  
- Scientific paper parsing and evidence restoration  
- Human evaluation of AI outputs  
- Hybrid sparse‑dense retrieval strategies
