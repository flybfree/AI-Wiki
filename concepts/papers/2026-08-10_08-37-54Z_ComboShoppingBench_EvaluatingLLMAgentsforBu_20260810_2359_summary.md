# Summary: 2026-08-10_08-37-54Z_ComboShoppingBench_EvaluatingLLMAgentsforBudget_Co.md
Saved: 2026-08-10 23:59
Source: 2026-08-10_08-37-54Z_ComboShoppingBench_EvaluatingLLMAgentsforBudget_Co.md
Model: None

---

## Summary  
[ComboShoppingBench is an agentic benchmark designed to evaluate large language models’ ability to construct feasible basket shopping orders under budget and coupon constraints in a simulated commerce environment. The paper addresses the difficulty of assessing LLM agents when multiple valid baskets exist, making exact‑match metrics insufficient while semantic evaluation alone cannot detect infeasible or invalid orders. To overcome these challenges, the authors introduce a synthesis‑driven framework that generates tasks with coupons, budgets, user queries, and aligned evaluation rubrics. Experiments show that even strong LLMs struggle on this task, highlighting substantial room for improvement in reliable, constraint‑aware combo shopping.]  

## Key Contributions  
- [Finding 1] ComboShoppingBench provides a unified benchmark for open‑ended basket construction with verifiable constraints such as budget limits and coupon validity.  
- [Finding 2] The benchmark separates semantic generation from deterministic validation, allowing both quality assessment and feasibility checking in one evaluation pipeline.  
- [Finding 3] Experiments reveal that LLM agents consistently fail to produce coupon‑optimal or fully budget‑compliant baskets despite high reasoning scores.]  

## Methodology  
[The authors built a simulated commerce and takeout environment where an exploration agent creates a feasible basket of purchasable products. This witness then guides the synthesis of coupons, budget constraints, user queries, and evaluation criteria to ensure coherence. During evaluation, LLM judges score semantic satisfaction, response quality, and claim faithfulness, while deterministic checks verify product‑ID validity, budget compliance, and coupon optimality.]  

## Results  
[Main experimental results show that the average semantic‑satisfaction score across diverse LLMs is below 0.5 on a 1–1 scale, indicating poor understanding of basket feasibility. Additionally, validation failures are frequent: many agents generate coupons that cannot be combined or exceed budget limits, and some produce product IDs that do not exist in the simulated store.]  

## Significance  
[This work demonstrates a clear gap between theoretical LLM capabilities and practical real‑world shopping tasks that require multi‑step, constrained planning. By exposing these limitations on a well‑defined benchmark, ComboShoppingBench motivates research into better prompting strategies, tool use, or hybrid architectures that can reliably handle coupon optimization and budget constraints.]  

## Related Concepts  
[Basket construction, coupon optimization, budget constraints, semantic evaluation, agentic reasoning, verification benchmarks, combinatorial search, store‑level feasibility.]
