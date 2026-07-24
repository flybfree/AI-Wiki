# Summary: 2026-07-23_09-55-45Z_RelativeValueLearning.md
Saved: 2026-07-24 02:46
Source: 2026-07-23_09-55-45Z_RelativeValueLearning.md
Model: None

---

## Summary  
Relative Value Learning (RV) is a reinforcement‑learning framework that learns value differences Δ(s_i,s_j)=V(s_i)-V(s_j) directly instead of absolute state values, because only relative changes are relevant for control. The authors introduce an antisymmetric Bellman operator and prove it is a γ‑contraction with a unique fixed point equal to the true value differences. This theoretical foundation enables the construction of unbiased policy‑gradient estimators (R‑GAE) that reconstruct generalized advantage from pairwise differences. Finally, RV is integrated with PPO and evaluated on the Atari benchmark, where it matches or exceeds standard PPO performance across 49 ALE games.

## Key Contributions  
- [Finding 1] The RV framework learns value differences directly via an antisymmetric function Δ(s_i,s_j)=V(s_i)-V(s_j).  
- [Finding 2] The pairwise Bellman operator is a γ‑contraction whose unique fixed point coincides with the true value differences.  
- [Finding 3] R‑GAE reconstructs generalized advantage estimation from these pairwise differences, providing an unbiased policy‑gradient estimator.

## Methodology  
The authors define Δ(s_i,s_j) as the antisymmetric difference of two state values and construct a Bellman operator that updates these differences across episodes. By proving that this operator is a γ‑contraction, they guarantee convergence to the unique fixed point representing true value differences. The derivation yields well‑posed targets for 1‑step, n‑step, and λ‑return calculations. From the pairwise differences they reconstruct generalized advantage (GAE) and feed it into R‑GAE, an unbiased policy‑gradient estimator. To evaluate practical impact, RV is combined with PPO; the integrated model is trained on Atari games to compare learning dynamics.

## Results  
Theoretical analysis demonstrates that the Bellman operator converges to the true Δ values under standard contraction assumptions. Experimentally, the R‑GAE‑PPO hybrid achieves competitive performance on 49 ALE Atari games, matching or surpassing baseline PPO in terms of average reward and sample efficiency. The relative‑value estimator reduces variance compared with absolute critics, leading to more stable policy updates.

## Significance  
Relative value estimation offers a theoretically sound alternative to conventional absolute critics by focusing solely on differences that drive control decisions. This approach yields unbiased advantage estimates, improves sample efficiency, and stabilizes learning in complex environments such as Atari, highlighting the practical relevance of relative rather than absolute value functions.

## Related Concepts  
- Reinforcement learning  
- Value function V(s)  
- Advantage estimation (GAE)  
- Policy gradient methods  
- PPO (Proximal Policy Optimization)  
- Bellman operator  
- Contraction mapping  
- Pairwise comparisons  
- Generalized advantage
