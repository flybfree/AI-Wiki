# Summary: 2026-07-26_11-49-23Z_OptimalRewardShaping_AutonomousCarParkingCaseStudy.md
Saved: 2026-07-27 22:42
Source: 2026-07-26_11-49-23Z_OptimalRewardShaping_AutonomousCarParkingCaseStudy.md
Model: None

---

## Summary  
The paper tackles the difficulty of designing effective reward functions for model‑free reinforcement learning under non‑holonomic constraints in autonomous car parking. It proposes a parameterized reward shaping framework that combines coverage‑gated alignment feedback, drive‑direction switch regularization, and an aligned episode termination mechanism. By jointly optimizing environmental reward parameters with algorithmic hyperparameters using Bayesian optimization, the authors achieve stable convergence and avoid local minima such as policy paralysis. The resulting Deep Q‑Network (DQN) agent outperforms uncalibrated baselines in both success rate and trajectory smoothness.

## Key Contributions  
- Finding 1: A coverage‑gated alignment feedback mechanism that aligns policy outputs with desired parking trajectories.  
- Finding 2: Drive‑direction switch regularization to prevent abrupt direction changes, improving control stability.  
- Finding 3: Joint meta‑optimization of reward parameters and DQN hyperparameters via Bayesian optimization yields a co‑calibrated system.

## Methodology  
The authors formulate the problem as a joint optimization where environmental reward shaping parameters are treated as variables that must be optimized together with the learning algorithm’s hyperparameters. They employ a surrogate‑based Bayesian optimizer to explore this high‑dimensional space, updating both the reward function and DQN settings iteratively until convergence criteria are met.

## Results  
Experiments on an autonomous parallel parking benchmark show that the co‑optimized system achieves a 28 % higher success rate compared with uncalibrated baselines. Trajectory smoothness metrics (e.g., jerk variance) drop by 35 %, indicating smoother control actions. The agent also reduces episodes of policy paralysis from 12 % to under 2 %.

## Significance  
This work demonstrates that reward shaping is not a one‑off design task but requires iterative, co‑optimized treatment when combined with model‑free RL, especially under non‑holonomic constraints. It provides a methodology for other safety‑critical autonomous systems where local minima can cause hazardous behavior.

## Related Concepts  
Model‑free reinforcement learning, reward shaping, Bayesian optimization, coverage gating, drive‑direction regularization, non‑holonomic constraints, DQN, policy paralysis, trajectory smoothness.
