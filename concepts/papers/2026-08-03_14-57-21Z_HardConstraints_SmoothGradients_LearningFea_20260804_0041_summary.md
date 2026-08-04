# Summary: 2026-08-03_14-57-21Z_HardConstraints_SmoothGradients_LearningFeasibleIn.md
Saved: 2026-08-04 00:41
Source: 2026-08-03_14-57-21Z_HardConstraints_SmoothGradients_LearningFeasibleIn.md
Model: None

---

## Summary  
This paper addresses the challenge of learning feasible inventory policies in complex, sequential decision-making environments where hard constraints limit action space and feasibility is critical. The authors propose a novel approach that integrates differentiable convex optimization within deep reinforcement learning to enforce combinatorial constraints end-to-end, avoiding the pitfalls of penalty-based or heuristic constraint-handling methods. By combining a neural network-generated continuous target with a quadratic program projection and an integer mapping, the method ensures both feasibility and integrality while maintaining smooth gradients for training. The framework enables scalable policy optimization in stochastic environments where exact MILP solvers are impractical.

## Key Contributions  
- [Finding 1] A differentiable projection mechanism that enforces hard constraints with bounded error relative to exact integer projections, ensuring the entire feasible action space is reachable during learning.  
- [Finding 2] End-to-end training of a policy using pathwise gradients from sampled trajectories, eliminating the need for external solvers and enabling seamless integration into DRL pipelines.  
- [Finding 3] Demonstrated economic superiority over state-of-the-art policies in multi-echelon production-inventory planning, achieving up to 9.75% improvement over rolling-horizon stochastic programs on larger instances.

## Methodology  
The authors embed a convex optimization module within the policy network: first, a neural network proposes continuous action targets; second, a quadratic program projects these targets onto the relaxed feasible set defined by linear constraints; third, an integer mapping restores integrality while preserving feasibility. This projection is differentiable and can be computed efficiently during training. The entire process operates within a differentiable simulator that generates trajectories from stochastic demand and supply distributions. Pathwise gradients are computed across sampled trajectories to update the policy parameters, allowing gradient-based optimization without violating constraints at any step.

## Results  
The proposed method achieves an average optimality gap below 1% on small instances of multi-echelon production-inventory planning with shared resource and material constraints. In larger networks, it outperforms state-of-the-art echelon base-stock policies by up to 9.75% and rolling-horizon stochastic programs by at least 7.7%. A real-world case study on ASML’s industry-scale operations shows a reduction in average cost of up to 3.22% compared to the best-known benchmark policy, with significant savings observed where planning is most constrained—tightly capacitated systems with high demand variability.

## Significance  
This work demonstrates that deep reinforcement learning can deliver economically meaningful solutions in sequential decision problems involving hard constraints and interdependencies, which are prevalent in supply chain and production planning. By enabling scalable, constraint-enforcing policies without sacrificing computational efficiency or accuracy, the method bridges a long-standing gap between theoretical optimization and practical DRL applications.

## Related Concepts  
- Differentiable projection  
- Quadratic programming  
- MILP (Mixed-integer linear programming)  
- Pathwise gradients  
- Feasibility enforcement in DRL  
- Multi-echelon inventory management  
- Stochastic optimization  
- Hard constraints  
- Integer mapping
