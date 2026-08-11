# Summary: 2026-08-09_10-20-20Z_UniMoMo_ExpertMerging_BasedMoEAccelerationforLarge.md
Saved: 2026-08-10 23:19
Source: 2026-08-09_10-20-20Z_UniMoMo_ExpertMerging_BasedMoEAccelerationforLarge.md
Model: None

---

## Summary  
The paper proposes UniMoMo, a post‑training compression framework that converts large recommendation MoE checkpoints into smaller expert banks while preserving performance. It does so by grouping experts based on functional similarity using an unlabeled calibration set and protecting high‑traffic experts with a layer‑adaptive mechanism.

## Key Contributions  
- Finding 1: UniMoMo formulates the conversion problem as a constrained graph coarsening task, enabling expert merging without adding compression‑specific online modules.  
- Finding 2: The method uses an unlabeled calibration set to measure functional similarity between experts, allowing grouping based on how they respond to shared recommendation states rather than parameter distance.  
- Finding 3: A layer‑adaptive protection mechanism restricts merging of high‑traffic experts, preventing performance degradation and preserving routing efficiency.

## Methodology  
The authors treat the MoE checkpoint as a graph where nodes are experts and edges represent functional similarity. They compute similarity scores using calibration data, then apply graph coarsening to merge clusters while respecting an expert budget. The protection mechanism monitors routing exposure per layer and blocks merges that would increase latency or degrade NDCG for high‑traffic experts.

## Results  
On Amazon Beauty, KuaiRec, and TenRec with 2–6 MoE blocks, UniMoMo converts checkpoints to four‑expert models achieving source‑relative five‑run mean NDCG@10 ratios of 99.92%–102.30%, outperforming the original by up to 2.3%. A two‑expert aggressive setting yields ratios of 98.36%–104.24% with speedups of 1.47×–2.21× on A100 GPUs, demonstrating both compression and inference acceleration.

## Significance  
UniMoMo bridges the gap between large‑scale recommendation models and resource‑constrained serving environments by enabling export at multiple expert budgets without sacrificing quality or speed. Its graph‑coarsening perspective offers a principled way to balance functional similarity with traffic constraints, paving the way for scalable deployment of MoE systems.

## Related Concepts  
- Mixture-of-Experts (MoE) architectures  
- Post‑training compression and model distillation  
- Graph coarsening and clustering  
- Expert budgeting in large language models
