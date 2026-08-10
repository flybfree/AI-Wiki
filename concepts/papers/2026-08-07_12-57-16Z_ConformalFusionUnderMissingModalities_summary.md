# Summary: 2026-08-07_12-57-16Z_ConformalFusionUnderMissingModalities.md
Saved: 2026-08-09 22:56
Source: 2026-08-07_12-57-16Z_ConformalFusionUnderMissingModalities.md
Model: None

---

## Summary  
Multimodal fusion architectures typically assume all sensor streams are present at inference time, yet real‑world data often suffer from missing modalities due to failures or cost constraints. This paper argues that robustness and calibrated uncertainty are a single coupled property and introduces Modality-Conditioned Conformal Fusion (MCCF), an architecture that jointly handles both. MCCF integrates modality dropout, per‑modality evidential heads, Dempster‑Shafer combination rules, and a conformal calibration module to guarantee coverage even when entire input streams are absent.

## Key Contributions  
- Formal coverage guarantees for any non‑empty subset of modalities via architectural integration rather than post‑hoc recalibration.  
- Per‑modality vacuity scores that precisely localize uncertainty to the absent modality responsible for missing information.  
- No measurable accuracy loss relative to temperature‑scaled or evidential baselines while substantially narrowing the coverage gap between full and partial modalities.

## Methodology  
The authors build a multimodal bottleneck fusion backbone trained with modality dropout, which yields per‑modality Dirichlet distributions of evidence. These are fused using a Dempster‑Shafer combination rule into a joint predictive distribution; missing modalities contribute vacuous evidence that is structurally ignored. A Mondrian conformal calibration module, keyed on a modality‑presence mask, computes finite‑sample group‑conditional coverage for every non‑empty subset of modalities. The architecture thus produces calibrated uncertainty automatically without test‑time imputation.

## Results  
Across a synthetic problem and three real multimodal benchmarks, MCCF achieves its target coverage on all modality‑presence subsets, markedly reduces the gap between full and partial modalities compared to a marginal split‑conformal baseline, and imposes no measurable accuracy cost relative to temperature‑scaled or evidential baselines.

## Significance  
MCCF is the first method to provide formal coverage guarantees for arbitrary modality availability through architectural integration. By embedding uncertainty calibration directly into the fusion pipeline, it enables precise localization of missing‑modality impact via vacuity scores and eliminates the need for separate recalibration steps, advancing both robustness and interpretability in multimodal AI systems.

## Related Concepts  
Multimodal fusion, conformal calibration, Dempster‑Shafer theory, Dirichlet distributions, modality dropout, conformal group‑conditional coverage, evidence decomposition, vacuity scores.
