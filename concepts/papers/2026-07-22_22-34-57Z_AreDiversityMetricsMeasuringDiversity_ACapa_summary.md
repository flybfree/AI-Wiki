# Summary: 2026-07-22_22-34-57Z_AreDiversityMetricsMeasuringDiversity_ACapability_.md
Saved: 2026-07-24 02:18
Source: 2026-07-22_22-34-57Z_AreDiversityMetricsMeasuringDiversity_ACapability_.md
Model: None

---

## Summary  
The paper investigates whether the five most widely employed diversity metrics in LLM ensembles genuinely reflect model diversity or merely encode latent capability, by auditing these measures as predictors of majority‑vote gain across a large collection of subsets. It evaluates the metrics on 31 900 subsets of 30 LLMs evaluated on MMLU‑Pro (and TruthfulQA) under explicit capability controls to isolate the role of diversity from performance differences. The study uncovers that latent complementarity is rare, a strict‑diversity proxy collapses with mean accuracy, and only a modest pairwise error‑sharing effect remains stable after control.  

## Key Contributions  
- **Finding 1**: Latent complementarity is ubiquitous—oracle gain is positive in every subset, yet simple majority voting beats the strongest member in only about 9.98 % of canonical size‑3 subsets (18.71 % with held‑out best selection), indicating that diversity rarely translates into measurable vote improvement beyond the obvious case where the best model is excluded.  
- **Finding 2**: A joint‑correctness proxy (strict diversity) is nearly collinear with one minus mean accuracy across size‑3 subsets (Spearman ρ ≈ 0.991), showing that raw diversity measures are heavily entangled with capability and unstable under explicit control, except for a single outlier.  
- **Finding 3**: Three linear contingency‑table statistics are algebraically non‑separable; after capability control the only empirically stable relationship is a modest residual pairwise co‑failure association: more shared error corresponds to lower gain, though its magnitude varies with configuration. Joint rawspace regressions treating strict diversity, disagreement, and double‑fault as independent predictors are rank‑deficient by construction.  

## Methodology  
The authors construct 31 900 random subsets of 30 LLMs drawn from MMLU‑Pro (and TruthfulQA) while fixing the best member to be excluded for a “held‑out” control. They compute five diversity metrics—strict diversity, disagreement rate, double‑fault count, pairwise error sharing, and a joint‑correctness proxy—and also calculate majority‑vote gain relative to the strongest member. Explicit capability controls (e.g., fixing model size, accuracy distribution) are applied to isolate the effect of diversity. Linear regression analyses, Spearman correlations, and contingency‑table tests are used to assess relationships between metrics and gains under both raw and controlled conditions.  

## Results  
Across all subsets, oracle gain is positive in 100 % of cases, yet simple voting outperforms the best model only 9.98 % of the time (size‑3) or 1.27 % for even‑sized ensembles, reflecting deterministic voting behavior. The strict diversity metric shows a Spearman correlation of +0.991 with one minus mean accuracy in size‑3 subsets and is unstable when capability is controlled, except for one subset where it remains significant. Pairwise error sharing yields the only stable residual effect: higher shared error reduces gain modestly (≈ 0.2 points). Joint regressions are rank‑deficient because the three contingency statistics cannot be separated algebraically.  

## Significance  
These findings challenge the assumption that diversity metrics reliably drive ensemble performance, revealing instead that many measures are proxies for capability rather than genuine diversity. The modest pairwise error‑sharing effect suggests a limited but real benefit of reducing model overlap in voting, which could guide more principled ensemble design. By exposing the algebraic non‑separability of standard diversity statistics, the work provides a methodological foundation for future audits of ensemble selection criteria.  

## Related Concepts  
- Majority voting over LLMs  
- Diversity metrics (strict diversity, disagreement rate)  
- Capability control in experimental design  
- Ensemble learning and oracle gain  
- MMLU‑Pro benchmark  
- TruthfulQA dataset
