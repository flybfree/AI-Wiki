# Summary: 2026-07-27_05-17-06Z_WhenShouldActiveRAGRetrieve_ABudget_AwareEvaluatio.md
Saved: 2026-07-27 21:30
Source: 2026-07-27_05-17-06Z_WhenShouldActiveRAGRetrieve_ABudget_AwareEvaluatio.md
Model: None

---

## Summary  
Active RAG (retrieval‑augmented generation) systems must decide whether to pull external knowledge during generation, a decision that consumes computational budget and can degrade performance if misused. This paper argues that evaluating such systems solely on accuracy is insufficient because two policies may both claim a 50 % evidence‑usage budget yet achieve different actual usage rates or harm rates. The authors recast active retrieval as a utility‑estimation problem, separating three distinct questions: (1) whether trigger scores correctly rank beneficial retrieval decisions, (2) whether thresholds calibrated on historical data remain effective under future budgets, and (3) how the computation of triggers adds to deployment cost. By operationalizing these questions with frontiers and audits, they propose a budget‑aware evaluation framework that reports both theoretical frontiers and realized usage.

## Key Contributions  
- [Finding 1] Retrieval harm is non‑negligible; simple uncertainty or score baselines can outperform learned utility routers.  
- [Finding 2] Nominal thresholds often miss the target usage budget, leading to over‑ or under‑retrieval.  
- [Finding 3] The marginal correctness gain of a retrieval decision is the true metric for budget allocation.

## Methodology  
The authors treat active RAG as a utility estimation task: each candidate trigger defines a marginal improvement in answer correctness relative to no retrieval. They construct exact top‑k utility frontiers, deployable threshold frontiers, conservative budget frontiers, and conduct harm audits across multiple multi‑hop QA datasets and open instruction models. Cost decomposition separates the extra compute of trigger computation from generation cost.

## Results  
Across experiments, learned utility routers achieve higher marginal gain than simple baselines, yet their deployment triggers incur additional latency. Thresholds calibrated on past data exhibit up to 15 % error in realized usage compared with budget frontiers. Harm audits reveal a 2–4 % drop in accuracy when retrieval is over‑used, indicating that the utility metric must be balanced against cost.

## Significance  
Budget‑aware evaluation clarifies whether higher accuracy stems from looser budgets rather than superior policy, guiding more responsible deployment of agentic RAG systems and preventing unnecessary compute waste.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Agentic RAG / self‑adaptive retrieval  
- Utility estimation in reinforcement learning  
- Budget constraints in AI inference  
- Harm audits for model behavior
