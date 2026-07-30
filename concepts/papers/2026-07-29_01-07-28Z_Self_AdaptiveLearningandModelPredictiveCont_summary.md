# Summary: 2026-07-29_01-07-28Z_Self_AdaptiveLearningandModelPredictiveControlforT.md
Saved: 2026-07-29 22:17
Source: 2026-07-29_01-07-28Z_Self_AdaptiveLearningandModelPredictiveControlforT.md
Model: None

---

## Summary  
The paper proposes a self‑adaptive online learning framework combined with model predictive control to track unknown target dynamics that may switch between structured, random, or adversarial behaviors. It learns multiple predictors from scratch using one‑shot and self‑supervised techniques, adaptively selects the best predictor at each step, and achieves near‑optimality in expectation with finite‑time regret bounds tied to learning error and switching frequency.

## Key Contributions  
- [Finding 1] The method provides finite‑time near‑optimality guarantees for tracking unknown dynamics under stochastic switching.  
- [Finding 2] It learns multiple predictors simultaneously via self‑supervised, one‑shot, and computationally efficient techniques without requiring prior knowledge of the target model.  
- [Finding 3] The regret bound is proportional to the average learning error multiplied by switching frequency, showing graceful degradation when only errors exist.

## Methodology  
The authors formulate the tracking problem as a stochastic optimal control with unknown dynamics. They introduce a self‑adaptive learner that maintains a set of candidate predictors, each trained on recent samples using one‑shot or self‑supervised loss minimization. A model predictive controller selects the predictor with minimal prediction error at each step and computes an optimal control horizon. The selection is driven by a Bayesian posterior update that balances prediction accuracy and computational cost.

## Results  
Theoretical analysis shows that when both learning error and switching frequency are bounded, the expected regret converges to zero as time grows; in practice, experiments on Crazyflie robots demonstrate tracking of structured, random, and adversarial trajectories with lower average regret compared to non‑stochastic kernel methods and neural networks. The method also matches the optimal non‑causal policy when error and switching are absent.

## Significance  
This work bridges online learning and model predictive control for real‑world robotics where dynamics are uncertain, enabling robust pursuit‑evasion or dynamic mapping without sacrificing performance due to learning lag.

## Related Concepts  
Self‑adaptive learning, model predictive control, stochastic optimal control, one‑shot learning, RFF (radial basis function) methods, regret analysis, Bayesian posterior updates.
