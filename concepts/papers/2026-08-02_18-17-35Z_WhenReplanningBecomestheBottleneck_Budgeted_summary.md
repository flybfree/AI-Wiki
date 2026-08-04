# Summary: 2026-08-02_18-17-35Z_WhenReplanningBecomestheBottleneck_BudgetedReplann.md
Saved: 2026-08-04 00:18
Source: 2026-08-02_18-17-35Z_WhenReplanningBecomestheBottleneck_BudgetedReplann.md
Model: None

---

## Summary  
Embodied agents frequently replan to correct execution drift, but each LLM‑based replanning call accumulates a growing textual context that can cause heavy‑tailed latency spikes and SLO violations even when task success is high. The authors introduce BRACE, a budgeted control loop controller that decides whether to replan, selects a mode, allocates an explicit token budget and a service‑level objective, and incorporates optional efficiency modules. To make this feasible at scale, they also propose E‑RECAP, a cost‑aware progressive pruning technique that predicts token utility across transformer layers and removes non‑essential tokens while preserving critical head and tail content. Together these components dramatically cut the overhead of replanning on multiple embodied platforms.

## Key Contributions  
- [Finding 1] Replanning latency exhibits heavy tails that lead to SLO violations independent of average latency or success rates, creating a hidden failure mode for budgeted control.  
- [Finding 2] BRACE implements a per‑call token budget and SLO as part of a budgeted control loop, enabling proactive replanning decisions across multiple agents.  
- [Finding 3] E‑RECAP reduces the number of tokens sent to the LLM by 62–92% while keeping critical information intact, lowering SLO violation rates from near‑100 % to 4.7–50 %.

## Methodology  
The authors treat replanning as a budgeted control problem: each call is evaluated against an allocated token budget and latency SLO; if the budget would be exceeded, BRACE postpones or selects a lighter mode. E‑RECAP operates before the LLM call, estimating token utility per layer and pruning progressive subsequences that have low predictive value for the next plan, thus shrinking the context size without losing essential head and tail tokens. The controller is integrated with three benchmark environments—Meta Habitat, RoboFactory, and AirSim—to evaluate its impact on token usage and performance.

## Results  
In settings where task success is already saturated, BRACE with E‑RECAP cuts replanning‑call token counts by 62–92% and reduces SLO violation rates from 85.5–100 % to 4.7–50 %. In a harder RoboFactory scenario where open‑loop, frozen‑plan, and no‑BRACE approaches all fail, BRACE + E‑RECAP achieves 80 % success with only 4.6 % SLO violations, demonstrating that tail‑aware per‑call budgeting is effective across embodied platforms.

## Significance  
By decoupling replanning decisions from the unchecked growth of LLM context and providing a concrete token budget and SLO, BRACE addresses a previously undetected bottleneck in autonomous agents. The combination with E‑RECAP shows that cost‑aware pruning can maintain high performance while dramatically reducing computational overhead, offering a scalable solution for real‑time embodied control.

## Related Concepts  
embodied agents, replanning, LLM context accumulation, token budgets, service‑level objectives (SLO), progressive token pruning, transformer layers, utility prediction, budgeted control loops.
