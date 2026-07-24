# Summary: 2026-07-22_18-28-38Z_AdaptiveMulti_HorizonReinforcementLearning.md
Saved: 2026-07-24 02:12
Source: 2026-07-22_18-28-38Z_AdaptiveMulti_HorizonReinforcementLearning.md
Model: None

---

## Summary  
The paper proposes Adaptive Multi‑Horizon Reinforcement Learning, a method that replaces the static discount factor used in standard RL with an adaptive mechanism capable of evaluating several temporal horizons simultaneously. By dynamically selecting and combining these horizons, the approach balances short‑term rewards with long‑term consequences without manual tuning. This flexibility is especially valuable for continual learning tasks where reward structures change across task switches or environmental configurations. The authors demonstrate that the method improves parameter efficiency and adaptability in both artificial and biologically inspired systems.

## Key Contributions  
- Finding 1: Introduces a multi‑horizon framework that evaluates several discount factors at once, allowing the agent to consider multiple temporal scales simultaneously.  
- Finding 2: Develops an adaptive selection mechanism that updates horizon priorities based on recent reward patterns, leading to more efficient parameter usage.  
- Finding 3: Shows empirical superiority in continual MiniGrid environments with three sequential task changes, achieving higher cumulative rewards and faster adaptation than fixed‑discount baselines.

## Methodology  
The authors model the problem as a multi‑armed bandit of temporal horizons, each represented by a discount factor γᵢ. The agent maintains a set of candidate horizons and employs Bayesian updating to estimate their performance on recent episodes. A selection rule—such as a weighted average or entropy‑maximizing policy—chooses which horizon(s) to apply at each step. These selected discount factors are then integrated into the standard RL update equations, enabling the learning dynamics to adapt over time.

## Results  
Experiments on MiniGrid environments reveal that the adaptive method reduces the number of episodes needed for convergence by up to 30 % compared with a fixed discount factor (e.g., γ=0.9). In continual settings involving three task switches, the adaptive approach maintains higher cumulative reward and identifies the optimal horizon within five to ten episodes on average, outperforming baseline methods that rely on static hyperparameters.

## Significance  
This work bridges artificial reinforcement learning with biologically inspired temporal discounting, offering a principled way to handle variable long‑term planning needs in continual learning tasks. By removing reliance on hand‑tuned hyperparameters, the method makes RL more robust and adaptable across diverse environments, aligning with the goal of creating agents that can learn efficiently from changing reward structures.

## Related Concepts  
- Temporal Discounting  
- Multi‑Horizon Planning  
- Continual Learning  
- Adaptive Hyperparameter Optimization  
- Bayesian Updating
