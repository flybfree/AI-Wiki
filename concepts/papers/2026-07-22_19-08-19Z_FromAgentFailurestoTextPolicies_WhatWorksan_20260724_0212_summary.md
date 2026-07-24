# Summary: 2026-07-22_19-08-19Z_FromAgentFailurestoTextPolicies_WhatWorksandWhatBr.md
Saved: 2026-07-24 02:12
Source: 2026-07-22_19-08-19Z_FromAgentFailurestoTextPolicies_WhatWorksandWhatBr.md
Model: None

---

## Summary  
The paper investigates how natural‑language feedback can be used to improve language‑model agents without retraining their weights, a problem that is especially difficult because agent failures occur only after a sequence of actions. By separating the ability to follow a useful policy from the ability to learn that policy from experience, the authors reveal a persistent gap in agent performance and demonstrate that human‑written policies can boost frozen 7B agents by five success points on TextWorldExpress, while policies generated from their own trajectories do not reliably outperform fixed prompting. Their work shows that generating reliable textual policies remains the bottleneck for agent‑level TextGrad.

## Key Contributions  
- [Finding 1] There is a clear gap between an agent’s ability to follow a useful policy and its capacity to learn that policy from experience.  
- [Finding 2] Human‑written policies improve two frozen 7B agents on TextWorldExpress by approximately five success points, proving that effective policy text exists.  
- [Finding 3] Policies generated from agent trajectories—even with richer traces, counterfactual evidence, or iterative GEPA search—do not reliably outperform fixed prompting.

## Methodology  
The authors adopt a comparative experimental design on the TextWorldExpress benchmark, which measures success in completing tasks. Two frozen 7B language‑model agents are kept constant while only their textual prompts (policies) vary: one set uses human‑written policies, another set uses policies generated from the agents’ own trajectories via GEPA (Generative Evaluation via Policy Search). They also test richer traces and counterfactual evidence as alternatives to raw trajectory text. The evaluation isolates whether policy generation is the limiting factor.

## Results  
Human‑written policies yield a consistent 5.0‑point increase in success relative to fixed prompting, indicating that well‑crafted textual guidance can be effective. In contrast, all generated‑policy approaches—including GEPA search and augmented traces—fail to surpass the baseline of fixed prompting; no statistically significant improvement is observed. The experiments confirm that the primary obstacle is not executing policy updates but reliably generating them from experience.

## Significance  
This research highlights a critical limitation in applying TextGrad to agents: while textual feedback can act as a gradient, the generation of reliable policies from agent‑generated data remains ineffective. It underscores the need for better mechanisms to translate experience into actionable text and suggests that future work should focus on improving policy synthesis rather than merely feeding feedback back into the model.

## Related Concepts  
- TextGrad: a method that uses natural‑language feedback as a gradient without updating model weights.  
- TextWorldExpress: a benchmark for evaluating language‑model agents in textual environments.  
- Frozen models: agents whose underlying weights remain unchanged during evaluation.  
- GEPA (Generative Evaluation via Policy Search): an iterative search that generates policies from agent trajectories.  
- Counterfactual evidence: synthetic examples that illustrate alternative outcomes to guide policy generation.
