# Summary: 2026-05-07_17-56-41Z_WhenNoBenchmarkExists_ValidatingComparativeLLMSafe.md
Saved: 2026-05-07 23:11
Source: 2026-05-07_17-56-41Z_WhenNoBenchmarkExists_ValidatingComparativeLLMSafe.md
Model: None

---


## Summary  
The paper tackles the challenge of comparing language‑model safety scores when no ground‑truth benchmark exists for a given language, sector, or regulatory regime. It formalizes this situation as *benchmarkless comparative safety scoring* and introduces an instrumental‑validity chain that replaces label agreement with statistical evidence derived from controlled safe versus abliterated contrasts. The authors validate the framework on a Norwegian safety pack and demonstrate its utility in real procurement decisions.

## Key Contributions  
- Formalization of benchmarkless comparative safety scoring, specifying a contract that ties scores to a fixed scenario pack, rubric, auditor, judge, sampling configuration, and rerun budget.  
- An instrumental‑validity chain (AUROC 0.89–1.00, target variance dominates with η²≈0.52, stability across ten reruns) implemented in SimpleAudit to generate scores without ground‑truth labels.  
- Demonstration that the same chain yields different outcomes for two models (Borealis vs Gemma 3) depending on scenario category and risk measure, showing that differences arise upstream of the scoring process.

## Methodology  
The authors define a *contract* that governs how safety scores are produced: a predefined set of scenarios, an evaluation rubric, specific auditors and judges, a fixed sampling configuration, and a limited rerun budget. They replace ground‑truth agreement with an instrumental‑validity chain that measures AUROC between safe and abliterated targets, decomposes variance into target identity (η²≈0.52) and auditor/judge artifacts, and checks stability across ten independent runs of SimpleAudit.

## Results  
The chain produces AUROC values ranging from 0.89 to 1.00, indicating high discriminative power between safe and abliterated outputs. Target identity explains about half the variance (η²≈0.52), while auditor/judge effects are smaller. Severity profiles stabilize after ten reruns, confirming reliability. SimpleAudit scores both models, but the substantial differences stem from upstream claim‑contract enforcement and deployment fit rather than the scoring instrument itself.

## Significance  
This work provides a principled method for generating safety evidence when no benchmark exists, allowing stakeholders to compare LLMs on real‑world data without relying on labeled datasets. It clarifies that scores are context‑dependent and must be reported together with deltas, critical rates, uncertainty, and the specific auditor/judge used, preventing misleading rankings.

## Related Concepts  
benchmarkless comparative safety scoring; instrumental validity; AUROC; variance decomposition (η²); scenario pack; rubric; local‑first instrument SimpleAudit; procurement case study.

[[2026-05-07_17-56-41Z_WhenNoBenchmarkExists_ValidatingComparativeLLMSafe.md]]