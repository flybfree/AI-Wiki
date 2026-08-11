# Summary: 2026-08-09_14-23-08Z_AnchorFold_AFocus_Then_FoldFrameworkviaRecursiveAt.md
Saved: 2026-08-10 23:23
Source: 2026-08-09_14-23-08Z_AnchorFold_AFocus_Then_FoldFrameworkviaRecursiveAt.md
Model: None

---

## Summary  
Multi‑vector visual document retrieval (VDR) stores many visual patch embeddings per page, creating a large index that is costly to maintain and score. Existing training‑free compression methods either prune aggressively—causing sharp performance drops—or merge vectors without prioritizing important regions, leading to loss of fidelity. AnchorFold addresses this by introducing a **focus‑then‑fold** framework that leverages recursive attention propagation to identify high‑centrality tokens as anchors and then summarizes the remaining tokens around them. This approach compresses the index while preserving most of the retrieval signal, enabling near‑lossless compression at high ratios.

## Key Contributions  
- AnchorFold introduces a training‑free focus‑then‑fold compression scheme for document‑side retrieval indices.  
- It employs Recursive Attention Propagation over visual self‑attention graphs to compute centrality scores within each head and layer, selecting the highest‑centrality tokens as anchors.  
- The fold stage assigns remaining tokens to their nearest anchors in a normalized retrieval space and aggregates groups using centrality‑weighted aggregation, preserving non‑anchor contributions while concentrating capacity on structurally important regions.

## Methodology  
The authors view the index compression problem as a two‑stage process: first, **focus** identifies salient visual patches by propagating attention scores recursively across heads and layers; second, **fold** groups all tokens into anchor‑centered clusters using their normalized retrieval distances. Each cluster is then summarized with a centrality‑weighted aggregation that retains the contribution of non‑anchor tokens but discards redundant information. This recursive propagation ensures that important regions are retained as anchors while the rest of the document is efficiently represented.

## Results  
Across ViDoRe v1/v2 and REAL‑MM‑RAG evaluated with three diverse retrieval backbones, AnchorFold consistently outperforms all training‑free baselines at compression ratios γ ≤ 0.20. At 5× index compression it retains an average NDCG@5 of 98.3%, and at 20× compression the performance drops to 92.4%. These results demonstrate that AnchorFold can achieve near‑lossless compression while preserving retrieval quality.

## Significance  
Efficient, training‑free index compression is critical for large‑scale document indexing where storage and latency are constraints. By concentrating representation on high‑centrality tokens and using recursive attention propagation, AnchorFold reduces memory footprint up to 20× without sacrificing much retrieval performance. This enables scalable deployment of visual document retrievers in production systems.

## Related Concepts  
- Multi‑vector visual document retrieval (VDR)  
- Attention propagation / Recursive Attention Propagation  
- Centrality scores for token importance  
- Anchor selection and grouping  
- Normalized retrieval space  
- Centrality‑weighted aggregation  
- Compressed retrieval indices
