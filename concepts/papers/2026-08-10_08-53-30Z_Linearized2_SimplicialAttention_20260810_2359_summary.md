# Summary: 2026-08-10_08-53-30Z_Linearized2_SimplicialAttention.md
Saved: 2026-08-10 23:59
Source: 2026-08-10_08-53-30Z_Linearized2_SimplicialAttention.md
Model: None

---

## Summary  
The authors propose a linearized version of 2‑simplicial attention that transforms the original trilinear score into an inner product between a composite query and a key, thereby allowing the sum over one token axis to resemble ordinary softmax attention. By approximating this sum with positive random features and storing the entire past in a fixed‑size state while keeping only a short window of recent tokens explicit, they achieve linear cost in sequence length without sacrificing global reach. The approach eliminates the need for full softmax attention entirely when combined with Kimi Delta Attention. Experiments show that under matched compute this model attains the highest mean downstream accuracy and reduces LAMBADA perplexity from 715.6 to 602.6 at a 16 k context length.

## Key Contributions  
- [Finding 1] The trilinear score is rewritten as an inner product between a composite query and a key, enabling a linear‑time attention formulation.  
- [Finding 2] Positive random features approximate the sum over one axis, while a fixed‑size state holds the past and only a short window of recent tokens remains explicit.  
- [Finding 3] The method yields the highest mean downstream accuracy among compared architectures and improves LAMBADA perplexity from 715.6 to 602.6 at 16 k context.

## Methodology  
The authors start with the standard 2‑simplicial attention score, which is a trilinear function of query, key, and value tensors over three token axes. They collapse one axis into an inner product by defining a composite query that combines the first two tokens’ information, leaving only the third axis to be summed explicitly. To keep computation linear, they replace the exact sum with positive random features sampled from a fixed distribution, allowing the past to be represented in a constant‑size state vector. The second token axis is processed over a short window using Kimi Delta Attention, which adds local interaction without full softmax. Custom Triton kernels implement these operations for high throughput.

## Results  
Under matched compute with other architectures, the linearized 2‑simplicial attention model achieves the highest mean downstream accuracy across benchmarks. At a sequence length of 16 k tokens, it outperforms a Kimi Delta Attention hybrid while lowering LAMBADA perplexity from 715.6 to 602.6, demonstrating both speed and quality gains.

## Significance  
This work bridges the gap between global attention reach and linear computational cost, offering a scalable alternative to full softmax attention that is especially valuable for long‑context models where memory and latency are constraints. By enabling no‑softmax architectures, it opens new design space for efficient large language models.

## Related Concepts  
2‑simplicial attention, trilinear score, inner product formulation, positive random features, fixed‑size state representation, windowed attention, Kimi Delta Attention, LAMBADA perplexity, mean downstream accuracy.
