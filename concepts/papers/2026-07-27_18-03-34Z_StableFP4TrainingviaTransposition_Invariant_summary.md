# Summary: 2026-07-27_18-03-34Z_StableFP4TrainingviaTransposition_InvariantBlockQu.md
Saved: 2026-07-28 22:22
Source: 2026-07-27_18-03-34Z_StableFP4TrainingviaTransposition_InvariantBlockQu.md
Model: None

---

## Summary  
The paper tackles the instability that limits training at 4‑bit floating point (FP4) precision by showing that existing microscaling techniques produce biased gradients when tensors are transposed. Its contribution is a low‑precision framework based on 2D block quantization that enforces transposition‑invariant scaling, uses truncation‑free scaling and stochastic rounding to bound error, and pairs this with MXFP8 for attention projections. The approach enables stable end‑to‑end FP4 training of large dense LLMs and MoE models while matching BF16 performance.

## Semantic links
- [[concepts/papers/2026-07-23_21-53-34Z_ToolGuardian_DeclarativeSecurityforAIAgent__summary.md|Summary: 2026-07-23_21-53-34Z_ToolGuardian_DeclarativeSecurityforAIAgent_ToolInt.md]] — 3 title terms overlap; 1 backlink; 9 summary/topic terms overlap
- [[concepts/papers/2026-08-03_10-33-34Z_ConvexNeuralEnergyElements_MonolithicFinite_20260804_0045_summary.md|Summary: 2026-08-03_10-33-34Z_ConvexNeuralEnergyElements_MonolithicFinite_Elemen.md]] — 3 title terms overlap; 15 summary/topic terms overlap; semantic match 0.10

## Key Contributions  
- [Finding 1] Identify scale inconsistency caused by tensor transposition in 1D block quantization leading to biased gradient updates.  
- [Finding 2] Introduce 2D block FP4 quantization that enforces consistent scaling forward and backward regardless of transposition, using truncation‑free scaling and stochastic rounding.  
- [Finding 3] Combine the 2D block method with MXFP8 for attention projections to maintain a practical mixed‑precision design.

## Methodology  
The authors analyze how transposition changes scaling factors in conventional 1D blocks, which results in different scales for identical values during forward and backward passes. To remedy this, they replace 1D blocks with independent 2D blocks where each block is quantized to FP4 using truncation‑free scaling, ensuring the same value retains its scale across both directions. Stochastic rounding is applied to bound quantization error, while MXFP8 is used for query and key projections in attention mechanisms.

## Results  
Experiments on dense LLMs up to 7 B parameters and a 30 B MoE model trained on up to 100 B tokens demonstrate stable training throughout. Compared with BF16 baselines, the FP4 method achieves perplexity degradation of less than 1.3% and maintains near‑identical downstream accuracy, confirming that scaling consistency is sufficient for practical large‑scale training.

## Significance  
Enforcing forward‑backward scaling consistency unlocks feasible FP4 training at scale, dramatically reducing memory and compute costs while preserving performance—a critical step toward more efficient LLM deployment.

## Related Concepts  
FP4 (4‑bit floating point), microscaling quantization, transposition‑invariant scaling, truncation‑free scaling, stochastic rounding, MXFP8 mixed precision, block quantization, attention projection scaling.
