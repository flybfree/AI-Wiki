# Summary: 2026-08-02_18-02-03Z_ReusingRolloutsunderPolicyLag_Prefix_NormalizedPol.md
Saved: 2026-08-03 23:32
Source: 2026-08-02_18-02-03Z_ReusingRolloutsunderPolicyLag_Prefix_NormalizedPol.md
Model: None

---

## Summary  
The paper tackles the computational bottleneck of autoregressive rollout generation in large‑language‑model reinforcement learning and proposes Prefix‑Normalized Policy Optimization (PNPO) to reuse each batch for multiple learner updates. By replacing the cumulative importance ratio with a geometric mean across causal prefixes, PNPO preserves prefix‑wise dependence while compressing the log‑weight scale. Experiments show that PNPO only improves performance when several policy updates are performed per rollout batch, especially under large off‑policy regimes. The method reduces sample cost and yields higher Avg@32 scores compared with single‑epoch alternatives such as GSPO.

## Key Contributions  
- [Finding 1] PNPO replaces the cumulative importance ratio with a geometric mean of likelihood ratios along each causal prefix.  
- [Finding 2] PNPO preserves causal‑prefix dependence at every token position while compressing the log‑weight scale.  
- [Finding 3] PNPO attains higher Avg@32 scores (up to +50.24) when four policy updates per rollout batch are used, outperforming GSPO and achieving a final macro Avg@32 of 49.66 with only 150 batches.

## Methodology  
The authors generate autoregressive rollouts for LLM agents, compute a prefix‑wise importance ratio using the geometric mean instead of a product, apply this ratio to the reinforcement‑learning loss, and perform either one or four policy updates per batch. They evaluate on long‑context mathematical reasoning benchmarks, varying the number of epochs (one or four) to induce two off‑policy regimes.

## Results  
With a single epoch PNPO does not consistently beat GSPO; however, with four epochs it reaches the highest Avg@32 among three independently selected benchmarks. The unweighted mean of the three peaks is 50.24, roughly 3 percentage points above GSPO’s score. Under a fixed budget of 2,400 updates, PNPO achieves a final macro Avg@32 of 49.66 after 150 rollout batches, comparable to the 49.56 obtained with 600 batches and one epoch.

## Significance  
This work demonstrates that reusing rollouts can be advantageous when training moves far off‑policy, offering a more efficient and effective way to update LLMs in reinforcement learning settings. By reducing compute cost while maintaining or improving performance, PNPO could enable larger models and longer training runs with limited resources.

## Related Concepts  
autoregressive rollout generation, importance ratio, cumulative importance, geometric mean, causal prefix, policy lag, off‑policy correction, Avg@32 metric, LLM reinforcement learning.
