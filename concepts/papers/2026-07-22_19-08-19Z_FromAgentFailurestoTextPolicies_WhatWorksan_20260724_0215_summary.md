# Summary: 2026-07-22_19-08-19Z_FromAgentFailurestoTextPolicies_WhatWorksandWhatBr.md
Saved: 2026-07-24 02:15
Source: 2026-07-22_19-08-19Z_FromAgentFailurestoTextPolicies_WhatWorksandWhatBr.md
Model: None

---

## Summary  
The paper investigates how natural‑language feedback can be leveraged to improve agent behavior in TextWorldExpress without retraining model weights, focusing on the gap between generating a useful policy and actually following it. It demonstrates that human‑written policies boost frozen 7B agents by five success points, while policies derived from the agents’ own trajectories do not outperform fixed prompting. The study separates two abilities: learning a good policy from experience and executing that policy reliably.

## Key Contributions  
- Finding 1: Human‑written policies improve two frozen 7B agents on TextWorldExpress by 5.0 success points.  
- Finding 2: Policy text generated from agent trajectories does not reliably outperform fixed prompting, even with richer traces or iterative GEPA search.  
- Finding 3: The main challenge for agent‑level TextGrad is reliably generating and selecting textual policy updates rather than updating the model weights.

## Methodology  
The authors treat the problem as a separation of two distinct capabilities in agents: (1) learning a useful policy from interaction data, and (2) executing that policy without further training. They freeze the 7B language‑model weights, train agents on TextWorldExpress, and compare three regimes: (a) fixed prompting, (b) human‑written policies, and (c) policies generated from agent trajectories or via iterative GEPA search using richer feedback traces such as counterfactual evidence.

## Results  
Human‑written policies yield a consistent 5.0 point gain over the baseline, indicating that useful policy text exists. In contrast, trajectory‑derived policies show no statistically significant improvement; their performance remains comparable to fixed prompting across all experimental variations. The gap persists even when richer traces or more extensive GEPA iterations are employed, confirming that the bottleneck lies in generating and selecting effective textual updates.

## Significance  
This work clarifies that improving agent behavior via TextGrad is not merely a matter of applying gradient‑free text updates but also requires robust policy generation and selection mechanisms. It highlights a practical limitation for meta‑learning agents and suggests future research directions on hybrid approaches that combine learning, evaluation, and execution.

## Related Concepts  
- TextGrad (gradient‑free textual optimization)  
- TextWorldExpress (benchmark environment)  
- Frozen models (weights not updated during training)  
- Policy learning from experience  
- Generative Evaluation Policy Architecture (GEPA)  
- Trajectory‑based feedback and counterfactual evidence  
- Success points as a metric of agent performance
