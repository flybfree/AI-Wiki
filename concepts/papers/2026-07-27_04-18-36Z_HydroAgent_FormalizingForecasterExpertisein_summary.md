# Summary: 2026-07-27_04-18-36Z_HydroAgent_FormalizingForecasterExpertiseintoSkill.md
Saved: 2026-07-28 00:05
Source: 2026-07-27_04-18-36Z_HydroAgent_FormalizingForecasterExpertiseintoSkill.md
Model: None

---

## Summary  
The paper introduces HydroAgent, a skill‑orchestrated agent framework that formalizes tacit forecaster expertise into an auditable and reproducible workflow for flood forecasting. By embedding Large Language Models (LLMs) within a model‑driven pipeline, each “skill” encodes explicit rules that bound LLM reasoning to physical simulation outputs. The authors validate the approach on five state‑of‑the‑art LLMs in the South Yamhill River basin using 129 events and a 5‑fold cross‑validation scheme. Results show that guided scheme selection improves Kolmogorov–Greenberg Efficiency (KGE) by up to 0.154 while preserving high correlation between forecasted peak flow/flood volume and prior judgments.

## Key Contributions  
- [Finding 1] HydroAgent provides a formal, skill‑oriented representation of forecaster expertise that can be audited and transferred across domains.  
- [Finding 2] The framework demonstrates that explicit rule boundaries guide LLM reasoning to achieve KGE improvements ranging from +0.023 to +0.154 over a high‑baseline scheme library (average KGE = 0.890).  
- [Finding 3] Five tested LLMs execute the HydroAgent workflow with judgment accuracy between 40 % and 80 %, highlighting moderate performance variation and notable cost differences.

## Methodology  
HydroAgent is built as a skill‑orchestrated agent where each skill represents an explicit rule that limits LLM inference. The model‑driven flood forecasting pipeline first generates physical simulations, then routes the output to the LLM via a curated set of skills. A high‑baseline scheme library supplies initial forecasts, which are refined by the LLMs under rule constraints. The authors evaluate this workflow on five LLMs using 129 South Yamhill River events with a 5‑fold cross‑validation strategy, measuring both KGE and Pearson correlation.

## Results  
Prior judgment captures observed peak flow within a 5 % tolerance in 10 out of 11 events and flood volume within 5 % tolerance in 11 out of 14 events. Across the full dataset (129 events) the Pearson correlations are 0.62 for peak flow and 0.84 for flood volume. The baseline KGE is 0.890; guided scheme selection raises it to 0.913–0.974, an improvement of 0.023–0.154. All five LLMs successfully perform the workflow with judgment accuracy ranging from 40 % to 80 %.

## Significance  
HydroAgent bridges tacit forecaster knowledge with a reproducible, auditable process that enhances forecast skill without supplanting human expertise. By explicitly encoding expert rules into LLM reasoning, the framework streamlines analytical steps and supports more informed decision‑making in flood management.

## Related Concepts  
- Flood forecasting  
- Large Language Models (LLMs)  
- Kolmogorov–Greenberg Efficiency (KGE)  
- Skill‑orchestrated agent  
- Model‑driven workflow  
- Explicit expert rules  
- Auditability and reproducibility
