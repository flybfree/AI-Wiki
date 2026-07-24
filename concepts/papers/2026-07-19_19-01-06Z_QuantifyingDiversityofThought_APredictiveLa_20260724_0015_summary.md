# Summary: 2026-07-19_19-01-06Z_QuantifyingDiversityofThought_APredictiveLawofWeig.md
Saved: 2026-07-24 00:15
Source: 2026-07-19_19-01-06Z_QuantifyingDiversityofThought_APredictiveLawofWeig.md
Model: None

---

## Summary  
The paper establishes a formal law that quantifies how diverse thought among Large Language Model (LLM) ensembles can improve collective performance, separating the beneficial “rescue” mass from the detrimental “damage” mass. By deriving an exact decomposition of ensemble lift into these two components, the authors introduce a compact heuristic that uses three metrics—accuracy‑adjusted correctness correlation (φ_adj), accuracy gap, and collective accuracy—to predict uplift with high reliability. Experimental validation on 767,520 inferences across ten open‑weight models and multiple graduate‑level science benchmarks demonstrates that this heuristic outperforms raw φ in predictive power while remaining stable across datasets. The work thus provides a theoretically grounded, empirically verified method for evaluating the value of cognitive diversity in LLM ensembles.

## Key Contributions  
- [Finding 1] An exact first‑principles decomposition of LLM ensemble lift into rescue and damage masses yields a compact heuristic for calculating uplift.  
- [Finding 2] The accuracy‑adjusted correctness correlation (φ_adj), together with the accuracy gap and collective accuracy, predicts lift with strong statistical performance (Spearman’s ρ ≈ 0.84 on calibration data).  
- [Finding 3] Swap mass—measuring realised lift after swapping model votes—tracks the heuristic predictions with R² ≥ 0.96 across all experiments.

## Methodology  
The authors start from a theoretical decomposition of how diverse LLM outputs affect ensemble performance, isolating contributions that rescue low‑quality answers from those that damage high‑quality ones. From this decomposition they extract three predictive metrics: φ_adj (a corrected version of the raw correctness correlation), the accuracy gap between models, and the collective accuracy after voting. The heuristic is calibrated once on SuperGPQA using a 40:60 vote split, then applied to two unseen datasets—GPQA Diamond and an agentic cybersecurity benchmark involving multi‑turn digital‑forensics tool use in a sandbox. All votes are released openly for reproducibility.

## Results  
Raw φ exhibits almost no predictive power (R² ≤ 0.09) across SuperGPQA, GPQA Diamond, and the forensic tasks. The accuracy‑adjusted φ_adj improves dramatically to R² = 0.67 on SuperGPQA. When combined with the accuracy gap and collective accuracy, this three‑metric heuristic is the most stable pre‑pooling predictor across all datasets, achieving Spearman’s ρ = 0.51 on GPQA Diamond and ρ = 0.84 on the cybersecurity benchmark. Swap mass—calculated by swapping model votes to observe lift changes—tracks the realised uplift with R² ≥ 0.96 throughout the experiments.

## Significance  
The paper provides a predictive law that quantifies how diversity of thought translates into ensemble performance, offering a more accurate and stable metric than raw correctness correlation. By separating rescue from damage effects, it enables better model selection and ensemble design, potentially leading to higher‑quality AI outputs in scientific reasoning and cybersecurity applications.

## Related Concepts  
- Large Language Model (LLM) ensembles  
- Ensemble voting and lift  
- Rescue mass vs. damage mass decomposition  
- Accuracy‑adjusted correctness correlation (φ_adj)  
- Spearman’s rank correlation (ρ)  
- Swap mass measurement  
- Calibration on SuperGPQA  
- Open‑weight model benchmarking
