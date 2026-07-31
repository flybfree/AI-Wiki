# Summary: 2026-07-30_17-36-36Z_RethinkingInference_TimeScalinginLocalComputer_Use.md
Saved: 2026-07-30 22:22
Source: 2026-07-30_17-36-36Z_RethinkingInference_TimeScalinginLocalComputer_Use.md
Model: None

---

## Summary  
The paper investigates how scaling inference time for local computer‑use agents (CUAs) affects performance, failure modes, and computational trade‑offs under strict hardware constraints. By empirically evaluating three state‑of‑the‑art CUAs on OSWorld, the authors demonstrate that additional computation yields diminishing returns while altering error patterns, highlighting a need for selective compute allocation and failure‑aware control mechanisms.

## Key Contributions  
- [Finding 1] Contextual scaling improves trajectory stability early in execution but saturates as token cost rises, leading to premature false successes.  
- [Finding 2] Temporal scaling reduces max‑step stalls yet does not markedly boost task success because longer horizons often extend erroneous trajectories rather than correct them.  
- [Finding 3] Structural decomposition introduces planning and formatting overhead in two‑stage local agents, while parallel scaling can mitigate these failures at a high computational cost.

## Methodology  
The authors conducted systematic experiments across contextual, temporal, structural, and parallel dimensions using Qwen3‑VL‑8B/30B‑A3B, UI‑TARS‑1.5‑7B, and OpenCUA‑7B on the OSWorld benchmark. They measured task success rates, token usage, failure type distribution, and runtime overhead for each scaling variant, comparing them against a baseline inference‑time budget.

## Results  
Contextual scaling yielded a modest 3–4 % increase in trajectory stability at low token budgets but reached saturation after ~150 tokens, with failures shifting to “false success” cases. Temporal scaling cut average max‑step stalls by roughly 20 % without a corresponding rise in task completion; instead, it prolonged incorrect paths. Structural decomposition added an extra 30–40 % runtime overhead and correlated with higher failure rates, whereas parallel scaling reduced these failures but at a cost of ~1.5× additional compute per step.

## Significance  
These findings underscore that naive inference‑time scaling is ineffective for resource‑constrained local CUAs; instead, they advocate failure‑aware allocation strategies that prioritize contextual grounding over raw compute expansion and recognize the trade‑offs introduced by architectural decompositions.

## Related Concepts  
- Inference‑time scaling  
- Local computer‑use agents (CUAs)  
- OSWorld benchmark  
- Contextual grounding  
- Temporal horizon extension  
- Structural decomposition in two‑stage agents  
- Parallel inference scaling
