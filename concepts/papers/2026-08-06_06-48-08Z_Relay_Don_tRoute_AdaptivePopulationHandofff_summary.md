# Summary: 2026-08-06_06-48-08Z_Relay_Don_tRoute_AdaptivePopulationHandoffforCost_.md
Saved: 2026-08-06 20:32
Source: 2026-08-06_06-48-08Z_Relay_Don_tRoute_AdaptivePopulationHandoffforCost_.md
Model: None

---

## Summary  
Large language model (LLM)-driven evolution is a promising approach for program search, yet the high cost of continuously using strong models makes long‑term runs economically prohibitive. The authors show that evolutionary progress is front‑loaded and can be largely recovered by cheaper models if budget is allocated at the population level rather than per query. To address this, they introduce **Relay**, a training‑free framework that uses adaptive *population handoff* to shift inference budgets between cheap and strong models. Their work demonstrates that organizing search around evolving populations yields higher performance with lower cost.

## Key Contributions  
- [Finding 1] Early trajectory performance is informative but noisy, and cheap models can recover much of the early progress achieved by strong models at a fraction of the cost.  
- [Finding 2] They define **Relay Gain**, a metric that quantifies the marginal improvement of a compact, quality‑diverse candidate bank constructed for handoff, which serves as the scheduler reward to decide when to hand off.  
- [Finding 3] The framework achieves the highest mean score in 11 out of 12 benchmark and budget settings, outperforming all competitive baselines.

## Methodology  
Relay treats evolutionary search as a stateful process where each generated candidate reshapes the population for subsequent mutations. Instead of assigning inference budgets to individual calls, the authors allocate short blocks of cheap‑model queries to explore multiple trajectories via a bandit scheduler. The scheduler’s reward is Relay Gain, which measures how much the curated candidate bank improves over a previous handoff point. When Relay Gain exceeds a threshold, the budget is handed off: a shared strong model refines the selected candidates. This training‑free pipeline iteratively balances exploration (cheap model) and exploitation (strong model), enabling cost‑efficient evolution.

## Results  
Across four benchmark domains—such as combinatorial optimization, symbolic regression, and program synthesis—and three different inference budgets, Relay consistently reached the top mean score in 11 of the 12 experimental configurations. In all cases it beat baselines that either used per‑call budgeting or static model switching. The relay gain metric correlated strongly with performance gains, confirming its utility as a scheduler reward.

## Significance  
Relay provides a principled view that stateful evolutionary search should be budgeted around populations rather than individual queries, reducing the overall inference cost without sacrificing progress. By decoupling exploration and exploitation through adaptive handoffs, it opens pathways to scalable LLM‑driven algorithm discovery where resources are limited.

## Related Concepts  
- LLM‑driven evolution  
- Population handoff / stateful search  
- Bandit scheduling for inference budget allocation  
- Relay Gain (marginal improvement metric)  
- Candidate bank curation  
- Cost‑efficient evolutionary algorithms
