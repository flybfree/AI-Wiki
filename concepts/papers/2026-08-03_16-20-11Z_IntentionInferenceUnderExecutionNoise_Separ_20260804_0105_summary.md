# Summary: 2026-08-03_16-20-11Z_IntentionInferenceUnderExecutionNoise_SeparatingAl.md
Saved: 2026-08-04 01:05
Source: 2026-08-03_16-20-11Z_IntentionInferenceUnderExecutionNoise_SeparatingAl.md
Model: None

---

## Summary  
This paper tackles the problem of interpreting actions in noisy social dilemmas where intended moves can be corrupted before execution, leading to ambiguous outcomes that may reflect either hostile intent or simple action error. By modeling opponent intentions as latent states and executed actions as stochastic observations within a Partially Observable MDP (POMDP) framework, the authors propose an active inference (AIF) solution that jointly infers current intent and learns how it evolves over time. Their analysis reveals a critical noise threshold beyond which cooperation collapses due to belief‑driven mutual intention attribution. The study demonstrates that the benefits of intention inference are only realized in games where inferring intent is decision‑relevant, highlighting a nuanced role for uncertainty decomposition.

## Key Contributions  
- [Finding 1] Introduces a POMDP formulation with latent opponent intentions and noisy observations, enabling separate treatment of aleatoric (action error) and epistemic (belief) uncertainty.  
- [Finding 2] Derives a critical noise threshold that governs the collapse of cooperation, linking it to a fixed‑point condition on the learned priors for intention states.  
- [Finding 3] Shows that the POMDP provides consistent advantages against conditionally cooperative opponents but leads to correlated belief‑driven collapse when mutual intention inference is performed under high noise.

## Methodology  
The authors adopt an active inference framework where the cost function is split into epistemic and pragmatic components. The epistemic part penalizes mismatches between observed actions and inferred intentions, while the pragmatic part rewards adherence to a strategic model of opponent behavior. By treating intentions as hidden states within a POMDP, they allow the system to update beliefs about current intent despite execution noise, solving the problem via belief propagation and expectation‑maximization steps.

## Results  
Theoretical analysis yields a threshold \( \tau_{\text{crit}} \) such that if the aleatoric noise exceeds this value, the fixed‑point of learned priors shifts to a state where cooperation is no longer optimal. Empirical experiments on the Iterated Prisoner’s Dilemma confirm these predictions: under moderate noise, the POMDP improves win rates against conditionally cooperative agents; however, when both players infer intentions simultaneously and noise surpasses \( \tau_{\text{crit}} \), belief synchronization drives a rapid collapse of cooperation. The advantage is observed only in games where inferring intent directly influences strategic choices.

## Significance  
Separating aleatoric from epistemic uncertainty provides a principled way to model real‑world social interactions, avoiding the over‑retaliation pitfalls of standard MDP approaches. By quantifying how belief dynamics interact with noise, this work advances both theoretical understanding and practical applications in game theory, negotiation design, and AI agents that must act on uncertain intentions.

## Related Concepts  
Aleatoric uncertainty, epistemic uncertainty, Partially Observable MDP (POMDP), Active Inference (AIF) framework, Markov Decision Process (MDP), social dilemma, intention inference, belief propagation, fixed‑point analysis.
