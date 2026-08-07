# Summary: 2026-08-06_08-07-18Z_SparseMutualInformationGraphAveragingforImprovingR.md
Saved: 2026-08-06 22:09
Source: 2026-08-06_08-07-18Z_SparseMutualInformationGraphAveragingforImprovingR.md
Model: None

---

## Summary  
The paper proposes a non‑gradient repair technique for Random Indexing (RI) embeddings by averaging vectors on a sparse Positive Pointwise Mutual Information (PPMI) graph that is pruned to the top‑K neighbors. By leveraging only sparse global corpus statistics, the method avoids dense co‑occurrence matrices and gradient training while still exploiting semantic similarity information. On the fairytales dataset, this approach raises semantic analogy accuracy from roughly 19 % to about 30 %, demonstrating a substantial boost without neural baselines. The improvement is most pronounced for seed42, where accuracy reaches around 34.6 %.  

## Key Contributions  
- Finding 1: Sparse mutual information (PPMI) graph averaging repairs weak RI initialization, leading to a noticeable gain in semantic analogy performance.  
- Finding 2: Top‑K pruning of the PPMI graph yields the best results; seed42 achieves the highest accuracy among all seeds.  
- Finding 3: The method is a non‑gradient repair that does not compete with neural baselines on standard evaluation sets such as text8 or SimLex‑999.  

## Methodology  
The authors construct a PPMI graph from sparse co‑occurrence statistics, then compute each node’s embedding by averaging the vectors of its top‑K neighbors. This process is applied to RI embeddings initialized with random indices; no gradient computation or dense matrix factorization is required. The sparsity ensures low memory usage and fast inference, while pruning retains only the most informative connections.  

## Results  
Experimental results on the fairytales analogy set show accuracy moving from 19.4 ±0.7 % to 30.7 ±2.9 % with PPMI top‑K=50 averaging, and a peak of 34.6 % for seed42. This outperforms baseline methods such as PPMI+SVD, Binary+SVD, CBOW, and Skip‑gram, all of which remain below the new level. Bloom filter sketches underperform RI in this configuration.  

## Significance  
The contribution is significant because it provides a lightweight, non‑gradient technique that can be integrated into existing sparse embedding pipelines without retraining or dense data structures. By exploiting only top‑K neighbor information from PPMI graphs, the method offers a practical way to improve semantic similarity for downstream tasks where RI embeddings are used.  

## Related Concepts  
Random Indexing (RI), Positive Pointwise Mutual Information (PPMI), Graph averaging, Top‑K pruning, Sparse mutual information, Semantic analogy evaluation, Neural baselines (text8, Skip-gram, CBOW, SVD), Bloom filter sketches.
