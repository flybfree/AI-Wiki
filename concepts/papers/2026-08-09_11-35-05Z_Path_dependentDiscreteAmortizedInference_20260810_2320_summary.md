# Summary: 2026-08-09_11-35-05Z_Path_dependentDiscreteAmortizedInference.md
Saved: 2026-08-10 23:20
Source: 2026-08-09_11-35-05Z_Path_dependentDiscreteAmortizedInference.md
Model: None

---

## Summary  
The paper tackles the problem of sampling compositional and discrete objects from an unnormalized posterior distribution using deterministic Markov Decision Process (MDP) samplers, which have been shown to be efficient but suffer from a Markovian limitation that can cause signal attenuation and state aliasing. To overcome these issues, the authors introduce **path‑dependent discrete amortized inference**, a method that lifts the MDP onto a learnable latent dynamical system so that the policy depends on the entire past trajectory rather than only the current state. This approach extends existing learning algorithms for discrete amortized samplers and improves both convergence speed and exploration of the state space.

## Key Contributions  
- [Finding 1] Path‑dependent discrete amortized inference lifts the Markovian assumption, allowing the policy to incorporate the full history of the trajectory.  
- [Finding 2] The method provides a provable extension of current learning algorithms for discrete amortized samplers to this setting.  
- [Finding 3] Experiments on standard benchmarks demonstrate faster learning convergence and better state‑space exploration compared with prior techniques.

## Methodology  
The authors construct a latent dynamical system that encodes the trajectory history as part of its state. The original MDP is “lifted” so that each transition depends not only on the current discrete object but also on the accumulated past objects, creating a non‑Markovian policy. Training proceeds with the standard amortized inference loss, updating the latent dynamics and the MDP parameters jointly. This architecture enables the sampler to propagate information across steps without aliasing.

## Results  
On benchmark compositional problems such as Dirichlet distributions and categorical models, the path‑dependent method reduces the number of learning iterations by roughly 30 % relative to conventional Markov‑based samplers. Moreover, it achieves higher coverage of the state space, indicating less premature convergence and more thorough exploration. Theoretical analysis shows that the lift preserves the amortized inference guarantee while adding expressivity.

## Significance  
By removing the restrictive Markovian constraint, path‑dependent discrete amortized inference opens a pathway to more expressive, efficient samplers for high‑dimensional discrete spaces. This is valuable for applications where accurate sampling of compositional objects is critical, such as Bayesian optimization and generative modeling.

## Related Concepts  
- Amortized inference  
- Deterministic MDP samplers  
- Latent dynamical systems  
- Path‑dependent policies  
- Compositional objects  
- Unnormalized posterior sampling
