# Summary: 2026-08-06_01-47-47Z_EcoAgent_Bench_EvaluatingEconomicDecision_Makingin.md
Saved: 2026-08-06 20:31
Source: 2026-08-06_01-47-47Z_EcoAgent_Bench_EvaluatingEconomicDecision_Makingin.md
Model: None

---

## Summary  
EcoAgent‑Bench introduces a benchmark for evaluating economic decision‑making in budget‑constrained LLM agents, defining tasks with explicit priced actions and budgets to test real‑world choices among local lookup, broader search, model tier selection, or human escalation. It comprises 304 tasks across five families derived from GAIA, HotpotQA, and MuSiQue, covering four decision types: avoiding unnecessary escalation, escalating when local evidence is insufficient, selecting a model tier, and stopping on unsupported premises. The benchmark evaluates seven LLM agents in both tool‑API and workspace‑CLI environments while comparing micro‑accuracy rewards with economic‑consistency scores. These results reveal that task completion and cost efficiency are distinct properties under budget limits.

## Key Contributions  
- Finding 1: Micro‑averaged accuracy rewards one‑sided policies (always‑escalate) achieve high success but fail save‑oriented tasks, highlighting a trade‑off between speed and cost.  
- Finding 2: Tool‑API agents have low micro strict success (3.9–24.0 %) and poor economic consistency (max 7.3 %), often stopping prematurely or overspending on cheap tasks.  
- Finding 3: A budget sweep changes GPT‑5.4’s escalation rate from 0 % to only 3 %, showing that budget constraints directly influence decision dynamics.

## Methodology  
The authors constructed EcoAgent‑Bench by curating real‑world tasks with defined action costs and budgets, then transformed them into a standardized evaluation pipeline. Tasks are grouped into five families testing four decision types: avoiding unnecessary escalation, escalating when local evidence is insufficient, selecting a model tier, and stopping on unsupported premises. Seven LLM agents (including GPT‑5.4) were run in both tool‑API and workspace‑CLI environments, with four oracle scripts providing ground‑truth decisions. Micro‑averaged accuracy rewards are computed per decision type, while an economic‑consistency score is derived as the minimum of upgrade‑oriented and save‑oriented accuracies.

## Results  
Micro‑averaged success rates for always‑escalate policies reach 92 % but drop to 48 % on save‑oriented tasks. Tool‑API agents achieve micro strict success between 3.9 % and 24.0 %, with economic consistency capped at 7.3 %. The budget sweep demonstrates that raising the budget from $0.5 to $1.0 reduces escalation frequency dramatically, from 0 % to 3 % for GPT‑5.4.

## Significance  
These findings reveal that task completion and economic efficiency are independent properties of LLM agents under budget constraints, prompting design considerations that balance speed versus cost in deployment systems.

## Related Concepts  
- Budget‑constrained decision making  
- Micro‑averaged accuracy rewards  
- Economic consistency score  
- Tool‑API vs workspace‑CLI environments  
- Oracle scripts for ground truth
