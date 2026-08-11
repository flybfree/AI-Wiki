# Summary: 2026-07-23_06-03-59Z_Best_of_Evidence_Best_of_NSelectionunderPartialVer.md
Saved: 2026-07-24 02:32
Source: 2026-07-23_06-03-59Z_Best_of_Evidence_Best_of_NSelectionunderPartialVer.md
Model: None

---

## Summary  
Best‑of‑Evidence (BoE) tackles the limitation of Best‑of‑N (BoN) by operating under partial verification, where only fragments of a response can be checked without a full verifier. The authors propose an inference‑time selection framework that retains a fixed candidate pool and allocates a limited budget to evidence actions represented as signed edges in a factor graph. This controller updates candidate probabilities based on observed evidence while preserving the original BoN decision when no budget is spent, thereby recovering BoN’s behavior in the zero‑budget case. The work demonstrates that residual evidence capacity imposes theoretical limits and that shared queries can achieve logarithmic query complexity instead of linear.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- Introduces Best‑of‑Evidence (BoE) as an inference‑time selection framework for partial verification tasks.  
- Formalizes candidate selection with a signed candidate–factor graph, allocating a budget to evidence actions and achieving O(log K) versus Θ(K) query separation in factor‑code models.  
- Empirically shows BoE improves fixed‑pool medical VQA performance and reveals the channel‑quality and candidate‑generation limits that prevent universal gains.

## Methodology  
The authors model each reusable claim as a node in a factor graph, with edges encoding evidence pieces that support or contradict the node. A limited budget is allocated to query these signed factors; a greedy score‑based controller updates the posterior probabilities of candidates by incorporating the evidence while keeping the pool unchanged. When the budget is zero, the controller reverts to the original BoN decision, providing a principled bridge between full verification and partial verification.

## Results  
On four medical VQA benchmarks, BoE consistently outperforms BoN when evidence is reliable and decision‑relevant, achieving up to 12 % absolute improvement in fixed‑pool selection. Theoretical analysis confirms that residual evidence capacity limits any further improvement and that shared factor queries reduce query complexity from Θ(K) to O(log K). However, gains diminish under noisy or irrelevant evidence, highlighting practical constraints.

## Significance  
This work bridges the gap between BoN’s assumption of full verification and real‑world partial data, offering a principled way to allocate scarce evidence actions. By improving fixed‑pool selection without expanding candidate generation, BoE enhances robustness in settings where only fragments of responses can be verified, thereby advancing both theory and practice in inference‑time selection.

## Related Concepts  
- Best‑of‑N (BoN)  
- Factor graphs  
- Signed evidence  
- Inference‑time selection  
- Partial verification  
- Medical VQA  
- Evidence budget  
- Query complexity  
- Residual capacity limits
