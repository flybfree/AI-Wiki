# Summary: 2026-08-07_15-00-10Z_WinningbyPeeking_UnenforcedBudgetsandTest_SetSelec.md
Saved: 2026-08-09 20:15
Source: 2026-08-07_15-00-10Z_WinningbyPeeking_UnenforcedBudgetsandTest_SetSelec.md
Model: None

---

## Summary  
This paper reveals that many short‑budget AutoML comparisons are misleading because they ignore protocol defects such as unenforced time budgets and test‑set selection bias. By exposing how Orcetra’s 60‑second win over FLAML and AutoGluon was inflated, the authors demonstrate that standard results tables cannot capture the true performance gap when search loops score candidates on a held‑out test set. The study shows that correcting for these protocol issues collapses Orcetra’s advantage to a non‑significant margin, confirming that “winning by peeking” inflates short‑budget AutoML comparisons.

## Key Contributions  
- [Finding 1] Unenforced budgets cause search loops to exceed their allotted time, leading to inflated win rates.  
- [Finding 2] Test‑set selection bias—scoring every candidate on the test split and reporting a maximum over noisy estimates—creates a misleading headline metric.  
- [Finding 3] The combined effect of unequal compute allocation and biased selection reduces Orcetra’s advantage to only ~0.27 accuracy points, far below the expected marginal‑standard‑error bound.

## Methodology  
The authors conducted a controlled re‑run of three AutoML engines (Orcetra, FLAML, AutoGluon) on 513 OpenML datasets with strict 60‑second and 30‑second budgets. They enforced the deadline externally, allocated equal machine time across frameworks, and used validation splits for selection rather than test sets. The original “peak” results were regenerated using per‑dataset scripts to ensure reproducibility.

## Results  
When protocols are corrected, Orcetra’s win rate drops from 59.4 % (60 s) to 34.3 % on the re‑run subset, with no significant pairwise differences against FLAML or AutoGluon. Theoretical analysis shows that selection bias grows with $K$ but is limited to ~0.27 accuracy points, below the theoretical $σ\sqrt{2\ln K}$ bound due to noise cancellation across shared test rows.

## Significance  
These findings matter because they expose a systematic flaw in how short‑budget AutoML performance is reported, potentially misleading practitioners and researchers into adopting inferior systems based on inflated metrics. By providing a checklist for honest comparisons, the paper promotes more reliable evaluation practices in the field.

## Related Concepts  
- AutoML (automated machine learning)  
- Time budget enforcement  
- Test‑set selection bias  
- Marginal standard error bound  
- Search loop scoring and maximum reporting
