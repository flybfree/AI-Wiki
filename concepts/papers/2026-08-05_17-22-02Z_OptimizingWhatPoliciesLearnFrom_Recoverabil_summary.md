# Summary: 2026-08-05_17-22-02Z_OptimizingWhatPoliciesLearnFrom_Recoverability_awa.md
Saved: 2026-08-05 22:33
Source: 2026-08-05_17-22-02Z_OptimizingWhatPoliciesLearnFrom_Recoverability_awa.md
Model: None

---

## Summary  
Critic‑free group‑based reinforcement learning for post‑training large language models suffers from inefficient rollout allocation, where many generated trajectories provide little learning signal. This paper introduces Recoverability‑Aware Intervention Learning (RAIL), which treats rollout generation as an online contextual‑bandit problem and learns a controller that selects interventions based on the improvement they produce. By using a shadow‑to‑live procedure, RAIL continuously adapts to policy changes while preserving the ability to generate informative rollouts under limited budgets.

## Key Contributions  
- Finding 1: RAIL models intervention selection as an online contextual‑bandit problem, enabling the controller to prioritize interventions that yield the greatest improvement.  
- Finding 2: The shadow‑to‑live procedure collects intervention traces from a baseline policy and applies them to live rollouts, allowing the controller to keep learning while the underlying policy evolves.  
- Finding 3: RAIL consistently outperforms fixed‑budget and heuristic allocation strategies across multiple settings, demonstrating higher sample efficiency and stronger final performance.

## Methodology  
RAIL treats each intervention as a decision in a contextual bandit where the context includes the current trajectory state and the improvement of prior interventions. A neural controller is trained to maximize expected reward (improvement) by selecting which rollouts to generate. The shadow‑to‑live procedure first runs a set of “shadow” rollouts using a fixed policy, records the resulting improvements, then applies those same interventions to live rollouts while updating the controller online.

## Results  
Experimental evaluations on several post‑training tasks show that RAIL reduces redundant rollout generation by up to 30 % compared with baseline allocation schemes. The adaptive controller yields higher final performance (average gain of 1.8 % in perplexity) and maintains stable learning throughout the training horizon, even as the policy drifts.

## Significance  
By explicitly optimizing for recoverability—i.e., how much each intervention can improve a policy—the method addresses a fundamental inefficiency in current group‑based RL pipelines. This principled approach improves sample efficiency, reduces computational cost, and enables scalable learning for large language models where rollout budgets are limited.

## Related Concepts  
- Contextual bandit: decision problem with contextual information influencing choice.  
- Shadow‑to‑live procedure: generating auxiliary data from a baseline policy to inform live interventions.  
- Recoverability: the extent to which an intervention can recover or improve model performance.
