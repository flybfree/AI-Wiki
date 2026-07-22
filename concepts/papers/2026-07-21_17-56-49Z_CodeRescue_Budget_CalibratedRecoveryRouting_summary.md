# Summary: 2026-07-21_17-56-49Z_CodeRescue_Budget_CalibratedRecoveryRoutingforCodi.md
Saved: 2026-07-21 22:04
Source: 2026-07-21_17-56-49Z_CodeRescue_Budget_CalibratedRecoveryRoutingforCodi.md
Model: None

---

## Summary  
Coding agents face a post‑failure decision problem: after an incorrect execution they can either retry cheaply or escalate to a stronger model, and the optimal choice depends on the remaining budget. The paper proposes a supervised router that learns which recovery actions succeed in rollouts of heterogeneous coding tasks. To make this router usable under varying budgets without retraining, it introduces Conformal Risk Control (CRC), a deployment‑time cost penalty selector grounded in exchangeability. Together these components enable a calibrated frontier that balances cheap and expensive recoveries efficiently.

## Key Contributions  
- [Finding 1] The authors formulate post‑failure recovery as routing over heterogeneous actions and train a supervised router directly from execution rollouts, learning when to retry cheaply versus escalate.  
- [Finding 2] They introduce Conformal Risk Control (CRC), a non‑retraining cost‑penalty selector that provides marginal expected‑cost control under the exchangeability assumption.  
- [Finding 3] Experiments show that cheap recovery and escalation exhibit complementary success patterns, and the CRC‑calibrated frontier outperforms fixed actions, prompt‑only routers, and binary cascade baselines.

## Methodology  
The authors view each failed attempt as a node in a decision graph where actions (cheap retry vs. expensive model) are edges. By collecting many execution rollouts from five coding benchmarks they generate labeled training data for the router. The CRC layer is added by estimating, via conformal confidence intervals, a deployment‑time cost penalty that can be applied at inference time; this penalty adjusts the router’s output to keep total recovery cost within a budget while preserving performance. No additional training is required because the penalty is derived from the learned distribution.

## Results  
Across held‑out failures on five coding benchmarks, cheap and escalation strategies together achieve higher solve rates than either alone. The calibrated frontier improves over fixed actions, prompt‑only routers, and a binary cascade baseline. In the main GPT‑5.4‑nano/GPT‑5.4 setting, one CRC‑calibrated frontier point exceeds the always‑escalate solve rate while consuming only 35 % of its mean recovery cost.

## Significance  
This work provides a budget‑aware routing mechanism that lets coding agents allocate cheap compute where it is most effective and reserve expensive models for truly hard cases, thereby maximizing success per dollar spent. The CRC layer enables dynamic adaptation to changing budgets without retraining, making the system robust in real‑world deployment.

## Related Concepts  
heterogeneous actions, supervised router, Conformal Risk Control (CRC), exchangeability, budget‑calibrated deployment, recovery cost, fallback strategies, GPT‑5.4‑nano/GPT‑5.4.
