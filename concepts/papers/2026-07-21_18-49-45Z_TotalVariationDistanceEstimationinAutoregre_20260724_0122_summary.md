# Summary: 2026-07-21_18-49-45Z_TotalVariationDistanceEstimationinAutoregressiveMo.md
Saved: 2026-07-24 01:22
Source: 2026-07-21_18-49-45Z_TotalVariationDistanceEstimationinAutoregressiveMo.md
Model: None

---

## Summary  
The paper addresses the challenge of estimating the total variation (TV) distance between two length‑$n$ autoregressive token distributions to an additive error $\varepsilon$, highlighting that practical inference implementations can produce different marginals even when the underlying weights are identical. It introduces three access models—sample, logit, and noisy logit—and derives query‑complexity bounds for each, showing a substantial improvement over prior work. The authors also provide empirical evidence by measuring the TV distance between SGLang and vLLM serving the same model, demonstrating that the theoretical guarantees hold in real deployments. This work bridges theory and practice, offering estimable distances even when KL divergence is infinite.

## Key Contributions  
- [Finding 1] The authors achieve a $\widetilde{O}(n^2 K/\varepsilon^2)$ query estimator under sample access, which outperforms Meel et al.’s $\widetilde{O}(n^3 m/\varepsilon^5)$ bound by reducing the dependence on the full token alphabet size $m$.  
- [Finding 2] Under logit access they prove a tight $O(n/\varepsilon^2)$ query complexity, establishing optimal asymptotic performance for this regime.  
- [Finding 3] For noisy logit access with relative error $\sigma$, they present a smooth interpolation yielding $\widetilde{O}((n+n^2\sigma^2)/\varepsilon^2)$ queries, bridging the gap between sample and logit regimes.

## Methodology  
The study begins by formalizing the total variation distance as an additive‑error problem: given two autoregressive distributions $p$ and $q$, estimate $\|p-q\|_{TV}$ within $\varepsilon$. The authors consider three realistic access scenarios. In **sample access**, they query the next‑token distribution at each position, leveraging the maximum support $K$ to bound the number of needed queries. For **logit access**, they sample logits directly and use a standard concentration argument to achieve the claimed bound. When values are noisy with relative error $\sigma$, they combine both approaches, deriving a hybrid query count that interpolates between the two extremes.

## Results  
Theoretically, the authors present three distinct complexity results: (1) $O(n^2 K/\varepsilon^2)$ queries for sample access; (2) $O(n/\varepsilon^2)$ queries for logit access; and (3) $\widetilde{O}((n+n^2\sigma^2)/\varepsilon^2)$ for noisy logit. Empirically, they run the estimators on SGLang and vLLM serving identical weights, confirming that the measured TV distance aligns closely with the theoretical estimates across various $\varepsilon$ values.

## Significance  
Estimating total variation distance matters because it quantifies how different inference engines may output distinct token distributions despite sharing the same model. The work shows that this quantity remains estimable even when KL divergence diverges, offering a robust metric for comparing deployment choices. By providing tighter query bounds and practical algorithms, the research enables more reliable monitoring of model behavior in production environments.

## Related Concepts  
- Total variation distance ($\|p-q\|_{TV}$)  
- Autoregressive token distributions  
- Sample access vs. logit access  
- Noisy logit access with relative error $\sigma$  
- Additive error $\varepsilon$ estimation  
- Meel et al.’s $O(n^3 m/\varepsilon^5)$ estimator (2025)
