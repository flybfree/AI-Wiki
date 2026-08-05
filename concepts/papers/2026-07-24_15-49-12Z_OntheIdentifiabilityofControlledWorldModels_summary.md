# Summary: 2026-07-24_15-49-12Z_OntheIdentifiabilityofControlledWorldModels.md
Saved: 2026-07-26 20:53
Source: 2026-07-24_15-49-12Z_OntheIdentifiabilityofControlledWorldModels.md
Model: None

---

## Summary  
The paper investigates when Joint‑Embedding Predictive Architectures (JEPAs) can uniquely recover both the latent state of a world and its controlled dynamics from high‑dimensional observations under action‑conditioned behavior policies. It establishes a joint identifiability theory that links representation and transition identifiability to two policy‑dependent conditions: spectral separation of the predictable signal and non‑degenerate conditional variation in actions. The authors prove that when both hold, every global minimizer of the JEPA objective identifies the latent state and transition up to an orthogonal transformation, and they derive quantitative bounds for approximate optimization scenarios.

## Semantic links
- [[concepts/papers/2026-08-02_14-26-12Z_PermissionDenied_Policy_GradedEvaluationofC_summary.md|Summary: 2026-08-02_14-26-12Z_PermissionDenied_Policy_GradedEvaluationofCodingAg.md]] — 4 title terms overlap; 11 summary/topic terms overlap; semantic match 0.07
- [[concepts/papers/2026-07-22_20-43-12Z_Transition_RelatedPotentialsasMarkersofNarr_summary.md|Summary: 2026-07-22_20-43-12Z_Transition_RelatedPotentialsasMarkersofNarrativeCo.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.05
- [[concepts/papers/2026-07-30_10-17-55Z_TAPO_Transition_AwarePolicyOptimizationforL_summary.md|Summary: 2026-07-30_10-17-55Z_TAPO_Transition_AwarePolicyOptimizationforLLMAgent.md]] — 3 title terms overlap; 11 summary/topic terms overlap; semantic match 0.12

## Key Contributions  
- [Finding 1] A joint identifiability framework for controlled world models with Gaussian latent states under state‑dependent Gaussian behavior policies.  
- [Finding 2] Two policy‑dependent conditions: spectral separation of the predictable signal governs representation identifiability, while non‑degenerate conditional action variation governs transition identifiability.  
- [Finding 3] A quantitative bound on identification error for approximate JEPA optimization and a counterfactual‑to‑on‑policy error ratio that equals the inverse transition‑identifiability margin.

## Methodology  
The authors formulate the problem as a joint learning task where observations are nonlinear functions of latent states, actions influence dynamics via Gaussian behavior policies, and the objective is to minimize reconstruction and prediction errors. They derive necessary conditions for identifiability by analyzing the covariance structure of observable signals and the action‑variation matrix under the policy. Using spectral analysis they test separation of signal components, and they construct perturbations along weakly excited action directions to evaluate transition identifiability via counterfactual error ratios.

## Results  
Theoretical proofs show that when both conditions are satisfied, any global minimizer of the JEPA loss uniquely identifies state and transition up to orthogonal equivalence. Experiments on nonlinear observation maps with behavior policies confirm these results: representation errors vanish under spectral separation, while transition errors persist when action variation is degenerate. Approximate optimization yields bounded error growth proportional to the identified identifiability margin.

## Significance  
Understanding when world models are identifiable informs safe planning and counterfactual prediction in reinforcement learning. The work clarifies that limited action coverage can obscure transition dynamics, highlighting a practical cost for model training and decision making.

## Related Concepts  
- Joint‑Embedding Predictive Architectures (JEPAs)  
- Gaussian latent states  
- Spectral separation of signals  
- Conditional action variation  
- Identifiability theory  
- Counterfactual prediction  
- Transition identifiability margin
