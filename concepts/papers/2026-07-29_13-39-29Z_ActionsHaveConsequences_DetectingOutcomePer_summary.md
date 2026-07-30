# Summary: 2026-07-29_13-39-29Z_ActionsHaveConsequences_DetectingOutcomePerformati.md
Saved: 2026-07-29 21:38
Source: 2026-07-29_13-39-29Z_ActionsHaveConsequences_DetectingOutcomePerformati.md
Model: None

---

## Summary  
The paper introduces Outcome Performativity, a phenomenon where predictions influence the outcomes they describe, and proposes Outcome Performativity A/B Detection (OPAB) to uncover this effect through controlled prediction interventions. OPAB compares outcome distributions between groups of predictions to detect significant dissimilarities that signal performativity. The authors formalize the problem, derive sample‑complexity bounds under different assumption classes, and validate their method empirically on real data. Their work bridges theory and practice by offering a scalable detection framework for settings where resources are limited or ethically constrained.

## Key Contributions  
- [Finding 1] OPAB provides a principled statistical test that quantifies outcome‑distribution divergence between prediction groups, enabling reliable detection of Outcome Performativity.  
- [Finding 2] The authors derive sample‑complexity bounds for various Outcome Performative assumption classes, showing when the proposed number of interventions is theoretically sufficient.  
- [Finding 3] Empirical experiments on the Open Bandits dataset demonstrate that OPAB can identify performative effects even with modest sample sizes and limited computational cost.

## Methodology  
The authors treat each prediction as an intervention that generates a distinct outcome distribution. By randomly assigning predictions to two groups (A/B), they compute empirical similarity metrics such as KL divergence or Wasserstein distance between the resulting outcomes. The test statistic is compared against a null hypothesis of no performativity, using derived confidence intervals based on sample‑complexity bounds. This approach isolates the effect of prediction choices from confounding variables and requires only a modest number of controlled experiments.

## Results  
Theoretical analysis shows that OPAB’s false‑positive rate can be bounded by O(√(log n / n)) under standard assumptions, where n is the sample size. Empirically, on the Open Bandits dataset, OPAB detected performative effects in 78 % of prediction groups with only ten interventions each, outperforming naïve baseline tests that required many more trials. The method also identified regions of indistinguishability where fewer than five interventions could not differentiate outcomes, confirming the theoretical bounds.

## Significance  
Detecting Outcome Performativity is crucial for fields like Palliative Care and credit scoring, where biased predictions can cause real‑world harm. OPAB offers a low‑cost, ethically sound way to audit such systems without extensive data collection or costly interventions. By providing clear theoretical guarantees and practical thresholds, the work enables stakeholders to trust that their models do not unintentionally shape outcomes.

## Related Concepts  
- Outcome Performativity: the causal loop where predictions influence observed results.  
- Intervention testing: controlled manipulation of prediction groups to isolate effects.  
- Sample‑complexity bounds: theoretical limits on how many experiments are needed for reliable inference.  
- KL divergence / Wasserstein distance: metrics quantifying distribution similarity between outcome groups.
