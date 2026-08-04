---
title: TBSG-Net: Temporal Bipartite Scene Graph Network for Fine-Grained Video Moment Retrieval
url: http://arxiv.org/abs/2608.02056v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_10-52-32Z_TBSG_Net_TemporalBipartiteSceneGraphNetworkforFine.md
generated_at: 2026-08-03 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TBSG‑Net, a proposal‑free video moment retrieval model that tackles two limitations of static scene graphs: lack of temporal dynamics and absence of explicit duration encoding. By using dynamic bipartite scene graphs (DSGs) and a Dynamic Scene Graph Embedding module, the network learns event‑centric representations that capture both spatio‑temporal information and relationship spans. Experiments show TBSG‑Net outperforms all baselines on VMR tasks.

## Key Takeaways
- The model introduces DSGs to model how objects and their relationships evolve over time, directly addressing the first limitation of static scene graphs.
- It adds a TBSG Constructor that encodes temporal span alongside object‑relationship pairs, solving the second limitation of missing duration information.
- The hybrid TBSG Encoder combines a Transformer for global event modeling with a Graph Convolutional Network for fine relational reasoning to produce rich spatio‑temporal embeddings.

## Context
Static scene graphs have been widely used in video analysis but they ignore temporal evolution, which is crucial for moment retrieval. This work bridges that gap by proposing the first dynamic bipartite graph framework, aligning with trends toward richer multimodal representations and end‑to‑end learning pipelines.

## Implications
For practitioners, TBSG‑Net offers a scalable way to retrieve specific moments without manual proposal generation, improving system efficiency. In industry, it can be integrated into real‑time video analytics for event detection and content moderation where precise timing matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02056v1)
