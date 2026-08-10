# Summary: 2026-08-07_13-42-43Z_LearningSuffersMoreThanthePolicyClassUnderPartialO.md
Saved: 2026-08-09 22:58
Source: 2026-08-07_13-42-43Z_LearningSuffersMoreThanthePolicyClassUnderPartialO.md
Model: None

---

## Summary  
The paper investigates why reinforcement‑learning agents under partial observability often perform poorly even when a good policy and an expressive value function exist, showing that the issue stems from critic bias rather than actor capacity limits. It analyzes a solvable linear‑quadratic problem with closed‑form solutions to demonstrate this phenomenon. The analysis reveals that the agent’s learned policy is 35 % worse than the optimal one available to it, while the best representable policy is only 10.4 % suboptimal. The authors provide closed‑form expressions for the resulting policy, its cost, and a design parameter that eliminates the problem.  

## Key Contributions  
- [Finding 1] In partially observable settings, learning can be worse than the inherent difficulty of representing optimal policies.  
- [Finding 2] The root cause is a critic bias misinterpreting unexplained state variation as curvature in value estimates, leading to suboptimal actor updates.  
- [Finding 3] A simple design choice—how far the learner looks ahead before trusting its value function—can remove the bias and recover near‑optimal performance.  

## Methodology  
The authors construct a partially observed linear‑quadratic control problem that admits an exact optimal policy. They compare three scenarios: (i) full observability, (ii) partial observation with a standard actor‑critic learner, and (iii) partial observation with a modified look‑ahead horizon. Using analytical derivations they compute the resulting policies and their cumulative costs, establishing closed‑form expressions for each scenario.  

## Results  
Theoretical analysis shows that under default settings the best policy the critic can represent is 10.4 % worse than optimal, while the actor settles at a policy 35 % suboptimal. Simulations confirm these predictions across multiple parameter sets, and experiments show that extending the look‑ahead horizon improves performance dramatically, whereas adding memory of past observations has negligible effect.  

## Significance  
This work clarifies a long‑standing mystery in reinforcement learning: why agents degrade beyond the limits imposed by their representation capabilities. By identifying a specific bias mechanism, it offers design guidance for improving partial‑observation RL systems and informs theoretical understanding of learning dynamics under uncertainty.  

## Related Concepts  
- Partial observability  
- Actor‑critic architecture  
- Value function expressiveness  
- Bias vs. capacity trade‑off  
- Look‑ahead horizon  
- Linear‑quadratic control
