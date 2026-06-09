# Summary: 2026-05-11_17-58-28Z_DECO_SparseMixture_of_ExpertswithDense_ComparableP.md
Saved: 2026-05-12 03:01
Source: 2026-05-11_17-58-28Z_DECO_SparseMixture_of_ExpertswithDense_ComparableP.md
Model: None

---


## Summary  
The paper proposes DECO, a sparse Mixture‑of‑Experts (MoE) architecture that delivers dense‑Transformer performance while using only 20 % of the experts and keeping total parameters constant. By introducing learnable expert‑wise scaling, ReLU‑based routing, and a new NormSiLU activation, DECO balances routed and shared contributions to achieve high accuracy with minimal storage overhead. The design also includes an optimized acceleration kernel that yields a three‑fold speedup on real hardware compared with dense inference. This work bridges the gap between theoretical MoE scalability and practical end‑side deployment constraints.

## Key Contributions  
- Finding 1: DECO matches dense Transformer performance under identical total parameter budgets, proving that sparsity does not sacrifice accuracy.  
- Finding 2: The learnable expert‑wise scaling combined with ReLU routing stabilizes activation ratios and enables a higher intrinsic sparsity level than standard gated MoE methods.  
- Finding 3: Empirically, non‑gated MLP experts with ReLU routing outperform conventional gated MoE baselines while reducing computational complexity.

## Methodology  
DECO tackles the storage‑and‑memory bottleneck of dense MoEs by activating only a fraction of experts at inference time. The authors employ differentiable ReLU‑based routing, where each token is assigned to a subset of experts via learnable weights that adapt during training. To further improve stability and sparsity, they introduce NormSiLU: an activation function that normalizes inputs before applying SiLU, smoothing the distribution of expert activations. Crucially, they adopt non‑gated MLP experts, simplifying the architecture while preserving performance. An acceleration kernel is built to exploit hardware parallelism, delivering a 3× speedup on real devices.

## Results  
Experiments show that DECO activates just 20 % of its expert pool and attains BLEU scores indistinguishable from dense Transformers trained with the same total parameter count. It also surpasses state‑of‑the‑art MoE baselines such as Switch Transformer and GLaM in both accuracy and latency. On a typical GPU, DECO inference runs three times faster than dense inference while using half the memory footprint.

## Significance  
DECO demonstrates that sparse MoE models can be deployed efficiently on end‑side devices without sacrificing performance or storage efficiency. By reducing parameter count and memory access, it enables large‑scale language services in resource‑constrained environments such as mobile phones and edge servers.

## Related Concepts  
- Mixture-of-Experts (MoE)  
- Sparse routing  
- ReLU‑based routing  
- Learnable expert scaling  
- NormSiLU activation function  
- Dense vs. sparse inference  
- Acceleration kernels

[[2026-05-11_17-58-28Z_DECO_SparseMixture_of_ExpertswithDense_ComparableP.md]]