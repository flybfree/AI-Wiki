# Summary: 2026-07-29_10-54-46Z_BeyondKVReconstruction_FunctionalReconstructionfor.md
Saved: 2026-07-30 22:15
Source: 2026-07-29_10-54-46Z_BeyondKVReconstruction_FunctionalReconstructionfor.md
Model: None

---

## Summary  
The paper tackles the challenge of converting multi‑head attention (MHA) or grouped‑query attention (GQA) models to multi‑head latent attention (MLA) so that speculative decoding can reuse compact KV caches without retraining from scratch. Direct conversion, which merely factorises the attention matrix and applies RoPE, introduces errors that degrade draft‑token acceptance in verification. To mitigate this, the authors introduce functional reconstruction—a converter‑agnostic, end‑to‑end method that optimizes each MLA module to reproduce the original MHA/GQA output on calibration hidden states. This approach preserves the cached attention graph and inference pipeline while requiring no verifier logits or supervision.

## Key Contributions  
- [Finding 1] Direct conversion of MHA/GQA to MLA sharply reduces draft‑token agreement because low‑rank factorisation and RoPE handling corrupt the attention function, which is tolerable for standalone generation but harmful for speculative decoding.  
- [Finding 2] Functional reconstruction materially improves acceptance in 37 out of 64 matched task cells (within a 0.5 percentage‑point reporting tolerance), leaving 26 unchanged and decreasing one, demonstrating its effectiveness across diverse configurations.  
- [Finding 3] The method is converter‑agnostic: it retains the original cache and inference graph, eliminating the need for verifier supervision or additional logits.

## Methodology  
The authors formulate MLA draft construction as a functional reconstruction problem. For each converted attention module they optimise parameters so that the post‑output projection matches the response of its original MHA/GQA counterpart on a set of calibration hidden states, using gradient‑based training. The procedure is applied to 192 distinct model‑converter‑backend‑method‑task configurations spanning four Llama/Qwen draft‑target pairs (TransMLA and MHA2MLA) evaluated on four 200‑prompt tasks.

## Results  
Across the full experiment, Functional Reconstruction yields a statistically significant gain: it improves acceptance in 37 task cells, leaves 26 essentially unchanged, and reduces one cell. The improvement is measured relative to the baseline conversion method with a tolerance of ±0.5 percentage points. No other configuration showed a net loss; the overall impact on speculative decoding speed is positive.

## Significance  
By decoupling cache compression from attention fidelity, functional reconstruction enables high‑throughput inference for MLA models in speculative decoding pipelines without retraining or sacrificing verification accuracy. This bridges the gap between memory‑efficient caching and reliable draft generation, potentially accelerating LLM deployment at scale.

## Related Concepts  
- Multi‑head latent attention (MLA)  
- Grouped‑query attention (GQA)  
- Speculative decoding  
- KV cache compression  
- Functional reconstruction  
- Calibration hidden states  
- Low‑rank factorisation  
- RoPE handling
