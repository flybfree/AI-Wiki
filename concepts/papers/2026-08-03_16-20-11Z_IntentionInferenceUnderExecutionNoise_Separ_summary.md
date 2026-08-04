# Summary: 2026-08-03_16-20-11Z_IntentionInferenceUnderExecutionNoise_SeparatingAl.md
Saved: 2026-08-04 00:45
Source: 2026-08-03_16-20-11Z_IntentionInferenceUnderExecutionNoise_SeparatingAl.md
Model: None

---

## Summary  
The paper tackles the problem of inferring opponent intentions when actions are corrupted by execution noise, a phenomenon that creates both aleatoric (inherent randomness) and epistemic (knowledge‑based) uncertainty. By modeling social dilemmas as partially observable MDPs and solving them with active inference, the authors introduce a cost function that separates epistemic and pragmatic components to jointly infer current intent and learn how it evolves. Their analysis reveals a critical noise threshold beyond which cooperation collapses due to belief‑driven misinterpretation of intentions. The study demonstrates that the value of intention inference depends on whether intent attribution is decision‑relevant, offering a nuanced view of noisy social interaction.

## Key Contributions  
- [Finding 1] Introduces a POMDP formulation that separates latent opponent intentions from noisy executed actions, enabling distinct aleatoric and epistemic uncertainty.  
- [Finding 2] Derives a critical noise threshold linking the collapse of cooperation to a fixed‑point condition on learned priors within the active inference cost function.  
- [Finding 3] Shows that intention inference yields a consistent advantage only in games where intent attribution is decision‑relevant; under high noise mutual inference leads to correlated belief collapse.

## Methodology  
The authors treat each round of a social dilemma as a partially observable MDP, encoding the opponent’s current intention as a latent state and the observed action as a stochastic observation contaminated by execution noise. They solve this POMDP using active inference (AIF), employing a cost function that decomposes into an epistemic term (penalizing uncertainty reduction) and a pragmatic term (maximizing expected utility). This decomposition allows simultaneous inference of intent and learning of its trajectory, avoiding the over‑retaliation pitfalls of standard MDPs.

## Results  
In the iterated Prisoner’s Dilemma with symmetric noise, the POMDP‑based AIF model provides a reliable advantage against conditionally cooperative opponents when noise is moderate. However, when noise exceeds the critical threshold, mutual intention inference produces correlated belief updates that drive both players toward defection—a phenomenon termed “belief‑driven collapse.” The value of intention inference varies with noise level and opponent strategy, confirming that it is context‑dependent.

## Significance  
This work bridges game theory and AI uncertainty modeling by providing a principled framework for handling noisy social interactions. It clarifies when inferring intentions improves outcomes versus when it merely amplifies misinterpretation, informing both theoretical models of cooperation and the design of agents operating in ambiguous environments.

## Related Concepts  
- Partially Observable MDP (POMDP)  
- Active Inference (AIF)  
- Aleatoric vs. epistemic uncertainty  
- Social dilemmas  
- Intentional action inference  
- Cost function decomposition (epistemic and pragmatic components)  
- Fixed‑point condition on learned priors
