# Summary: 2026-08-06_11-29-48Z_CohortHijack_RobustnessofSingleCellAnnotationtoCom.md
Saved: 2026-08-06 22:13
Source: 2026-08-06_11-29-48Z_CohortHijack_RobustnessofSingleCellAnnotationtoCom.md
Model: None

---

## Summary  
The paper investigates whether the refinement step in single‑cell annotation can be exploited without altering the target cell’s expression profile or predicted label. To do this, the authors introduce **CohortHijack**, a robustness audit that removes selected non‑target cells from a query cohort while preserving the target’s phenotype and the model’s output. Experiments on two immune datasets (PBMC3K and Paul15) using logistic regression and calibrated linear SVMs reveal that structured removal can consistently outperform random removal, especially on Paul15. The study also shows that sophisticated search strategies such as multi‑start and beam search can alter many targets while affecting only a small fraction of the cohort and keeping collateral expression changes low.

## Key Contributions  
- [Finding 1] Structured removal of non‑target cells consistently produces stronger label flips than random removal on the Paul15 dataset, indicating that the annotation refinement process is not robust to targeted perturbations.  
- [Finding 2] Multi‑start and beam search approaches change a substantial portion of linear‑SVM (≈24 % and ≈19 %) and logistic‑regression (≈19.7 %) targets while removing only a small fraction of cells, yet the mean collateral expression changes remain below 0.4 %.  
- [Finding 3] Ablation experiments confirm that the observed effect disappears when neighborhood refinement is disabled, proving that the robustness hinges on the use of neighbor‑based voting; CellTypist majority voting shows unchanged predictions but altered refined labels after small companion‑cell removals.

## Methodology  
The authors construct a CohortHijack audit by selecting a set of non‑target cells from each query cohort and removing them, ensuring that the target cell’s expression profile, base prediction, and trained classifier remain untouched. They evaluate both random and structured removal strategies—including greedy, multi‑start, and beam search—across PBMC3K and Paul15 using logistic regression and calibrated linear SVMs to measure label changes and collateral expression impact.

## Results  
Structured removal outperformed random removal on Paul15, producing a higher rate of incorrect labels. Multi‑start search altered 24.33 % of SVM targets and 19.67 % of logistic‑regression targets while removing only a minor fraction of the cohort; the mean collateral expression change stayed under 0.4 %. When neighbor refinement was disabled, no label changes occurred, confirming its necessity. CellTypist’s majority voting remained stable in predictions but refined labels shifted after small companion‑cell removals.

## Significance  
These findings demonstrate that query‑cohort composition constitutes a target‑preserving attack surface for single‑cell annotation tools, undermining confidence in downstream analyses that rely on refined labels without altering the original cell. The results highlight the need for rigorous robustness testing to ensure annotation reliability and guide the design of more resilient annotation pipelines.

## Related Concepts  
single-cell annotation refinement, neighbor voting, calibration, logistic regression, linear SVM, multi‑start search, beam search, collateral expression changes, cohort composition, robustness audit, expression profile preservation.
