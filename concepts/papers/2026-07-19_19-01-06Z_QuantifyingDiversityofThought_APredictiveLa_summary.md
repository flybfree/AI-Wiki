# Summary: 2026-07-19_19-01-06Z_QuantifyingDiversityofThought_APredictiveLawofWeig.md
Saved: 2026-07-24 00:12
Source: 2026-07-19_19-01-06Z_QuantifyingDiversityofThought_APredictiveLawofWeig.md
Model: None

---

## Summary  
The paper introduces a formal law that quantifies how diverse thought among Large Language Model (LLM) ensembles improves performance, separating the “rescue” mass from the “damage” mass. It derives an exact decomposition of ensemble lift into these two components and proposes a compact heuristic based on accuracy‑adjusted correctness correlation (φ_adj), accuracy gap, and collective accuracy to predict uplift. The authors validate this law empirically across 767 520 inferences from ten open‑weight models on three graduate‑level science benchmarks and a novel cybersecurity task involving multi‑turn tool use. Their work provides the first experimentally verified metric that reliably predicts ensemble performance before pooling.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 11 summary/topic terms overlap

## Key Contributions  
- **Exact decomposition of lift**: The paper derives an exact formula separating the portion of ensemble improvement (rescue mass) from any degradation caused by conflicting reasoning (damage mass).  
- **Predictive heuristic φ_adj**: It introduces accuracy‑adjusted correctness correlation, a metric that outperforms raw φ in predictive power and can be combined with accuracy gap to form a stable pre‑pooling predictor.  
- **Empirical validation**: The law is tested on three datasets (SuperGPQA, GPQA Diamond, forensic cybersecurity tasks) achieving high Spearman correlations and near‑perfect R² for measured swap mass.

## Methodology  
The authors start from first principles of ensemble voting to compute the rescue and damage masses analytically. They then calculate φ_adj by normalizing raw correctness correlation with model accuracy gaps, producing a dimensionless predictor. The heuristic is calibrated once on SuperGPQA using a 40:60 vote split, after which its coefficients are frozen for transfer testing. All votes from the experiments are released openly to ensure reproducibility.

## Results  
Raw φ shows negligible predictive power (R² ≤ 0.09) across all datasets. The accuracy‑adjusted φ_adj improves dramatically, reaching R² = 0.67 on SuperGPQA and comparable values on GPQA Diamond and the forensic benchmark. When combined with the accuracy gap, this heuristic yields the most stable pre‑pooling predictor (Spearman ρ = 0.84 on calibration, 0.51–0.84 on transfer sets). The measured swap mass tracks realised lift with R² ≥ 0.96 throughout.

## Significance  
By providing a mathematically grounded law and a high‑accuracy predictive metric, the paper enables practitioners to design LLM ensembles that maximize benefit from diversity while minimizing conflict. This reduces reliance on trial‑and‑error pooling strategies, saving compute resources and improving downstream task performance in science and cybersecurity applications.

## Related Concepts  
- **Rescue mass**: The portion of ensemble uplift attributable to complementary reasoning.  
- **Damage mass**: The portion that harms overall performance due to contradictory outputs.  
- **Accuracy‑adjusted correctness correlation (φ_adj)**: A normalized metric that corrects raw φ for model accuracy gaps.  
- **Swap mass**: The observed difference between predicted and actual ensemble lift, measured with high R².
