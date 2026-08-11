# Summary: 2026-08-09_10-20-20Z_UniMoMo_ExpertMerging_BasedMoEAccelerationforLarge.md
Saved: 2026-08-10 23:16
Source: 2026-08-09_10-20-20Z_UniMoMo_ExpertMerging_BasedMoEAccelerationforLarge.md
Model: None

---

## Summary  
UniMoMo is a post‑training compression framework that reduces the expert bank of large recommendation MoE models to meet an explicit serving budget without requiring an online compression module. It treats the conversion problem as a constrained graph coarsening task, grouping experts based on functional similarity measured from an unlabeled calibration set. The method also includes a layer‑adaptive protection mechanism that prevents merging high‑traffic experts, preserving routing efficiency. Experiments show that the resulting four‑expert checkpoints retain or improve source‑relative NDCG@10 while delivering A100 speedups of up to 2.2×.

## Key Contributions  
- Introduces UniMoMo, a constrained graph coarsening framework for MoE compression.  
- Uses an unlabeled calibration set to measure expert functional similarity rather than parameter distance.  
- Implements layer‑adaptive protection that restricts merging of high‑traffic experts based on routing exposure.

## Methodology  
The authors formulate the conversion problem as a graph coarsening task: each MoE checkpoint is represented as a graph whose nodes are experts and edges encode functional similarity derived from calibration responses. The goal is to compress this graph into a smaller expert bank under a fixed budget while applying adaptive protection that limits merges of high‑traffic experts. The compressed model is then exported with reduced experts and adapted routing tables, enabling deployment on standard hardware.

## Results  
On Amazon Beauty (2 MoE blocks), KuaiRec (4 blocks) and TenRec (6 blocks), four‑expert checkpoints achieve source‑relative NDCG@10 ratios of 99.92%–102.30% with A100 speedups ranging from 1.28× to 1.63×. An aggressive two‑expert, top‑1 operating point yields ratios of 98.36%–104.24% and speedups up to 2.21×, demonstrating that expert merging can both reduce resource usage and improve performance.

## Significance  
UniMoMo enables the deployment of large recommendation MoE models at limited serving budgets by shrinking their memory footprint and compute requirements without introducing online compression components. The framework demonstrates that expert‑merging strategies can yield tangible efficiency gains while maintaining or enhancing recommendation quality, offering a practical solution for scalable model serving.

## Related Concepts  
Mixture‑of‑Experts (MoE), post‑training compression, graph coarsening, functional similarity, routing exposure, NDCG@10, A100 speedup.
