# Summary: 2026-07-22_22-34-57Z_AreDiversityMetricsMeasuringDiversity_ACapability_.md
Saved: 2026-07-24 02:25
Source: 2026-07-22_22-34-57Z_AreDiversityMetricsMeasuringDiversity_ACapability_.md
Model: None

---

## Summary  
The paper investigates whether the five most common diversity metrics used to select models for majority‑vote ensembles actually capture true diversity or merely reflect model capability. By auditing these metrics across 31,900 subsets of 30 large language models on MMLU‑Pro and TruthfulQA under explicit capability controls, the authors uncover three empirical findings that challenge the assumption of a simple link between diversity measures and majority‑vote gain over the best member.  

## Key Contributions  
- **Finding 1:** Latent complementarity is ubiquitous; oracle gain is positive in every subset, yet simple voting beats the strongest model only 9.98 % of canonical size‑3 subsets (18.71 % when the best model is held out), and pooled size‑2–4 ensembles achieve a gain rate of just 1.27 %, largely due to deterministic even‑size voting behavior.  
- **Finding 2:** The joint‑correctness proxy “strict diversity” is nearly collinear with one minus mean accuracy (Spearman ρ ≈ 0.99), indicating that raw diversity–gain associations are strongly entangled with capability and unstable when controls are applied; three linear contingency‑table statistics are algebraically non‑separable, leaving only a modest residual pairwise co‑failure association where more shared error correlates with lower gain.  
- **Finding 3:** Joint linear regressions treating strict diversity, disagreement, and double‑fault as independent predictors are rank‑deficient by construction, revealing that the three metrics cannot be used simultaneously as independent drivers of majority‑vote performance.  

## Methodology  
The authors constructed 31,900 subsets from a pool of 30 large language models (LLMs) evaluated on two benchmark suites: MMLU‑Pro for factual knowledge and TruthfulQA for truthfulness. For each subset they computed five diversity metrics—including strict diversity, disagreement, double‑fault, and three linear contingency‑table statistics—and measured majority‑vote gain over the best single model. Explicit capability controls (e.g., fixing a random seed, holding out the strongest model) were applied to isolate the effect of diversity on performance. Statistical analyses such as Spearman correlation, regression, and rank‑deficiency tests were performed to assess relationships between metrics and gain.  

## Results  
The empirical audit shows that diversity measures do not reliably predict majority‑vote gain when capability is controlled. First, while oracle gain is always positive, simple voting outperforms the best model only rarely. Second, strict diversity correlates almost perfectly with negative mean accuracy, suggesting it reflects a trade‑off between diversity and correctness rather than pure diversity. Third, after controlling for capability, the only stable relationship is a modest residual where increased shared error reduces gain; all other relationships are either unstable or mathematically non‑separable. Joint regression models treating the three metrics as independent predictors are rank‑deficient, confirming that they cannot be simultaneously used to explain variance in gain.  

## Significance  
These findings expose a fundamental flaw in relying on diversity metrics as proxies for ensemble performance: many of them are merely re‑expressions of model capability or are mathematically incompatible with each other. The results highlight the need for more principled, capability‑controlled definitions of diversity and caution against treating diversity as an independent driver of majority‑vote gain.  

## Related Concepts  
- Diversity metrics (strict diversity, disagreement, double‑fault)  
- Majority‑vote gain over the best member  
- Oracle gain  
- Latent complementarity  
- Joint‑correctness proxy  
- Linear contingency‑table statistics  
- Capability control  
- Spearman correlation  
- Rank‑deficient regression
