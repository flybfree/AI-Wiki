# Summary: 2026-08-01_07-28-39Z_HP_JEPA_HierarchicalPartitioningforMulti_Resolutio.md
Saved: 2026-08-03 23:51
Source: 2026-08-01_07-28-39Z_HP_JEPA_HierarchicalPartitioningforMulti_Resolutio.md
Model: None

---

## Summary  
Graph self‑supervised learning seeks to extract transferable representations from massive unlabeled graphs, and Joint‑Embedding Predictive Architectures (JEPAs) achieve this by predicting masked targets directly in latent space without constructing explicit negative pairs. Existing graph JEPAs are limited because they rely on a single fixed partition, which biases the learned features toward one structural scale and prevents the model from exploiting complementary patterns at different resolutions. Our contribution is HP‑JEPA, a hierarchical partitioning framework that creates an ordered bank of coarse‑to‑fine partitions for each graph. By processing each resolution with its own online encoder, exponential‑moving‑average target encoder, and latent predictor, HP‑JEPA integrates multi‑resolution representations to improve downstream performance.

## Key Contributions  
- [Finding 1] Introduces hierarchical partitioning that generates multiple resolution‑specific graph embeddings.  
- [Finding 2] Uses an online encoder with an exponential‑moving‑average target encoder and a latent predictor for each partition, enabling context‑target prediction at every scale.  
- [Finding 3] Demonstrates superior performance over fixed‑resolution Graph‑JEPA on six out of eight graph classification tasks and on most regression benchmarks.

## Methodology  
HP‑JEPA first partitions a given graph into an ordered set of resolutions, starting from coarse clusters that coarsen to finer neighborhoods. For each resolution, the online encoder processes node features, producing a latent representation; this representation is then updated by the exponential‑moving‑average target encoder and fed to the latent predictor which outputs predictions for masked nodes. The resolution‑specific embeddings are concatenated or weighted according to a task‑specific scheme, yielding a unified multi‑resolution output that captures local, regional, and global structural cues simultaneously.

## Results  
Experiments on seven graph classification benchmarks and one regression benchmark show HP‑JEPA outperforms the fixed‑resolution Graph‑JEPA baseline on six of eight tasks. Size‑stratified analyses reveal higher accuracy than Graph‑JEPA across most quartiles of graph size for three representative datasets, confirming that hierarchical partitioning benefits both small and large graphs.

## Significance  
By decoupling representation learning from a single partition, HP‑JEPA enables more robust self‑supervised graph models that can adapt to varying structural scales without manual intervention. This approach reduces reliance on handcrafted negative pairs and improves transferability across diverse graph sizes, offering a practical improvement for large‑scale unlabeled graph datasets.

## Related Concepts  
graph self‑supervision, joint‑embedding predictive architecture (JEPA), multi‑resolution partitioning, online encoder, exponential moving average target encoder, latent predictor, hierarchical bank of resolutions.
