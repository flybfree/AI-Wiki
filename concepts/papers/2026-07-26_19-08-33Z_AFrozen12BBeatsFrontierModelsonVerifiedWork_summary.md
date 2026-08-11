# Summary: 2026-07-26_19-08-33Z_AFrozen12BBeatsFrontierModelsonVerifiedWork_100_Ac.md
Saved: 2026-07-27 22:46
Source: 2026-07-26_19-08-33Z_AFrozen12BBeatsFrontierModelsonVerifiedWork_100_Ac.md
Model: None

---

## Summary  
The paper proposes a system where a frozen 12 B language model answers verified problem instances without generating any tokens, using a persistent memory store of exact solutions. It demonstrates zero‑token inference with bit‑exact outputs across multiple problem families and architectures. The approach decouples performance from parameter scaling by relying on stored knowledge rather than computation. A public benchmark is provided for independent verification.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.05
- [[concepts/papers/2026-07-30_13-58-33Z_SecurityofWorld_Model_BasedEmbodiedAI_ALife_summary.md|Summary: 2026-07-30_13-58-33Z_SecurityofWorld_Model_BasedEmbodiedAI_ALifecycleof.md]] — 4 title terms overlap; 7 summary/topic terms overlap; semantic match 0.03

## Key Contributions  
- [Finding 1] A frozen 12 B model can answer new instances of a verified problem family with zero generation tokens, delivering bit‑exact and deterministic answers.  
- [Finding 2] The persistent memory enables sub‑millisecond selection (≈1.4 µs) and full reuse in 6–23 ms at 36 mWh, fitting within a 6 M‑token GPU window.  
- [Finding 3] Retrieval‑based solution fetching suffers from high error rates (94.3% wrong picks on a 4,500‑item store), highlighting the need for exact addressing.

## Methodology  
The authors keep the model frozen and maintain a verified memory of solutions that were solved independently without consulting an answer key. For each query they retrieve the most similar stored solution via approximate similarity search, then output its bit‑exact text. Verification is performed once per problem family before storage, ensuring trust in the retrieved content.

## Results  
Across 180 fresh instances from nine families and four architectures (dense and MoE), the system achieved 180/180 accuracy with zero generation tokens. A negative control without memory yields no capability. Open‑ended reasoning shows 88/88 consistency‑gated acceptances when solution retrieval is gated, and a formal proof is machine‑checked. Retrieval error rate is 94.3% on the store; vLLM caps at 30,399 tokens while SGLang silently truncates beyond 32,000.

## Significance  
This work shows that memory can be the primary resource for high‑accuracy inference, offering a cost‑free, parameter‑independent alternative to scaling model size. It challenges frontier models that always generate fresh answers, proving that verified reuse is superior on tasks it has already solved.

## Related Concepts  
frozen model, persistent memory store, verification contract, bit‑exact output, token‑free reuse, similarity retrieval, GPU memory window, vLLM/SGLang token limits, zero‑token inference, parameter scaling decoupling.
