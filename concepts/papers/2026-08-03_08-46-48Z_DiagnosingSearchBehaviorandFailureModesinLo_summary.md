# Summary: 2026-08-03_08-46-48Z_DiagnosingSearchBehaviorandFailureModesinLong_Hori.md
Saved: 2026-08-04 00:29
Source: 2026-08-03_08-46-48Z_DiagnosingSearchBehaviorandFailureModesinLong_Hori.md
Model: None

---

## Summary  
The paper investigates how search effort correlates with answer quality in long‑horizon deep search agents. It proposes a trajectory‑level diagnostic framework that separates evidence retrieval from evidence utilization to identify failure modes. By analyzing human‑annotated relevance judgments across multiple agents, the authors reveal that more searches do not necessarily improve answers and that useful evidence often appears early but is ignored later. The work offers practical insights for improving deep research systems.

## Key Contributions  
- Finding 1: Search effort and answer quality are only weakly aligned; accuracy correlates more strongly with cumulative retrieval recall than with number of queries or context length.  
- Finding 2: Useful evidence typically emerges in early steps, yet agents continue searching, generating a long tail of low‑yield retrievals that do not improve performance.  
- Finding 3: Exploratory reformulations remain beneficial at the query level, but top‑performing agents issue far fewer redundant queries.

## Methodology  
The authors constructed a diagnostic harness using human‑annotated document relevance scores to evaluate each search step. They fixed both the retrieval model and evaluation system while comparing six deep search agents on BrowseComp‑Plus and later on an open‑web API version of BrowseComp. The trajectory data were decomposed into evidence retrieval events and their subsequent utilization, allowing separate analysis of gaps in retrieval versus gaps in usage.

## Results  
Across all settings, the best agents retrieve high‑quality evidence early but then stop or switch to less informative queries. Average answer accuracy improved modestly with cumulative recall, whereas increasing query count had negligible effect. The longest trajectories contained many redundant queries that contributed little to final answer quality.

## Significance  
Understanding these failure modes helps researchers design better deep search agents by focusing on effective evidence selection, context management, and appropriate stopping criteria rather than simply expanding search effort.

## Related Concepts  
- Deep search agents  
- Trajectory‑level analysis  
- Evidence retrieval vs. utilization gaps  
- Cumulative recall  
- Query reformulation  
- Stopping criteria
