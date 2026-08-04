# Summary: 2026-07-31_19-05-43Z_Verifier_InducedSupportReshapinginOn_PolicyOptimiz.md
Saved: 2026-08-03 21:24
Source: 2026-07-31_19-05-43Z_Verifier_InducedSupportReshapinginOn_PolicyOptimiz.md
Model: None

---

## Summary  
This paper investigates how verifier‑induced support reshaping affects on‑policy reinforcement learning with verifiable rewards (RLVR). It shows that while RLVR can boost immediate task performance, it also reduces the frequency of successful trajectories needed for later objectives. The authors define effective rewardable support as trajectories reachable within a fixed rollout budget and demonstrate this effect across two model families. Their findings reveal a trade‑off between early success and future trainability.

## Key Contributions  
- Verifier‑induced support reshaping causes RLVR to improve average instruction‑following success but decrease the number of prompts with any successful response under repeated sampling.  
- The reshaped support concentrates changes in the first few response tokens, indicating that selected openings causally affect later math searchability and constraint following.  
- Marginal endpoint improvements do not translate fully into joint correctness and constraint adherence across tasks, highlighting a limitation of on‑policy optimization with RLVR.

## Methodology  
The authors employ repeated verifier‑scored sampling to score trajectories as either rewardable or non‑rewardable based on success within a fixed rollout budget. They train two model families—Math‑RLVR and IF‑RLVR—using bidirectional training with both the original and opposite verifiers, while maintaining reference‑policy constraints, routing priors, and on‑policy distillation to preserve cross‑task support.

## Results  
In Math‑RLVR, average instruction‑following success rises by 6.5 percentage points but best@32 falls by 9.8 percentage points; similarly IF‑RLVR reduces best@k across sampling budgets and lowers reward variation for later tasks. Token‑distribution analyses show that modifications concentrate in early response tokens. Controlled opening interventions confirm that the selected opening influences both math searchability and constraint following.

## Significance  
These results demonstrate a critical trade‑off in on‑policy optimization: improving immediate performance can undermine future learnable support, especially for joint tasks requiring correct and constrained responses. The findings caution against assuming endpoint gains guarantee trainability or joint capability under RLVR, urging careful design of reward structures that preserve long‑term support.

## Related Concepts  
- Verifier‑induced support reshaping  
- Effective rewardable support (trajectories within fixed rollout budget)  
- On‑policy reinforcement learning with verifiable rewards (RLVR)  
- Reward shaping and trajectory selection  
- Bidirectional training with opposite verifiers
