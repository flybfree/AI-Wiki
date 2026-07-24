# Summary: 2026-07-21_19-13-54Z_TheC_indexillusion_discriminationwithoutcalibratio.md
Saved: 2026-07-24 01:23
Source: 2026-07-21_19-13-54Z_TheC_indexillusion_discriminationwithoutcalibratio.md
Model: None

---

## Summary  
The paper investigates a potential “C‑index illusion” in published survival models, questioning whether high reported discrimination (concordance index) can mask poor calibration or time‑dependent accuracy. By reproducing three real‑world survival‑ML systems—hard‑drive failure prediction, peer‑to‑peer credit default, and platform churn— the authors test five pre‑registered hypotheses under a Holm‑corrected family‑wise error rate to see if model comparisons are systematically misleading. The study demonstrates that models with near‑identical C‑indices can still fail formal calibration tests, suggesting that published rankings may overstate predictive quality.

## Key Contributions  
- [Finding 1] Published survival models often exhibit systematic calibration failures despite high C‑index values; a model reproducing the literature’s C = 0.958 actually fails a calibration test at p < 0.001.  
- [Finding 2] A broad feature‑ablation search reveals no single attribute responsible for the observed discrimination, indicating the calibration issue is not a trivial shortcut artifact.  
- [Finding 3] When loan prepayment is treated as non‑informative censoring rather than a competing risk, the lender’s default‑risk estimates are biased upward by roughly two percentage points and can exceed four in the highest‑risk segment.

## Methodology  
The authors reproduced three published survival models across distinct domains (hard‑drive failure, credit default, platform churn). Each model was validated against the anchor paper’s synthetic experiment. Five pre‑registered hypotheses were tested using a Holm‑corrected family‑wise error rate to control Type I error. The instrument was also compared with the original synthetic benchmark and a feature‑ablation search was performed to isolate contributing variables.

## Results  
Three of the five hypotheses were rejected; one passed by a narrow margin. The model with C = 0.9595 versus the reported 0.958 fails calibration testing (p < 0.001). No single feature accounts for its discrimination, so the failure is not due to a shortcut. In the lender domain, treating prepayment as non‑informative censoring inflates default risk estimates by ~2 pp (up to ~4 % in the highest‑risk segment). The platform churn model shows probability estimates that degrade with horizon while global C‑index remains within the pre‑registered band.

## Significance  
These findings highlight a misplaced confidence in published survival models: high C‑indices can conceal poor calibration and biased risk predictions, potentially leading to suboptimal decision‑making. The study underscores the need for rigorous calibration checks alongside discrimination metrics in real‑world applications.

## Related Concepts  
C-index (concordance index), calibration, time‑dependent accuracy, competing risks, non‑informative censoring, pre‑registered evaluation harness, Holm correction, family‑wise error rate.
