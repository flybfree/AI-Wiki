# Summary: 2026-07-29_11-39-21Z_FedTopo_Relation_LevelTopologySharingforModel_Hete.md
Saved: 2026-07-29 21:38
Source: 2026-07-29_11-39-21Z_FedTopo_Relation_LevelTopologySharingforModel_Hete.md
Model: None

---

## Summary  
Federated learning (FL) struggles to transfer knowledge across clients when each client runs a different model architecture, because the resulting feature representations are not aligned in an absolute space. Existing FL methods share only parameters, distilled predictions or prototypes, all of which must be expressed in a common coordinate system that can mislead local training. FedTopo addresses this by encoding global knowledge as a **relation‑level topology**—the pattern of how classes relate to one another within each client’s own representation space—rather than trying to align raw feature vectors. This approach lets clients upload lightweight class statistics, and the server aggregates them in a reliability‑aware way before broadcasting a global topology that guides local training.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] **Relation‑level topology sharing**: FedTopo replaces parameter or prototype sharing with a compact representation of class relationships learned locally.  
- [Finding 2] **Reliability‑aware aggregation**: The server down‑weights weak or noisy relations, producing a more trustworthy global topology.  
- [Finding 3] **Topology‑guided local training**: The broadcasted global topology is used to emphasize negative classes that are topologically similar to the current class during loss computation.

## Methodology  
Each client first builds its relation topology by computing pairwise similarity among local prototypes and extracting class statistics (e.g., prototype embeddings, class counts). These relations are encoded as a lightweight graph or adjacency matrix and uploaded together with the class statistics. The server receives all such graphs, performs a weighted aggregation that favors high‑confidence edges, and then broadcasts the aggregated global topology to every client. During local training, the loss is augmented so that when a negative example is selected, its similarity to the positive class is evaluated against the global topology; if the relation matches the global pattern, it receives a stronger penalty. This process requires only communication of the topology and no additional inference steps.

## Results  
Experiments on three benchmark datasets with eight different heterogeneous backbones demonstrate that FedTopo consistently outperforms baselines based on parameter sharing, distillation, or prototype sharing. The method achieves higher validation accuracy while using minimal communication (only the topology and class stats) and incurs zero inference overhead beyond the usual FL update. Ablation studies confirm that removing reliability weighting degrades performance, confirming the importance of trust‑based aggregation.

## Significance  
FedTopo enables effective knowledge transfer across model‑heterogeneous clients without requiring costly alignment of absolute feature spaces. By focusing on relational patterns and incorporating a reliability filter, it reduces communication load and inference cost while improving generalization—key advantages for large‑scale FL deployments where bandwidth is limited and latency must be minimized.

## Related Concepts  
- Federated learning (FL)  
- Model heterogeneity / non‑aligned representations  
- Prototypes and class embeddings  
- Parameter sharing in FL  
- Distillation techniques  
- Topology / graph representation of class relationships  
- Reliability‑aware aggregation  
- Negative sampling for loss functions
