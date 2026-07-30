# Summary: 2026-07-29_12-45-55Z_ReCo_ReweightingGRPOAgainstDistributionalConcentra.md
Saved: 2026-07-29 20:34
Source: 2026-07-29_12-45-55Z_ReCo_ReweightingGRPOAgainstDistributionalConcentra.md
Model: None

---

## Summary  
Group Relative Policy Optimization (GRPO) is widely used to fine‑tune large language models for reasoning tasks, yet recent experiments reveal that GRPO can concentrate updates on responses the base model already generates with high probability, thereby diminishing its ability to explore alternative reasoning paths. This concentration leads to a drop in Pass@k performance when the evaluation horizon k becomes large. The authors of ReCo identify two mechanisms driving this behavior: (1) response‑level dominance caused by repeated occurrence of frequent outputs, and (2) token‑level importance scaling that reinforces tokens that become more likely under the current policy. Their contribution is a reweighting technique called ReCo that mitigates both effects.

## Key Contributions  
- [Finding 1] GRPO’s response contributions are biased toward high‑probability outputs, causing an over‑representation of those responses in the group gradient.  
- [Finding 2] The token‑level importance ratio amplifies updates for tokens that become increasingly probable under the policy, further saturating decision points.  
- [Finding 3] ReCo normalizes response contributions to their expected occurrence and replaces the token importance ratio with a variance‑based scaling factor that favors less saturated choices.

## Methodology  
ReCo addresses both mechanisms by first computing, for each group rollout, the normalized contribution of every candidate response relative to its expected frequency among the group. This prevents any single frequent response from dominating the update. At the token level, instead of using a simple importance ratio that grows as a token’s probability rises, ReCo employs a variance‑based ratio that is large when alternative tokens remain plausible (i.e., low variance) and small when the decision point is saturated. The reweighted gradients are then applied to the policy network in the usual GRPO fashion.

## Results  
Across five mathematical reasoning benchmarks evaluated on Qwen2.5‑Math‑1.5B/7B and Llama‑3.1‑8B‑Instruct, ReCo consistently improves Pass@k for large values of k, showing a clear advantage over GRPO in these regimes. For small k the performance gap narrows, making ReCo comparable to baseline GRPO. The improvements are statistically significant (p < 0.01) and persist across different model sizes.

## Significance  
ReCo tackles a fundamental limitation of GRPO that hampers long‑range reasoning in large language models. By preventing distributional concentration at both response and token levels, the method preserves the model’s ability to explore diverse reasoning paths, which is crucial for tasks requiring extended chain‑of‑thought generation. This work therefore advances the state of post‑training RL by offering a simple yet effective correction that can be integrated into existing fine‑tuning pipelines.

## Related Concepts  
- Group Relative Policy Optimization (GRPO)  
- Distributional concentration in reinforcement learning updates  
- Response‑level dominance and its mitigation  
- Token‑level importance ratio scaling  
- Variance‑based scaling for exploration encouragement  
- Pass@k evaluation metric for reasoning tasks
