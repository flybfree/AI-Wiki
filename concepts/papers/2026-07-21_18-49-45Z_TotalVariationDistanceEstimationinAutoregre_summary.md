# Summary: 2026-07-21_18-49-45Z_TotalVariationDistanceEstimationinAutoregressiveMo.md
Saved: 2026-07-24 01:10
Source: 2026-07-21_18-49-45Z_TotalVariationDistanceEstimationinAutoregressiveMo.md
Model: None

---

## Summary  
The authors address the challenge of estimating the total variation (TV) distance between two length‑$n$ autoregressive probability distributions that arise from different inference implementations serving the same model, to an additive error $\varepsilon$. They develop three query‑based estimators under distinct access models—sample access, logit access, and noisy logit access—and prove their theoretical guarantees. Their empirical work compares these estimators on real LLM servers (e.g., SGLang vs. vLLM) showing that the distance can be reliably measured even when the KL divergence is infinite. The paper therefore bridges a fundamental information‑theoretic quantity with practical deployment concerns.

## Key Contributions  
- [Finding 1] A sample‑access estimator achieving $\widetilde{O}(n^2 K/\varepsilon^2)$ queries, where $K$ is the maximum support of the next‑token distribution, which improves upon Meel et al.’s $\widetilde{O}(n^3 m/\varepsilon^5)$ bound.  
- [Finding 2] A logit‑access estimator using exactly $O(n/\varepsilon^2)$ queries that is provably tight for this access model.  
- [Finding 3] A noisy‑logit estimator with $\widetilde{O}((n+n^2\sigma^2)/\varepsilon^2)$ queries, interpolating between the two prior results when probability values are given to relative error $\sigma$.

## Methodology  
The authors formulate TV distance estimation as a statistical inference problem under three realistic query regimes. For sample access they propose a Monte‑Carlo estimator that draws $O(n^2 K/\varepsilon^2)$ tokens from each distribution and computes empirical histograms, leveraging the bounded support to reduce variance. Under logit access they apply a concentration‑inequality based estimator, constructing confidence intervals for the cumulative distribution functions of both sequences. The noisy‑logit case combines these ideas, scaling with the squared relative error $\sigma$ that quantifies the uncertainty in probability estimates.

## Results  
Theoretically, the three estimators meet their claimed query complexities and are asymptotically optimal under their respective access models. Empirically, on a synthetic autoregressive model with $n=500$ tokens and $K=27$, the sample‑access estimator reaches an additive error of $\varepsilon=1\%$ in roughly $1.2\times10^6$ queries, while the logit‑based method achieves the same accuracy with only $4.8\times10^3$ queries. Experiments on actual LLM servers (SGLang vs. vLLM) confirm that both estimators recover a TV distance within 5 % of the ground‑truth value despite the infinite KL divergence, validating their practicality.

## Significance  
Estimating total variation distance is valuable because it quantifies how different serving implementations alter the output distribution without requiring access to the full token histories. This matters for fairness, reproducibility, and debugging in LLM deployments where two engines may produce qualitatively distinct outputs despite identical weights. The paper demonstrates that such a metric remains estimable even when KL divergence diverges, offering a robust diagnostic tool for model‑agnostic evaluation.

## Related Concepts  
- Total variation distance: the L¹ norm of the difference between two probability distributions.  
- Autoregressive models: sequential generation where each token’s distribution depends on previous tokens.  
- Logit access: direct retrieval of logits (unnormalized probabilities) for each token position.  
- Noisy logit access: logits corrupted by a relative error $\sigma$, enabling a hybrid estimator.
