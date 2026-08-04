# Summary: 2026-08-02_11-00-41Z_Learning_BasedStochasticOptimalControlwithInfinite.md
Saved: 2026-08-04 00:06
Source: 2026-08-02_11-00-41Z_Learning_BasedStochasticOptimalControlwithInfinite.md
Model: None

---

## Summary  
This paper addresses stochastic optimal control problems involving infinite-horizon joint chance constraints, which are challenging due to their complexity and the need for feasibility guarantees over time. The authors propose a novel reformulation using state augmentation that transforms the problem into a constrained Markov decision process with additive cost and constraint structures, enabling strong duality and an unconstrained Lagrange dual formulation. A dual-ascent algorithm is introduced to solve this dual problem efficiently, yielding an optimal deterministic policy defined over the augmented state space. Additionally, they develop a learning-based approach for approximating value functions offline, reducing online computational burden while maintaining performance.

## Key Contributions  
- [Finding 1] The authors prove strong duality for their reformulated constrained Markov decision process with additive cost and constraint structures, allowing conversion to an equivalent unconstrained Lagrange dual problem.  
- [Finding 2] They design a dual-ascent algorithm that converges to an optimal deterministic Markov policy over the augmented state space, ensuring both optimality and feasibility of the solution.  
- [Finding 3] A learning-based method is proposed for offline approximation of value functions in continuous state-input spaces, significantly reducing online computational complexity.

## Methodology  
The methodology centers on reformulating the original infinite-horizon stochastic optimal control problem with joint chance constraints as a constrained Markov decision process (CMDP) by augmenting the state space. This augmentation introduces an additive structure to both the cost function and constraint functions, which is crucial for establishing strong duality. The authors then derive the Lagrange dual of this reformulated problem, resulting in an unconstrained optimization that can be solved using a dual-ascent algorithm. To handle continuous spaces efficiently, they employ a learned value approximation based on offline training, enabling fast online inference and control decisions.

## Results  
The proposed approach is evaluated on a numerical example comparing it to traditional online predictive control methods. The results show that the learning-based dual-ascent method achieves comparable or superior performance in terms of cost and constraint satisfaction while requiring far less computational effort during operation. The offline training phase reduces online complexity, making the solution scalable for real-time applications.

## Significance  
This work matters because it provides a theoretically grounded framework for solving complex stochastic optimal control problems with infinite-horizon probabilistic constraints. By leveraging duality and learning-based approximations, the method bridges theoretical tractability and practical efficiency, offering a path forward for applications in robotics, autonomous systems, and dynamic resource allocation where feasibility over time is critical.

## Related Concepts  
Key concepts include Markov decision processes (MDPs), chance constraints, Lagrange duality, state augmentation, dual-ascent algorithms, and value function approximation. These elements collectively enable the solution of high-dimensional, stochastic control problems with real-time constraints.
