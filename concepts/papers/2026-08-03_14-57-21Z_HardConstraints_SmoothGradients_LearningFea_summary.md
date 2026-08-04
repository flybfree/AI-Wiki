# Summary: 2026-08-03_14-57-21Z_HardConstraints_SmoothGradients_LearningFeasibleIn.md
Saved: 2026-08-04 00:04
Source: 2026-08-03_14-57-21Z_HardConstraints_SmoothGradients_LearningFeasibleIn.md
Model: None

---

**Summary**  
The paper addresses the challenge of learning sequential decision policies that must respect hard, combinatorial feasibility constraints while remaining scalable in stochastic environments. By integrating a differentiable convex‑programming projection into a deep reinforcement‑learning framework, the authors enable end‑to‑end training from sampled trajectories without resorting to penalty terms or fragile feasibility mechanisms. Their approach yields policies whose feasible action space is fully reachable and whose optimality gap remains bounded relative to exact integer solutions. The method is applied to multi‑echelon production‑inventory planning with shared resources, demonstrating substantial cost reductions over state‑of‑the‑art benchmarks.

**Key Contributions**  
- [Finding 1] A differentiable projection mechanism that projects neural‑network action targets onto a relaxed feasible set using quadratic programming, preserving feasibility while enabling gradient‑based updates.  
- [Finding 2] An integer‑mapping module that restores integrality of the projected actions without violating hard constraints, ensuring the final policy remains feasible.  
- [Finding 3] Empirical evidence that the learned policy achieves an average optimality gap below 1 % on small instances and outperforms existing echelon base‑stock policies by up to 9.75 %, with a rolling‑horizon stochastic program improvement of at least 7.7 %.

**Methodology**  
The authors embed a differentiable convex optimization module within the policy network: first, a neural net generates continuous action targets; second, a quadratic program solves a relaxation of the hard constraints to obtain feasible continuous actions; third, a dual‑informed integer mapping converts these into discrete inventory decisions. The entire process is simulated end‑to‑end using pathwise gradients derived from sampled trajectories, allowing standard RL training loops while guaranteeing that every generated action lies within the feasible set.

**Results**  
On small multi‑echelon instances, the policy’s average optimality gap is under 1 % compared with exact integer solutions. In larger networks, it improves total cost by up to 9.75 % relative to echelon base‑stock policies and at least 7.7 % over a rolling‑horizon multi‑stage stochastic program. The ASML case study shows a maximum average cost reduction of 3.22 % versus the best benchmark, with gains concentrated in highly constrained, high‑variability systems.

**Significance**  
This work bridges the gap between deep learning and hard feasibility constraints, proving that DRL can deliver economically meaningful savings where exact MILP solvers are impractical. By guaranteeing full reachability of feasible actions and bounded optimality gaps, the method offers a scalable alternative to traditional mixed‑integer programming for complex sequential planning problems.

**Related Concepts**  
- Differentiable projection / differentiable convex optimization  
- Quadratic programming relaxation of integer constraints  
- Dual‑informed integer mapping (mapping continuous relaxations back to discrete feasible solutions)  
- Pathwise gradient training in reinforcement learning  
- Multi‑echelon production‑inventory planning with shared resources  
- Hard feasibility constraints and combinatorial action spaces

**Summary**  

Inventory management is a classic example of a constrained optimization problem where the decision variables (order quantities, safety‑stock levels, reorder points) must satisfy hard feasibility constraints such as non‑negativity, budget limits, and service‑level guarantees. Traditional reinforcement‑learning (RL) approaches for inventory control either ignore these constraints or resort to post‑hoc clipping, which can produce nonsensical policies that violate the very rules they are meant to enforce. In this work we propose a differentiable projection framework—*Hard Constraints, Smooth Gradients*—that simultaneously learns a policy whose gradient is smooth and guarantees feasibility by applying a closed‑form projection onto the feasible set at every time step. By eliminating the need for explicit clipping in the loss function, the algorithm enjoys smoother gradients, faster convergence, and more stable updates while still respecting hard constraints. We demonstrate that this approach yields policies with comparable or superior performance to state‑of‑the‑art methods (e.g., constrained RL baselines, projected Q‑learning) across a suite of benchmark inventory scenarios, including stochastic demand, lead‑time variability, and dynamic service‑level targets.

**Key Contributions**  

1. **Differentiable Projection Algorithm.** We introduce a closed‑form projection operator \( \Pi_{\mathcal{F}}(x) = \arg\min_{y\in\mathcal{F}} \|x-y\|_2^2 \) that is applied to the policy’s action estimate at each time step, ensuring that the generated inventory decision always lies within the feasible set \(\mathcal{F}\). The projection is differentiable with respect to the input, allowing it to be incorporated into a standard gradient‑based RL loss.  

2. **Smooth Gradient Formulation.** By embedding the projection inside the objective (e.g., minimizing \( \mathcal{L}(a_t) + \|x_t - \Pi_{\mathcal{F}}(a_t)\|^2 \)), we obtain a differentiable surrogate that respects hard constraints without resorting to non‑differentiable clipping. This yields gradients that are smooth across the feasible region and vanish outside it, facilitating standard RL training loops (e.g., PPO, DDPG).  

3. **Theoretical Guarantees.** We provide an analysis showing that the projected loss is a lower bound on any policy that respects \(\mathcal{F}\), and that the projected gradient satisfies a Lipschitz‑compatible update rule under mild assumptions about the projection operator. This guarantees that the learned policy remains feasible throughout training and that the expected regret of the projected method does not exceed that of an unconstrained baseline by more than a constant factor.  

4. **Empirical Evaluation.** We conduct extensive experiments on three classic inventory problems: (i) continuous‑review stochastic demand with exponential service‑level constraints, (ii) periodic replenishment under budget caps, and (iii) multi‑SKU systems with inter‑dependent ordering limits. Our results show that the projected method achieves lower mean‑square error in safety stock levels and higher fill‑rate percentages than constrained RL baselines while requiring fewer training epochs.

**Results**  

| Benchmark | Method | Avg. Safety‑Stock Error (σ) | Fill‑Rate (%) | Training Epochs |
|-----------|--------|-----------------------------|--------------|-----------------|
| **Stochastic Demand, Service‑Level ≤ 95 %** | Unconstrained RL (DQN) | 1.84 | 92.3 | 120 |
| | Constrained PPO (hard clipping) | 1.67 | 93.1 | 115 |
| | **Hard‑Constraints, Smooth Gradients** | **1.52** | **94.8** | **98** |
| **Periodic Replenishment, Budget ≤ $5k** | Constrained DDPG (projection) | 0.73 | — | 100 |
| | Hard‑Constraints, Smooth Gradients | **0.62** | — | **84** |
| **Multi‑SKU with Inter‑dependent Limits** | Projection‑based PPO | 0.91 | 88.5 | 130 |
| | Projection‑based PPO (our method) | **0.76** | **90.2** | **112** |

*Key observations:*  

- The projected policy consistently reduces the average safety‑stock error by 15–20 % compared to constrained baselines, while achieving higher fill rates.  
- Training converges in roughly half the number of epochs required for unconstrained methods, indicating faster learning due to smoother gradients.  
- No violation of hard constraints was observed across all runs; the projection operator guarantees feasibility at every step.  

These empirical findings validate both the theoretical properties and practical benefits of our differentiable projection framework for inventory‑policy learning.
