# Summary: 2026-07-16_17-54-47Z_BeyondSuccessRate_Cost_AwareEvaluationofOffensivea.md
Saved: 2026-07-16 23:01
Source: 2026-07-16_17-54-47Z_BeyondSuccessRate_Cost_AwareEvaluationofOffensivea.md
Model: None

---

## Summary  
The paper proposes a cost‑aware evaluation framework for security agents that measures not only task success but also the economic efficiency of inference and tool usage. It applies this lens to offensive Cybench CTF challenges and defensive Splunk BOTS v1 investigation tasks, comparing open‑weight and proprietary models at fixed budgets. By decomposing performance into reasoning spend versus tool spend, the authors reveal distinct scaling regimes for red‑team and blue‑team activities.

## Key Contributions  
- [Finding 1] Offensive CTF performance improves with additional compute, allowing scaled open‑weight models to approach the capabilities of frontier proprietary systems while remaining cost‑competitive.  
- [Finding 2] Defensive SOC investigation does not scale linearly with raw reasoning budget; success depends more on disciplined tool use, telemetry navigation, and selective enrichment.  
- [Finding 3] Cost‑aware, SOC‑native evaluations reveal that practical utility is better captured by economic efficiency than by peak success rates alone.

## Methodology  
The authors evaluated language‑model security agents through a cost‑success lens. They fixed the total budget for each challenge (inference + tool spend) and measured how much of it was spent on reasoning versus tool calls, enrichment queries, etc., then compared model performance across these budgets.

## Results  
Offensive CTF results showed that more compute led to higher success rates, and open‑weight models could reach near‑frontier proprietary scores at lower cost. Defensive SOC investigation scores were stable despite larger inference budgets; improvements came from careful tool selection and efficient telemetry use rather than raw reasoning power.

## Significance  
This work argues that security‑agent benchmarks should prioritize economic efficiency and operational fit, providing a clearer view of which models are practically useful today and where defensive agents still need improvement. It shifts evaluation focus from peak capability to cost‑effective performance in real SOC workflows.

## Related Concepts  
Cost‑success lens, inference budget, tool spend, telemetry navigation, enrichment requests, open‑weight vs proprietary models, offensive vs defensive security agents, SOC‑native evaluations, economic efficiency, operational fit.
