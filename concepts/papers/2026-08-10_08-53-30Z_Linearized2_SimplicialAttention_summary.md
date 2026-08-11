# Summary: 2026-08-10_08-53-30Z_Linearized2_SimplicialAttention.md
Saved: 2026-08-10 23:43
Source: 2026-08-10_08-53-30Z_Linearized2_SimplicialAttention.md
Model: None

---

## Summary  
The authors propose a linearized version of 2‑simplicial attention that rewrites the trilinear score into an inner product between a composite query and a key, thereby allowing the sum over one token axis to resemble ordinary softmax attention. By approximating this sum with positive random features and storing only a fixed‑size state for the past while keeping a short window of recent tokens explicit, they achieve linear cost in sequence length without sacrificing global reach. The method is implemented using custom Triton kernels and combined with Kimi Delta Attention to produce a model that contains no softmax attention at all. Under matched compute, this architecture attains the highest mean downstream accuracy among compared models and reduces LAMBADA perplexity from 715.6 to 602.6 at a 16k context window.

## Key Contributions  
- [Finding 1] The linearized formulation of 2‑simplicial attention converts the trilinear score into an inner product, enabling a softmax‑like sum over one axis.  
- [Finding 2] Approximation with positive random features and a fixed‑size past state yields linear sequence‑length cost while preserving global context.  
- [Finding 3] Integration with Kimi Delta Attention eliminates the need for explicit softmax attention, producing a fully linear architecture.

## Methodology  
The authors first decompose the original 2‑simplicial attention score into two inner products: one between a query and a key that spans the entire sequence, and another between a composite query and a key limited to recent tokens. The sum over the past dimension is approximated by sampling positive random features, which are stored in a compact state vector. This state is updated per token, while the short‑window key remains explicit. Triton kernels execute these inner products efficiently on GPU hardware. The resulting module is fused with Kimi Delta Attention, which also relies on linear operations, so no softmax computation occurs anywhere in the pipeline.

## Results  
Experiments compare the proposed linearized 2‑simplicial attention against standard softmax attention and a hybrid KDA model across several downstream tasks (e.g., LAMBADA, GLUE). The linear architecture achieves the highest mean accuracy among all models under matched compute. At a context length of 16k tokens, its perplexity drops from 715.6 to 602.6, outperforming the KDA hybrid in both absolute and relative terms. Ablation studies confirm that the random‑feature approximation is sufficient for the desired accuracy while maintaining linear cost.

## Significance  
By replacing costly softmax operations with linear inner products and a fixed‑size state, the paper demonstrates that global attention can be approximated without sacrificing performance. This reduces memory usage and inference latency, making large‑scale language models more scalable. The work also highlights how simple feature‑based approximations can replace full attention mechanisms, opening avenues for further research into lightweight, linear attention variants.

## Related Concepts  
- 2‑simplicial attention: a higher‑order generalization of softmax attention that uses trilinear scores.  
- Linearized attention: rewriting multi‑head attention as inner products to achieve O(L) cost.  
- Positive random features: stochastic approximations used for fast, linearizable attention.  
- Kimi Delta Attention: another linear attention variant that eliminates softmax computation.  
- Triton kernels: high‑performance GPU execution primitives employed in the implementation.
