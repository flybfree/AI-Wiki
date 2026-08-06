# Summary: 2026-08-04_13-08-07Z_SJEPA_LearningElegantLatentDynamicswithHybridSymbo.md
Saved: 2026-08-05 23:11
Source: 2026-08-04_13-08-07Z_SJEPA_LearningElegantLatentDynamicswithHybridSymbo.md
Model: None

---

## Summary  
The paper proposes SJEPA, a reconstruction‑free joint‑embedding predictive architecture that learns latent dynamics with compact symbolic descriptions. It combines a symbolic law (grammar) with a regularised neural correction for states outside the grammar. The core idea is to minimise induced‑dynamics complexity while preserving informative predictive coordinates and avoiding representation collapse. SJEPA enables alternating learning of representations and symbols, or fitting symbols to fixed representations.

## Key Contributions  
- Finding 1: Joint embedding predicts target embeddings from context embeddings without explicit transition models.  
- Finding 2: The hybrid symbolic‑neural predictor induces dynamics with low complexity and avoids shortcuts that cause collapse.  
- Finding 3: Regularisation preserves the representable symbolic mechanism while guiding neural components to residual dynamics.

## Methodology  
SJEPA learns predictive representations by minimising a loss that balances symbolic parsimony (via grammar) and neural correction. The induced‑dynamics complexity is measured, and non‑identifiability of predictive coordinates is exploited. Two learning modes are supported: alternating representation‑equation learning where both symbols and embeddings are updated, and fixed‑representation fitting where only the transition model adapts.

## Results  
In pendulum experiments, SJEPA discovers simpler symbolic dynamics with lower long‑horizon rollout error and divergence compared to post‑hoc fitting. An unconstrained one‑step diagnostic reveals a shortcut that would cause representation collapse. When grammar is misspecified, correction regularisation keeps the symbolic mechanism intact.

## Significance  
By providing a controllable trade‑off among predictive fidelity, representation quality, symbolic parsimony, and allocation between symbols and neural components, SJEPA advances interpretable generative modelling and offers tools for diagnosing representation collapse.

## Related Concepts  
Joint embedding, latent dynamics, symbolic grammar, regularised correction, induced‑dynamics complexity, representation collapse shortcut, non‑identifiability of predictive coordinates.
