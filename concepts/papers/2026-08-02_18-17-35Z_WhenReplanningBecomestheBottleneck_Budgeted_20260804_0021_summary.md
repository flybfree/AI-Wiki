# Summary: 2026-08-02_18-17-35Z_WhenReplanningBecomestheBottleneck_BudgetedReplann.md
Saved: 2026-08-04 00:21
Source: 2026-08-02_18-17-35Z_WhenReplanningBecomestheBottleneck_BudgetedReplann.md
Model: None

---

## Summary  
Embodied agents frequently need to replan to recover from execution drift, partial observability, and coordination hazards, but the cumulative textual context of LLM‑based replanning calls can become prohibitively large, causing heavy‑tailed latency that violates real‑time deadlines even when task success is high. The authors introduce **BRACE**, a budgeted control loop controller that decides whether to replan, selects a replanning mode, and allocates an explicit token budget with a service‑level objective (SLO). To reduce the burden on the LLM, they also propose **E‑RECAP**, a cost‑aware progressive token pruning method that predicts token utility across transformer layers while preserving critical head and tail tokens. Together, these components dramatically cut token usage and latency violations across multiple embodied platforms.

## Key Contributions  
- [Finding 1] BRACE formulates replanning as a budgeted control loop, enabling explicit allocation of token budgets and SLOs per call to manage latency.  
- [Finding 2] E‑RECAP implements progressive token pruning that predicts token utility across transformer layers, reducing context size by up to 92% while preserving essential information.  
- [Finding 3] Empirical results show BRACE + E‑RECAP achieves 80% task success with only 4.6% SLO violations in a challenging RoboFactory scenario where other approaches fail.

## Methodology  
The authors treat replanning as a budgeted control problem: they decide whether to initiate a replanning call, choose among available modes (e.g., open‑loop, frozen‑plan), and assign an explicit token budget that must be met within a defined SLO. Optional efficiency modules can be injected to further optimize the plan. E‑RECAP operates as a preprocessing step; it scores each token’s utility across transformer layers, then prunes non‑essential tokens while retaining head and tail tokens that carry critical information, thereby shrinking the context fed to the LLM.

## Results  
In Meta Habitat, RoboFactory, and AirSim, BRACE with E‑RECAP reduces replanning‑call token counts by 62–92% and lowers SLO violation rates from 85.5–100.0 % down to 4.7–50.0 %, even when task success is already saturated. In a harder RoboFactory setting where open‑loop, frozen‑plan, and no BRACE all fail, the combined system reaches 80.0% success with only 4.6% SLO violations, demonstrating that tail‑aware per‑call budgeting improves performance across embodied platforms.

## Significance  
Tail‑aware per‑call budgeting addresses a hidden bottleneck in LLM‑driven replanning: the accumulation of context leads to heavy‑tailed latency spikes that are invisible from average metrics. By decoupling decision‑making from raw token consumption and providing explicit SLOs, BRACE enables real‑time responsiveness on diverse embodied agents without sacrificing task success.

## Related Concepts  
- Embodied agents  
- Replanning for partial observability and coordination hazards  
- LLM‑based planning  
- Token budgets and service‑level objectives (SLO)  
- Progressive token pruning across transformer layers  
- Context accumulation in large language models  
- Latency heavy tails and real‑time deadlines
