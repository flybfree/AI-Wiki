# Summary: 2026-07-28_04-57-19Z_CoSA_AcceleratingLong_ContextInferenceviaProxy_Ker.md
Saved: 2026-07-28 22:31
Source: 2026-07-28_04-57-19Z_CoSA_AcceleratingLong_ContextInferenceviaProxy_Ker.md
Model: None

---

## Summary  
The paper tackles the quadratic cost of self‑attention in long‑context language models and introduces CoSA, a training‑free sparse attention framework that pairs a proxy‑kernel co‑design to boost accuracy at low budgets. It combines a Kernel‑Aware Proxy (KAP) that selects blocks under moderate constraints with an Ordered‑Skipping Kernel (OSK) that further skips blocks using online‑softmax statistics. Empirically, CoSA delivers higher perplexity preservation while dramatically reducing inference time and memory usage.

## Key Contributions  
- A two‑stage training‑free sparse attention framework that merges KAP and OSK for proxy‑kernel co‑design.  
- Empirical proof that CoSA yields higher accuracy at lower budgets compared with existing proxy‑kernel methods.  
- Demonstrated 4.93× speedup in attention computation and a 2.53× reduction in time‑to‑first‑token for a context length of 128 K, with negligible performance loss.

## Methodology  
The authors replace dense self‑attention with a sparse kernel that processes key‑value pairs in an ordered sequence. In Stage 1, the KAP generates an ordered mask constrained by a moderate budget, dictating the visitation order of KV pages to the OSK. In Stage 2, the OSK applies this mask and dynamically skips additional blocks using online‑softmax statistics derived from recent attention probabilities, tightening the budget further without manual tuning.

## Results  
Across LLaMA, Vicuna, WikiText10M and LongBench benchmarks, CoSA maintains or slightly improves perplexity while cutting memory consumption from O(N²) to O(N). It achieves a 4.93× faster attention throughput and a 2.53× lower time‑to‑first‑token at 128 K context length, with an accuracy drop of less than 0.2% perplexity increase.

## Significance  
CoSA resolves the classic sparsity‑accuracy trade‑off in long‑context inference, showing that proxy‑kernel co‑design can deliver scalable, high‑throughput models at low cost—critical for deploying massive LLMs on resource‑constrained hardware.

## Related Concepts  
- Self‑attention quadratic complexity  
- Block‑sparse attention  
- Proxy‑based sparse masks  
- Kernel parallelism  
- Online softmax statistics
