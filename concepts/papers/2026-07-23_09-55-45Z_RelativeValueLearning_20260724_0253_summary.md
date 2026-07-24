# Summary: 2026-07-23_09-55-45Z_RelativeValueLearning.md
Saved: 2026-07-24 02:53
Source: 2026-07-23_09-55-45Z_RelativeValueLearning.md
Model: None

---

## Summary  
The paper introduces Relative Value Learning (RV), a reinforcement learning framework that learns value differences between states rather than absolute values, arguing that only relative changes matter for control. RV defines an antisymmetric function Δ(s_i, s_j)=V(s_i)‑V(s_j) and uses a pairwise Bellman operator to directly estimate these differences. The authors prove the operator is a γ‑contraction with a unique fixed point equal to true value differences. They also derive well‑posed targets for 1‑step, n‑step, λ‑return and reconstruct generalized advantage estimation (R‑GAE). Finally, RV integrated with PPO achieves competitive performance on the Atari benchmark (49 ALE games) compared to standard PPO, indicating that relative value estimation is an effective alternative to absolute critics.  

## Key Contributions  
- [Finding 1] The pairwise Bellman operator is a γ‑contraction guaranteeing convergence to the true value differences.  
- [Finding 2] A unique fixed point exists for the operator, providing stability and unbiasedness of policy gradients.  
- [Finding 3] RV enables reconstruction of generalized advantage estimation (R‑GAE) from relative values, yielding an unbiased estimator.  

## Methodology  
The authors approached the problem by formulating value differences as antisymmetric functions and constructing a Bellman operator that operates on pairs of states. They analyzed its contraction properties mathematically, establishing convergence guarantees. The methodology also includes deriving target functions for various return horizons (1‑step, n‑step, λ‑return) to align with policy gradient objectives. Implementation integrates RV’s relative critic with the Proximal Policy Optimization (PPO) algorithm, using R‑GAE as the advantage estimator.  

## Results  
Theoretically, the pairwise Bellman operator converges to the true value differences under standard RL assumptions. Experimentally, RV‑augmented PPO outperforms baseline PPO on 49 ALE Atari games, achieving higher cumulative rewards and lower variance in policy gradients compared to absolute critics. The R‑GAE reconstruction yields unbiased advantage estimates across all tested episodes.  

## Significance  
Relative value learning decouples the need for absolute state baselines, simplifying training and improving sample efficiency. By focusing on differences, RV reduces overestimation bias common in absolute critics and enables more stable policy updates. This work provides a theoretically sound alternative to standard value function estimation and demonstrates practical benefits in high‑dimensional control tasks.  

## Related Concepts  
- Value functions (V(s))  
- Generalized advantage estimation (GAE)  
- PPO algorithm  
- Bellman operator  
- Contraction mapping  
- R‑GAE (Relative GAE)
