# Summary: 2026-08-06_17-09-46Z_TheTamedSubgradientUnadjustedLangevinAlgorithmbeyo.md
Saved: 2026-08-06 23:07
Source: 2026-08-06_17-09-46Z_TheTamedSubgradientUnadjustedLangevinAlgorithmbeyo.md
Model: None

---

## Summary  
The paper proposes the Subgradient Tamed Unadjusted Langevin Algorithm (SG‑TULA), a discretisation of the unadjusted Langevin diffusion that operates directly on subgradients without requiring costly smoothing. It is designed for sampling from non‑convex, superlinear‑growth potentials such as those encountered in large language model pretraining. The authors derive explicit non‑asymptotic convergence bounds in Wasserstein‑2 distance and provide excess‑risk estimates for the associated optimisation problem. Their work also verifies that the assumptions hold for the regularised pretraining potential of a GPT‑2 lineage LLM, showing SG‑TULA can be competitive with standard AdamW and Muon fine‑tuning.

## Key Contributions  
- [Finding 1] The authors obtain non‑asymptotic Wasserstein‑2 convergence rates for SG‑TULA, expressing all constants explicitly in terms of the problem dimension and inverse temperature.  
- [Finding 2] They derive explicit excess‑risk bounds that quantify how far the sampled distribution deviates from the true target under the same parameters.  
- [Finding 3] The paper confirms that the pretraining potential used for GPT‑2 lineage LLMs satisfies the required regularity conditions, enabling SG‑TULA to achieve performance comparable to AdamW and Muon without additional smoothing.

## Methodology  
The methodology centres on a direct discretisation of Langevin diffusion applied to subgradients. Instead of approximating the gradient with smooth functions, SG‑TULA uses taming techniques that stabilise the stochastic updates when the underlying potential grows superlinearly. The algorithm proceeds by generating a subgradient at each step, applying a tamed correction derived from the inverse temperature and dimension, then performing an unadjusted Langevin move. This approach avoids the need for expensive smoothing or second‑order approximations while preserving the diffusion dynamics that guarantee ergodicity.

## Results  
Theoretically, SG‑TULA converges to the target distribution with a Wasserstein‑2 error bounded by \(C \sqrt{\frac{d}{\beta}} e^{-\lambda t}\) where \(d\) is the dimension, \(\beta\) the inverse temperature, and \(\lambda>0\) depends on the subgradient growth rate. The excess risk of the optimisation problem is also bounded by a term proportional to \(\|g\|_2^2 / \beta\). Empirically, when pretraining GPT‑2 lineage models with SG‑TULA, the resulting language quality and downstream performance match or exceed that of AdamW fine‑tuning and Muon fine‑tuning, despite using only subgradient information. No comparable non‑asymptotic guarantees are currently available for these methods.

## Significance  
SG‑TULA bridges a longstanding gap in stochastic optimisation: it provides stable, explicit convergence analysis for subgradient Langevin schemes even when the potential is non‑convex and superlinear. This theoretical foundation removes reliance on costly smoothing, making large‑scale pretraining of LLMs more efficient and scalable. Moreover, the verification against real LLM potentials demonstrates practical relevance, offering a viable alternative to conventional AdamW or Muon fine‑tuning that could be integrated into future training pipelines.

## Related Concepts  
- Subgradient‑based Langevin algorithm  
- Unadjusted Langevin algorithm (ULA)  
- Taming techniques for superlinear gradients  
- Wasserstein‑2 convergence rates  
- Excess risk bounds  
- Regularised pretraining potential of LLMs  
- AdamW and Muon fine‑tuning methods
