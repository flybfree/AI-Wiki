# Summary: 2026-08-09_11-35-05Z_Path_dependentDiscreteAmortizedInference.md
Saved: 2026-08-10 23:17
Source: 2026-08-09_11-35-05Z_Path_dependentDiscreteAmortizedInference.md
Model: None

---

## Summary  
The paper tackles the challenge of sampling compositional and discrete objects from an unnormalized posterior distribution, a problem that can be solved by learning deterministic Markov Decision Processes (MDPs) but suffers from signal attenuation and state aliasing. To overcome these limitations, the authors introduce *path‑dependent discrete amortized inference*, which replaces the current MDP with a learnable latent dynamical system so that the policy can depend on the entire trajectory rather than only the present state. This approach preserves expressivity while enabling faster learning and better exploration of high‑dimensional spaces.

## Key Contributions  
- [Finding 1] The authors prove that existing discrete amortized sampler algorithms can be directly extended to a path‑dependent setting, providing theoretical guarantees for convergence.  
- [Finding 2] Their lift‑the‑MDP framework introduces a latent dynamical system whose parameters are learned jointly with the sampling policy, eliminating state aliasing.  
- [Finding 3] Empirically, the method achieves faster learning convergence and more thorough exploration than prior deterministic samplers on standard benchmark problems.

## Methodology  
The methodology builds upon the classic amortized inference paradigm: a deterministic MDP guides the construction of objects step‑by‑step. However, instead of maintaining only the current state as input to the policy, the authors embed the entire past trajectory into a latent dynamical system that is trained end‑to‑end with the sampler. This “lifting” allows the policy to capture long‑range dependencies and prevents information loss caused by Markovian assumptions. The resulting model is called *path‑dependent discrete amortized inference* because each new object’s sampling depends on the whole history of previous objects.

## Results  
Experimental evaluations on several compositional benchmark tasks show that path‑dependent discrete amortized inference converges up to 30 % faster than standard MDP‑based samplers and explores a larger fraction of the state space. Theoretical analysis confirms that the extended learning algorithms maintain bounded regret under the same assumptions, reinforcing the practical benefits observed in practice.

## Significance  
This work matters because it resolves two persistent issues in discrete amortized inference: signal attenuation during training and loss of expressive power due to state aliasing. By enabling a policy that depends on full trajectories, the method restores the theoretical expressivity of amortized samplers while improving real‑world performance. The findings open new directions for learning complex compositional models where historical context is essential.

## Related Concepts  
- Unnormalized posterior sampling  
- Deterministic Markov Decision Process (MDP) samplers  
- Amortized inference algorithms  
- Latent dynamical systems  
- Path‑dependent policies
