# Summary: 2026-07-22_19-08-19Z_FromAgentFailurestoTextPolicies_WhatWorksandWhatBr.md
Saved: 2026-07-24 02:11
Source: 2026-07-22_19-08-19Z_FromAgentFailurestoTextPolicies_WhatWorksandWhatBr.md
Model: None

---

## Summary  
The paper investigates why language‑model agents struggle to benefit from textual feedback, a problem that TextGrad addresses for static text generation but is far harder in the agentic setting where feedback arrives only after a sequence of actions. It proposes a theoretical separation between an agent’s ability to **follow** a useful policy and its ability to **learn** that policy from experience, arguing that these are distinct capabilities. The authors demonstrate empirically that human‑crafted policies can boost frozen 7B agents on TextWorldExpress by five success points, while policies derived from the agents’ own trajectories fail to improve performance. This work highlights a practical gap: generating reliable textual policies from agent experiences is far more challenging than simply applying them.

## Key Contributions  
- [Finding 1] A clear gap exists between an agent’s capacity to follow a useful policy and its capacity to learn that policy from experience, indicating that execution and learning are not interchangeable.  
- [Finding 2] Human‑written policies improve frozen 7B agents on TextWorldExpress by approximately five success points, proving that well‑crafted textual instructions can yield measurable gains without retraining model weights.  
- [Finding 3] Policies generated from agent trajectories do not reliably outperform fixed prompting, even when enriched with richer traces, counterfactual evidence, or iterative GEPA search.

## Methodology  
The authors treat the problem as a comparative study of three policy sources: (1) human‑written text, (2) trajectories extracted from the agents’ own actions, and (3) policies produced via an iterative Gradient‑Evolution Policy Algorithm (GEPA). They freeze the underlying 7B language model weights to isolate the effect of prompt‑level modifications. Experiments are conducted on TextWorldExpress, a benchmark where success is measured by task completion. The evaluation measures both immediate performance gains and the stability of policy selection over multiple episodes.

## Results  
Human policies yield a consistent five‑point uplift in success rate across all runs, confirming that textual guidance can be effective even for frozen agents. In contrast, trajectory‑derived policies show no statistically significant improvement; their success rates remain near baseline levels despite richer conditioning data or GEPA refinement. The authors also note that the process of generating and selecting a policy from experience is computationally expensive and often yields suboptimal results.

## Significance  
The findings underscore that for agents, textual feedback can act as a gradient‑free optimizer only if the generated policies are reliable. The work moves beyond the assumption that any text improvement will translate into performance gains, emphasizing the need for robust policy generation mechanisms. This insight is crucial for designing systems where agents must continuously adapt to new tasks without costly weight updates.

## Related Concepts  
- TextGrad: a gradient‑free optimization method that uses textual feedback to improve language models.  
- TextWorldExpress: a benchmark suite evaluating agent reasoning and success metrics.  
- Frozen model: a pre‑trained model whose weights are not updated during training.  
- GEPA search: an iterative policy‑generation algorithm that explores trajectory space.  
- Policy text: the textual instructions guiding an agent’s behavior.
