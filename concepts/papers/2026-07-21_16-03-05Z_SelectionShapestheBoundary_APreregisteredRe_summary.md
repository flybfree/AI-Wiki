# Summary: 2026-07-21_16-03-05Z_SelectionShapestheBoundary_APreregisteredReplicati.md
Saved: 2026-07-21 21:01
Source: 2026-07-21_16-03-05Z_SelectionShapestheBoundary_APreregisteredReplicati.md
Model: None

---

## Summary  
The paper seeks to replicate a previously reported negative monotonicity boundary in natural‑language inference (NLI) label agreement, but it does so on the unselected populations that ChaosNLI was drawn from—namely the SNLI and MultiNLI development sets. It uses a preregistered operator tagger together with a four‑level ordinal agreement outcome to test whether non‑upward monotonicity operators produce lower label agreement. The replication fails to find any significant negative effect, suggesting that the earlier boundary may be an artifact of the selective re‑annotation process rather than a population‑level property.

## Key Contributions  
- [Finding 1] No statistically significant negative monotonicity boundary was observed in the unselected SNLI and MultiNLI populations.  
- [Finding 2] All seven pairwise contrasts between non‑upward and upward operators yielded positive Cliff’s delta values, indicating that non‑upward items agree slightly more than upward ones.  
- [Finding 3] The magnitude of these effects was below the smallest effect size of interest (0.10), meaning they are not practically meaningful.

## Methodology  
The authors approached the problem by employing a preregistered study design that mirrors the original ChaosNLI experiment: an operator tagger classifies each sentence as non‑upward or upward, and participants rate agreement on a four‑level ordinal scale. The test was conducted on the SNLI and MultiNLI development sets, with simulated misclassification of the tagger to assess robustness. A manual re‑tagging audit was performed on a fresh 200‑item sample to verify that observed effects were not due to systematic errors.

## Results  
The registered prediction fails: only one contrast reached significance, but its sign is opposite to what was registered (positive instead of negative). Every effect is far smaller than the smallest effect size of interest. Robustness checks show that simulated tagger misclassification shrinks the effects rather than amplifies them, and manual re‑tagging yields a four‑class agreement of 0.875 on the new sample.

## Significance  
This work matters because it challenges the assumption that monotonicity in NLI label agreement is an inherent property of language data; instead, it appears contingent on how items are selected for analysis. The study underscores the need for explicit reporting of selection criteria when investigating human‑label variation (HLV) and supports preregistration as a safeguard against publication bias.

## Related Concepts  
monotonicity, label agreement, Cliff’s delta, chaosNLI, natural language inference, ordinal agreement, preregistration, selection bias, re‑annotation, HLV.
