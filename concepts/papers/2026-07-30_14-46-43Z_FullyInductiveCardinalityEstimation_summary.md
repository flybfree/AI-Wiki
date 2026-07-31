# Summary: 2026-07-30_14-46-43Z_FullyInductiveCardinalityEstimation.md
Saved: 2026-07-30 21:56
Source: 2026-07-30_14-46-43Z_FullyInductiveCardinalityEstimation.md
Model: None

---

## Summary  
The paper introduces FICE (Fully Inductive Cardinality Estimation), a graph neural network that estimates the cardinality of Basic Graph Pattern SPARQL queries without retraining, even on unseen knowledge graphs. It generalizes to entirely new graphs and relations, eliminating the transductive limitation of prior learned estimators. The estimator uses an encoder GNN to produce entity‑relation embeddings from a factor‑graph view and a decoder GNN that composes these embeddings along the query join topology. Experiments show FICE reduces median q‑error dramatically compared with state‑of‑the‑art baselines.

## Key Contributions  
- [Finding 1] A fully inductive learned cardinality estimator that works on unseen graphs without retraining.  
- [Finding 2] A joint encoder‑decoder GNN architecture where embeddings are specialized for local neighborhood functions.  
- [Finding 3] Training with neighborhood sampling enables sub‑millisecond latency at scale.

## Methodology  
FICE builds a factor‑graph representation of the KG, then applies an encoder GNN that performs message passing over the 2‑hop neighborhood to generate entity and relation embeddings. These embeddings are specialized because BGP cardinality is proven to be a local function of that neighborhood. A decoder GNN receives these embeddings in the order dictated by the query’s join topology and predicts log‑cardinality. The encoder and decoder are trained jointly using sampled neighborhoods, decoupling embedding generation from decoding to keep inference fast.

## Results  
Over ten diverse KGs with millions of triples, FICE achieves a median q‑error of 5.34, compared with the best competitor’s 13.54. It also dominates all approaches in tail behavior, delivering more accurate estimates for rare cardinalities. Inference latency is under one millisecond per query.

## Significance  
Accurate cardinality estimation is crucial for query optimization and resource planning in large‑scale triplestores. By providing a fully inductive estimator that never requires retraining, FICE enables real‑time use on dynamic knowledge graphs, reducing operational overhead and improving user experience.

## Related Concepts  
- Graph Neural Networks (GNN)  
- Factor‑graph representation of KG  
- Local neighborhood function  
- Joint encoder‑decoder training  
- Neighborhood sampling for scalability
