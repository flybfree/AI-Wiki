# Summary: 2026-07-27_03-30-44Z_GrokkingontheWeight_DecayClock_ARateHierarchyfromS.md
Saved: 2026-07-28 00:02
Source: 2026-07-27_03-30-44Z_GrokkingontheWeight_DecayClock_ARateHierarchyfromS.md
Model: None

---

## Summary  
Delayed generalization—commonly called “grokking”—remains an unsolved phenomenon in machine learning despite extensive empirical observation. This paper introduces a theoretical framework that explains grokking as the slow relaxation of a special subspace of model parameters driven solely by weight‑decay regularization. By treating the decay process as a clock with exact discrete‑time and continuous‑time laws, the authors derive a rate hierarchy that predicts how quickly the population risk decays after training stops. The framework also distinguishes between coupled L₂ regularization and decoupled weight decay, offering causal insights into interventions that alter the grokking component.

## Key Contributions  
- [Finding 1] An exactly solvable relaxation mechanism for grokking in linear models under full‑batch heavy‑ball optimization with weight decay, extended locally quadratically to nonlinear neural networks.  
- [Finding 2] Identification of a population‑active “grokking subspace” whose training predictions stay frozen while the rest of the parameters relax, establishing a rate hierarchy among regularization components.  
- [Finding 3] Explicit iteration‑scale predictions for grokking time that recover the familiar \((1-β)/(ηλ)\) scaling in the weak‑regularization regime and causal effects of optimizer choice.

## Methodology  
The authors first formulate the training dynamics as a discrete‑time gradient step augmented by weight decay, then solve the resulting linear system analytically to reveal the null space where updates vanish. They extend this analysis to neural networks using a locally quadratic approximation that preserves the same relaxation structure. By computing the spectral decomposition of the Jacobian at steady state, they isolate the grokking subspace and derive its decay rate as a function of learning‑rate η, weight‑decay λ, and momentum β. All derivations are performed without fitting parameters; closed‑form expressions for every component are obtained.

## Results  
Theoretical predictions include an exact discrete‑time law \(t_k = \lceil k / (ηλ) \rceil\) and a continuous‑time counterpart \(τ(t) = τ_0 + t/(ηλ)\). Experiments on synthetic models with known subspace dimensions confirm that the measured grokking delay follows \((1-β)/(ηλ)\) scaling, and the late‑time relaxation matches the clock within 5 % of the theoretical rate. Modular addition tasks exhibit genuine delayed generalization whose observed lag aligns with the predicted hierarchy.

## Significance  
Understanding grokking as a controlled dissipative process clarifies why some models generalize slowly while others do not, and it provides quantitative tools for designing regularization schedules that accelerate or suppress this delay. The exact clock framework also bridges theory and practice by offering causal predictions for optimizer modifications, such as switching between coupled L₂ and decoupled weight decay.

## Related Concepts  
- Grokking subspace (population‑active null space)  
- Weight‑decay clock (rate hierarchy of regularization components)  
- Heavy‑ball optimization with momentum β  
- Population risk and its asymptotic decay  
- Coupled vs. decoupled L₂ regularization
