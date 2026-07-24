# Summary: 2026-07-22_13-52-40Z_ActiveInferenceasaConvexMarkovDecisionProcess.md
Saved: 2026-07-24 01:52
Source: 2026-07-22_13-52-40Z_ActiveInferenceasaConvexMarkovDecisionProcess.md
Model: None

---

## Summary  
The paper proposes a formal treatment of Active Inference (AIF) by recasting its variational principle—minimizing expected free energy—as an optimization problem within the framework of Markov decision processes (MDPs). By separating epistemic and pragmatic components, it shows that closed‑loop policies can be optimized as a convex MDP where the pragmatic terms are linear rewards in a latent MDP while the epistemic term introduces a nonlinear, policy‑dependent component. The authors introduce a mirror descent algorithm that locally approximates this objective, enabling actor‑critic style updates and dynamic programming analysis. This perspective reveals AIF’s performative nature: the reward is shaped by the current world model, linking active inference to modern reinforcement learning theory.

## Key Contributions  
- [Finding 1] The expected free energy minimization of AIF can be expressed as a convex MDP for closed‑loop control policies, with pragmatic terms linearized into a latent reward function.  
- [Finding 2] A mirror descent (MD) algorithm is derived that locally linearizes the EFE objective around current state marginals, yielding a policy‑dependent reward compatible with actor‑critic and dynamic programming methods.  
- [Finding 3] The epistemic component creates a nonlinear, performative reward, demonstrating that active inference’s drive arises from the interaction between world‑model learning and policy optimization.

## Methodology  
The authors begin by reviewing AIF’s variational principle: EFE = ε + pragmatic term + epistemic term. For a closed‑loop policy π, the pragmatic term is linear in predictive state marginals, thus equivalent to maximizing a latent reward Rπ(s′). The epistemic term depends nonlinearly on the uncertainty of those marginals and is tied to the current policy’s performance. By treating EFE minimization as an MDP with state s, action a, and latent reward Rπ(s′,a), they formulate the problem as minimizing expected value Vₚ(π) + Vₑ(π). The MD formulation enables standard convex optimization techniques; the mirror descent algorithm is then applied to update the policy by approximating the gradient of EFE with respect to π using local linearizations.

## Results  
The derived MDP yields a locally convergent MD algorithm that improves both the pragmatic and epistemic components simultaneously. Simulations on finite‑horizon discounted tasks show that the algorithm converges to near‑optimal policies, while average‑reward settings benefit from dynamic programming updates. The policy‑dependent reward aligns with actor‑critic updates: the actor maximizes the latent reward, and the critic evaluates its effect on epistemic uncertainty. Theoretical guarantees are provided, including bound on the free energy reduction per iteration.

## Significance  
This work bridges active inference to contemporary reinforcement learning by providing a convex MDP representation, an explicit optimization algorithm with convergence analysis, and a theoretical link between epistemic drive and policy performance. It establishes performative reinforcement learning as a principled framework for AIF, offering new tools for grounding adaptive behavior in optimization theory.

## Related Concepts  
- Free energy minimization (variational principle)  
- Markov decision process (MDP)  
- Convex optimization and mirror descent  
- Performative reward  
- Epistemic vs. pragmatic terms  
- Latent MDP  
- Actor‑critic methods  
- Dynamic programming  
- Active inference (AIF)
