# Summary: 2026-07-31_19-18-37Z_HierarchicalBM25_LexicalSearchatBillion_DocumentSc.md
Saved: 2026-08-03 23:24
Source: 2026-07-31_19-18-37Z_HierarchicalBM25_LexicalSearchatBillion_DocumentSc.md
Model: None

---

## Summary  
The paper introduces Hierarchical BM25 to perform exact lexical search over a billion documents while keeping the resident footprint and query latency bounded. By replacing a flat index that would require 400 GB of DRAM with a coarse top‑down index, the authors achieve sub‑second response times and far higher throughput than conventional multi‑threaded implementations. The approach trades exact ranking for fixed resource usage, delivering a practical solution for interactive search at massive scale.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Hierarchical BM25 reduces the index size from ~400 GB to ~4.4 GB, enabling full resident operation on standard hardware.  
- [Finding 2] The coarse index selects up to a few thousand document groups per query using term‑frequency totals and co‑occurrence signals, preserving exact top‑k scores.  
- [Finding 3] Experiments show that visiting only 5–10 % of clusters for a billion‑document corpus recovers 0.83–0.92 of the exhaustive result score with negligible loss.

## Methodology  
The authors replace flat BM25 with a two‑stage process. First, they build a resident coarse index that stores per‑group term frequencies and global statistics (≈4.4 GB). For each query, these signals are used to compute relevance scores for candidate groups; the top‑scoring groups (typically 10–30) are then searched exhaustively with BM25, scoring documents against the same global statistics. The coarse index is size‑balanced and topical, so only relevant groups are expanded.

## Results  
Sixteen‑term queries over one billion documents return in ~300 ms, achieving 4.7× to 5.6× higher throughput than a flat multi‑threaded BM25 index. A warmed cache sustains ≈32 queries per second versus <3 for the flat approach. At a 500 K‑document configuration, visiting only 5–10 % of clusters recovers 0.83–0.92 of the exhaustive score.

## Significance  
Hierarchical BM25 enables scalable lexical search at billion‑scale corpora with bounded memory and low latency, eliminating disk I/O bottlenecks that plague flat indexes. This makes interactive retrieval feasible for real‑time applications such as recommendation systems and information retrieval services.

## Related Concepts  
BM25, hierarchical indexing, coarse index, topical grouping, co-occurrence signals, exact top‑k retrieval, blockmax‑wand, document reordering.
