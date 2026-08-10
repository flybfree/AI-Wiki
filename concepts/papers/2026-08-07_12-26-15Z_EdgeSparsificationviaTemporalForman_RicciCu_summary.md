# Summary: 2026-08-07_12-26-15Z_EdgeSparsificationviaTemporalForman_RicciCurvature.md
Saved: 2026-08-09 22:56
Source: 2026-08-07_12-26-15Z_EdgeSparsificationviaTemporalForman_RicciCurvature.md
Model: None

---

## Summary  
Temporal graph learning aims to model evolving networks such as financial transaction systems, communication channels, and social platforms, but dense graphs pose computational challenges. This paper introduces TRicci, a network‑curvature‑inspired edge sparsification framework that extends classical Forman‑Ricci curvature to directed weighted temporal graphs. By incorporating recency, structural support, and local competition into the curvature measure, TRicci enables aggressive graph reduction while preserving predictive performance. Experiments demonstrate up to 80 % fewer edges and a 56 % reduction in training and inference time without significant loss of accuracy.

## Key Contributions  
- Finding 1: Proposes TRicci, a curvature‑based edge sparsification framework for directed weighted temporal graphs.  
- Finding 2: Introduces a temporal Forman‑Ricci curvature that incorporates recency, structural support, and local competition.  
- Finding 3: Demonstrates that sparsified graphs maintain predictive performance across multiple graph‑level tasks.

## Methodology  
The authors define a new curvature measure on each edge by combining the classical geometric curvature with a temporal weight decaying over time steps. The measure uses node degrees, edge weights, and a recency factor derived from recent interaction strength to capture structural support and competition. Edges with high curvature are flagged for removal; the sparsified graph retains only low‑curvature connections. This iterative process gradually reduces density while preserving structural integrity.

## Results  
On nine real transaction networks and three benchmark temporal datasets, TRicci reduces the number of edges by an average of 80 % compared with dense graphs, cutting end‑to‑end training time by 55.94 % and inference latency accordingly. Downstream tasks such as node classification, link prediction, and sequence modeling achieve performance within 1–2 % of the full graph baseline.

## Significance  
The work shows that temporal curvature can serve as a principled guide for scalable dynamic graph learning, enabling massive sparsification without sacrificing predictive accuracy—a key step toward real‑time applications in finance, communications, and social media.

## Related Concepts  
Forman‑Ricci curvature, edge sparsification, temporal graphs, dynamic network learning, graph curvature measures, recency weighting, structural support, downstream prediction tasks.
