# Summary: 2026-07-23_04-49-38Z_Three_ProngedSpectralControlforFederatedParameterE.md
Saved: 2026-07-24 02:27
Source: 2026-07-23_04-49-38Z_Three_ProngedSpectralControlforFederatedParameterE.md
Model: None

---

## Summary  
Federated parameter‑efficient fine‑tuning (PEFT) aims to adapt large pretrained models on edge devices while minimizing communication, yet its performance degrades when clients have heterogeneous data distributions. The proposed TRISHUL framework addresses this fragility by controlling the spectral alignment of low‑rank adaptation updates across federated rounds. It does so without altering the underlying FL protocol and adds negligible computation or extra communication overhead. Our experiments show that TRISHUL yields faster, more stable convergence and higher final accuracy than standard federated LoRA baselines, especially under strong client heterogeneity.

## Key Contributions  
- [Finding 1] TRISHUL achieves algebraically exact aggregation of compact core updates using shared frozen multi‑head low‑rank bases.  
- [Finding 2] Nuclear norm proximal shrinkage selectively suppresses high‑rank, client‑specific spectral components before upload.  
- [Finding 3] Adaptation heads are allocated non‑uniformly across layers via a concave water‑filling budget derived from pretrained layer capacity.

## Methodology  
TRISHUL operates within the FL no‑raw-data-sharing setting and reuses the standard multi‑head PEFT pipeline. First, a set of low‑rank bases is frozen globally; each client computes its local adaptation matrix on these bases. The framework then applies nuclear norm proximal shrinkage to the resulting core matrices, which eliminates high‑variance spectral components while preserving useful low‑rank information. Finally, a concave water‑filling allocation distributes adaptation heads across layers based on their intrinsic capacity, ensuring efficient use of the limited communication budget.

## Results  
Across vision benchmarks (CIFAR‑100, SVHN) and language tasks (20 Newsgroups, MRQA), TRISHUL improves convergence speed by up to 30 % and final accuracy by 4–6 % compared with federated LoRA. On GLUE with LLaMA3.2‑1B, gains reach 5 % higher F1 scores on average. The improvements are most pronounced when client data distributions differ markedly, confirming robustness to heterogeneity.

## Significance  
TRISHUL demonstrates that spectral control can be integrated seamlessly into federated PEFT without sacrificing efficiency or privacy guarantees. By reducing variance in aggregated updates and optimizing head allocation, it enables scalable adaptation on resource‑constrained edge devices while preserving the communication advantages of PEFT.

## Related Concepts  
- Federated learning (FL)  
- Parameter‑efficient fine‑tuning (PEFT)  
- Low‑rank adaptation (LoRA)  
- Spectral alignment / low‑rank subspace control  
- Nuclear norm proximal shrinkage  
- Concave water‑filling allocation
