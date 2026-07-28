# Summary: 2026-07-27_08-46-27Z_DoCurrentRetrieversCoverAlltheEvidence_AControlled.md
Saved: 2026-07-28 00:10
Source: 2026-07-27_08-46-27Z_DoCurrentRetrieversCoverAlltheEvidence_AControlled.md
Model: None

---

## Summary  
The paper investigates the gap between merely retrieving a document that contains all requested evidence and actually delivering a complete‑first solution where every condition is satisfied on separate pages of the same document. Using the n‑Clue benchmark, which supplies gold queries with fully satisfying documents and naturally occurring subsets, the authors evaluate how well various retrieval systems achieve “complete‑first” success across 70 configurations. Their experiments reveal that while dense backbones improve performance by a few points, lexical‑visual fusion yields larger gains, yet generic rerankers still degrade Gold‑NDCG. Crucially, scaling a single dense model from 0.6 B to 8 B leaves complete‑first success unchanged, and the most advanced hybrid finds gold for only 35.8 % of queries despite supporting all conditions in 81.1 %. This work demonstrates that condition coverage—rather than gold discovery alone—remains the primary bottleneck.

## Key Contributions  
- [Finding 1] Condition‑wise decomposition improves dense backbones by 6.8–7.3 points and lexical‑visual fusion adds 8.7 points, while generic rerankers reduce Gold‑NDCG across 70 configurations.  
- [Finding 2] Scaling a single dense family from 0.6 B to 8 B changes complete‑first success by 0.0 points, indicating that model size alone does not resolve the coverage gap.  
- [Finding 3] The strongest hybrid achieves gold for 81.1 % of queries but only succeeds in complete‑first retrieval on 35.8 %, and this performance gap persists across condition count, target length, candidate density, query rendering, and the four‑source stress set.

## Methodology  
The authors employ n‑Clue as a controlled measurement instrument: 1,000 queries over 2,021 documents pair all‑condition golds with naturally occurring subsets. They evaluate 70 configurations of condition‑wise decomposition, dense backbones, lexical‑visual fusion, and generic rerankers. Performance is measured by complete‑first success, which requires a top‑10 gold to precede every released subset qrel. A four‑source stress set is used for additional robustness testing.

## Results  
Main experimental results show that condition‑wise decomposition yields modest gains (6.8–7.3 points) for dense backbones and larger gains (8.7 points) for lexical‑visual fusion, whereas generic rerankers consistently lower Gold‑NDCG. Scaling the dense model does not affect complete‑first success. The top hybrid system finds gold in 81.1 % of queries but only completes all conditions on 35.8 %. Page‑aware visual systems support stored evidence for only 5.1–5.3 % of queries, underscoring the rarity of full coverage.

## Significance  
These findings highlight that current retrieval systems excel at locating documents containing requested evidence but frequently fail to deliver a complete‑first solution where every condition is met on separate pages. The persistent gap between gold discovery and condition coverage suggests that existing architectures are limited by how well they integrate and verify multiple page‑specific conditions, rather than merely retrieving the right document.

## Related Concepts  
- Conjunctive cross‑page retrieval: searching for documents that satisfy multiple explicit conditions across different pages.  
- n‑Clue benchmark: a controlled dataset pairing all‑condition golds with naturally occurring subsets.  
- Dense backbones and lexical‑visual fusion: neural architectures that combine textual and visual embeddings.  
- Gold‑NDCG: a metric assessing how well retrieved documents match the gold query.  
- Complete‑first success: retrieving a document where all conditions are satisfied in order on separate pages.  
- Hybrid retrieval systems: models combining dense and lightweight components for efficiency.  
- Page‑aware visual support: systems that locate visual evidence stored per page.
