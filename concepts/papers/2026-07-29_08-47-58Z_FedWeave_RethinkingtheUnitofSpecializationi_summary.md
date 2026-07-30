# Summary: 2026-07-29_08-47-58Z_FedWeave_RethinkingtheUnitofSpecializationinHetero.md
Saved: 2026-07-29 20:30
Source: 2026-07-29_08-47-58Z_FedWeave_RethinkingtheUnitofSpecializationinHetero.md
Model: None

---

## Summary  
FedWeave tackles the problem of task heterogeneity in federated MoE‑LoRA by separating expert aggregation from router optimization. It introduces asymmetric aggregation so that experts receive pure, pattern‑coherent updates while routers benefit from mixed‑task observations to maintain contrast. The framework uses unsupervised prototype discovery to form local buckets and align them across clients, enabling prototype‑level expert aggregation without sacrificing soft‑routing performance. At inference it activates a single expert per request, achieving sparsity while preserving near‑full routing accuracy.

## Key Contributions  
- Asymmetric aggregation separates the responsibilities of experts (purity) and routers (contrast), eliminating cross‑task interference.  
- Unsupervised prototype discovery creates local buckets that are aligned across clients, allowing prototype‑level expert aggregation.  
- The framework enables sparse inference with one active expert while retaining near‑full soft‑routing performance.

## Methodology  
FedWeave adopts heterogeneous federated MoE‑LoRA where each client may handle different tasks. Existing methods specialize at the client level, causing interference between tasks. FedWeave’s core idea is to treat experts and routers as distinct units: experts aggregate only their own pattern‑coherent updates (purity), while routers optimize based on a contrastive view of mixed observations. Unsupervised prototype discovery generates local buckets that are then aligned across clients, producing a shared representation for router training. During inference the system activates a single expert per request, achieving sparsity and preserving soft‑routing efficiency.

## Results  
Theoretical analysis shows that asymmetric aggregation limits expert convergence to stationary updates by removing off‑pattern contamination; it also bounds consensus error from fragmented router trajectories and sparse‑inference risk. Experiments on a heterogeneous multi‑task benchmark with mainstream LLM backbones demonstrate that FedWeave outperforms strong baselines, achieving higher task‑specific accuracy while maintaining soft‑routing efficiency. Ablations confirm that prototype discovery is essential for bucket alignment.

## Significance  
This work redefines the unit of specialization in federated MoE‑LoRA, moving from client‑level to expert‑level purity and router contrast, enabling efficient personalization across diverse tasks without compromising privacy. It provides a scalable solution for large‑scale heterogeneous federated learning where task diversity is high.

## Related Concepts  
- Federated PEFT (Federated Parameter-Efficient Fine-Tuning)  
- LoRA (Low‑Rank Adaptation)  
- MoE (Mixture of Experts)  
- Heterogeneous federated learning  
- Asymmetric aggregation  
- Unsupervised prototype discovery  
- Soft routing
