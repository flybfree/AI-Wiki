# Summary: 2026-07-30_02-58-46Z_AWARE_FX_AnAuditableKnowledge_GuidedAISystemforMea.md
Saved: 2026-07-30 20:25
Source: 2026-07-30_02-58-46Z_AWARE_FX_AnAuditableKnowledge_GuidedAISystemforMea.md
Model: None

---

## Summary  
AWARE-FX is an auditable AI/NLP decision‑support system that converts weakly structured corporate annual‑report text into traceable foreign‑exchange hedging‑disclosure measures. The authors built the system using a professional lexicon, negation and accounting‑status logic, channel‑specific encoders, evidence gates, conservative aggregation, and an audit ledger to retrieve and score thousands of snippets across 24,909 Hong Kong firm‑years (2008‑2025). The approach yields a deterministic FX score that can be externally validated against baseline and stress‑period exposure data.  

## Key Contributions  
- Finding 1: AWARE-FX converts weakly structured report text into traceable hedging‑disclosure measures using a lexicon and logic.  
- Finding 2: The system achieves high reliability with F1 scores up to 0.872 on temporal tests, and uncertainty handling improves scores by ~0.06 when abstaining from low‑confidence observations.  
- Finding 3: Deterministic FX score correlates negatively with linked baseline and stress‑period FX exposure, providing external construct validation without implying causal hedging effectiveness.  

## Methodology  
The authors built AWARE-FX as an auditable AI/NLP decision‑support system that integrates a professional‑source lexicon, negation and accounting‑status logic, channel‑specific encoders, evidence gates, conservative aggregation, and an audit ledger. They applied it to 24,909 Hong Kong firm‑years (2008‑2025), retrieving 543,527 snippets. Evaluation includes ablations, a stratified human audit of 300 snippets, three‑seed FinBERT vs ModernBERT comparisons, temporal tests limited to 2023‑2025, probability calibration, selective prediction, and fixed‑prompt benchmarks with Qwen3‑8B.  

## Results  
AWARE-FX scores were computed for each firm‑year; the deterministic FX score showed a negative association with linked baseline and stress‑period FX exposure, while the broader generic score did not. F1 performance ranged 0.702–0.872 across temporal splits, and abstaining on low‑confidence observations raised retained‑sample F1 by 0.050–0.077.  

## Significance  
This work provides a rigorously auditable framework for measuring corporate FX hedging disclosure, enabling transparent, comparable metrics that can be validated against external exposure data without implying causal hedging effectiveness.  

## Related Concepts  
- Auditable AI/NLP decision‑support system  
- Knowledge‑guided classification with lexicon and logic  
- Evidence gating and conservative aggregation  
- Temporal validation of model performance  
- External construct validation via FX exposure correlation
