# Summary: 2026-08-10_08-37-54Z_ComboShoppingBench_EvaluatingLLMAgentsforBudget_Co.md
Saved: 2026-08-10 23:42
Source: 2026-08-10_08-37-54Z_ComboShoppingBench_EvaluatingLLMAgentsforBudget_Co.md
Model: None

---

## Summary  
The paper introduces **ComboShoppingBench**, an agentic benchmark that evaluates large language models (LLMs) on open‑ended basket construction tasks where users must select complementary products, apply coupons, stay within a budget, and respect store‑level constraints. It bridges the gap between semantic satisfaction and real‑world feasibility by providing verifiable tasks that generate coupons, budgets, user queries, and aligned evaluation rubrics. The study demonstrates that even state‑of‑the‑art LLMs can produce semantically coherent baskets while violating budget limits or using invalid coupon combinations. This work highlights the need for constraint‑aware reasoning beyond pure text generation in shopping agents.

## Key Contributions  
- **ComboShoppingBench** provides a unified benchmark for open‑ended basket construction with real‑world constraints such as coupons, budgets, and product availability.  
- A synthetic pipeline generates diverse tasks that include user queries, coupon sets, budget caps, and witness baskets to guide LLM generation and evaluation.  
- Experiments show systematic failures in deterministic validation (budget compliance, coupon optimality) despite high semantic scores, revealing a large gap between language quality and feasible action.

## Methodology  
The authors built a simulated commerce environment where an exploration agent constructs feasible baskets of purchasable products. These witness baskets are used to synthesize tasks that include user queries, coupon combinations, budget constraints, and evaluation rubrics. LLM agents generate responses which are then assessed semantically (satisfaction, response quality) and validated deterministically (product‑ID validity, budget adherence, coupon optimality). The evaluation framework combines a qualitative rubric with automated checks to detect infeasible orders or invalid coupon usage.

## Results  
Across 120 synthetic tasks, the average semantic satisfaction score was around 84 %, but only about 57 % of generated baskets passed deterministic validation. Top models such as GPT‑4o achieved high scores yet frequently violated budget limits or employed coupons that were not combinable with the selected items. The study quantifies the discrepancy between language quality and real‑world feasibility, showing that robust constraint handling remains a major challenge.

## Significance  
ComboShoppingBench reveals that LLMs excel at generating plausible shopping baskets but often lack the necessary grounding in budget constraints and coupon rules. By exposing this limitation on a benchmark with both qualitative and quantitative evaluation, the work motivates research into more reliable, constraint‑aware agents for everyday commerce tasks.

## Related Concepts  
- Basket construction (combo‑shopping)  
- Coupon optimization and validation  
- Budget constraints in e‑commerce  
- Agentic AI and task synthesis  
- Semantic evaluation of LLM outputs  
- Deterministic validation of real‑world actions
