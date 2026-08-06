# Summary: 2026-08-05_01-55-33Z_TheCalibrationFloor_FormatRepairCanMasqueradeasSel.md
Saved: 2026-08-05 22:22
Source: 2026-08-05_01-55-33Z_TheCalibrationFloor_FormatRepairCanMasqueradeasSel.md
Model: None

---

## Summary  
This paper investigates why language‑model self‑revision can appear to improve accuracy when the underlying content is unchanged, revealing a “calibration floor” where format‑related changes masquerade as reasoning gains at small‑to‑mid scale. By decomposing observed accuracy shifts into content‑margin and format‑recovery/loss margins across multiple models and cells, the authors demonstrate that format effects can dominate on 12 of 29 primary cells, especially when answers become unparseable. A causal test—constraining generated reasoning to be syntactically valid—shows that this floor is not merely observational but can be closed by up to 71 % in many cases. The study also reveals a sharp scaling gap: floor‑scale models suffer larger content‑margin errors, while capable‑scale models exhibit near‑zero content impact despite large total gains.

## Key Contributions  
- [Finding 1] Format repair can produce accuracy improvements that are entirely due to changes in parseability rather than genuine reasoning enhancement.  
- [Finding 2] A causal experiment using grammar‑constrained decoding reduces the observed gap between naive and content‑margin estimates by a median of 71 % across 14 cells, confirming format effects as a primary driver.  
- [Finding 3] The “calibration floor” is model‑size dependent: small models have high odds of content‑level change with little signal, whereas large models show zero content margin despite sizable total accuracy gains.

## Methodology  
The authors evaluated Qwen3.5 (0.8B–9B), Gemma‑4‑12B, and frontier APIs (Tencent Hy3, Nvidia Nemotron‑3‑Ultra‑550B) across 29 primary cells plus a high‑capacity arm. They measured two margins: content margin (answers remain parseable and correct) and format‑recovery/loss margin (parseability changes). Using statistical tests (Wilcoxon), they compared margins, then performed a controlled decoding where all reasoning was forced to be syntactically valid, allowing them to isolate the content component. A clustered model analysis quantified floor‑scale versus capable‑scale behavior.

## Results  
On 12 cells with high unparseable‑answer rates, format effects exceeded content effects (Wilcoxon p = 1.7e‑3). The causal decoding closed a median 71 % of the naive total effect gap; two cells converged exactly and residual gaps remained only on the largest‑effect cells. For floor‑scale models, the content margin had headroom but insufficient signal; capable‑scale models possessed strong signal yet little headroom. Replicating a confidence‑gating protocol on Qwen3.5 yielded near‑zero content gain, confirming that reported improvements were artifactual. The frontier arm showed total gains up to +0.275 with zero content margin, indicating format dominance intensifies with scale.

## Significance  
Understanding the calibration floor clarifies why self‑revision metrics can be misleading at modest model sizes, guiding more reliable evaluation protocols and preventing overestimation of reasoning quality in early‑stage models.

## Related Concepts  
- Calibration floor  
- Content margin vs. format margin  
- Self‑correction bias  
- Grammar‑constrained decoding  
- Model scaling effects
