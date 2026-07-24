# Summary: 2026-07-18_15-09-58Z_BeyondMemoryLeaderboards_EvaluatingScientificMemor.md
Saved: 2026-07-24 00:05
Source: 2026-07-18_15-09-58Z_BeyondMemoryLeaderboards_EvaluatingScientificMemor.md
Model: None

---

## Summary  
The authors introduce two new full‑text scientific memory benchmarks—Public AI Memory (PAIM) and Public Transformers (PTr)—to evaluate how language models restore evidence from research papers, arguing that current leaderboards are misleading because they ignore critical protocol details such as ingestion granularity, raw‑text preservation, retrieval budget, modality, rubric audit, and judge choice. Their contribution is a methodological framework for treating scientific memory as *budgeted context restoration* rather than an unconstrained architecture competition, together with the release of datasets, code, and all intermediate outputs to enable reproducible research.

## Key Contributions  
- Memory leaderboards lack interpretability: rankings vary dramatically when ingestion granularity, raw‑text preservation, retrieval budget, modality, rubric audit, or judge choice are altered.  
- On PAIM Graphiti’s apparent lead disappears after controlling for the 2.6 million characters of retrieved context per query, demonstrating that budget constraints dominate performance.  
- Hybrid sparse‑dense retrieval methods (e.g., Simple RAG, Mem0, Theoria) tie for the top score on PTr, showing that integrating a dense model with a sparse index yields the most significant improvement.

## Methodology  
The authors created two benchmark datasets: PAIM contains 81 papers and 66 questions, while PTr holds 252 papers and 98 questions. Eight memory/retrieval systems were evaluated, including their own Theoria model and a no‑retrieval baseline. Each system was run under the same ingestion protocol (full‑text passage ingestion, raw‑text preservation) but with varying retrieval budgets (e.g., 2 M characters) and modalities (BM25 vs. dense RAG). The experiments measured context usage per query, compared hybrid versus sparse approaches, and performed multi‑judge human calibration to assess consistency.

## Results  
Graphiti leads on PAIM when no budget is imposed, but its advantage vanishes once the 2.6 M character limit is enforced. On PTr, sparse‑dense hybrids achieve scores within 0.03 points of each other, outperforming pure simple RAG or Mem0 models. Human and LLM‑as‑a‑judge evaluations converge on a ten‑point scale, resolving disagreements by roughly one point, indicating reliable calibration.

## Significance  
By exposing the fragility of leaderboard rankings to protocol variations, this work pushes the field toward a more rigorous evaluation of scientific memory as a budgeted restoration task. The released resources allow others to reproduce results and build fair comparisons, fostering trust in future AI agents that rely on accurate evidence retrieval.

## Related Concepts  
- Memory retrieval  
- Retrieval‑Augmented Generation (RAG)  
- Budgeted context restoration  
- Hybrid sparse‑dense retrieval  
- Benchmarking of LLM agents
