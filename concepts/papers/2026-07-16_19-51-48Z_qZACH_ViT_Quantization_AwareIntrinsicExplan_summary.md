# Summary: 2026-07-16_19-51-48Z_qZACH_ViT_Quantization_AwareIntrinsicExplanationsw.md
Saved: 2026-07-23 23:47
Source: 2026-07-16_19-51-48Z_qZACH_ViT_Quantization_AwareIntrinsicExplanationsw.md
Model: None

---

## Summary  
The paper introduces qZACH‑ViT, a quantization‑aware extension of the zero‑token ZACH‑ViT backbone that delivers intrinsic patch‑level class explanations for compact medical‑image classifiers, and RASO (Recursive Attribution‑Stabilized Optimization), an optimizer that aligns classification and attribution gradients to remove conflicting components. The goal is to achieve both high inference efficiency in INT8 deployment and reliable interpretability through intrinsic evidence. Experiments on seven MedMNIST datasets demonstrate measurable gains in accuracy while preserving explanation quality.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 12 summary/topic terms overlap

## Key Contributions  
- qZACH‑ViT provides quantization‑aware intrinsic explanations with recursive patch‑level class evidence, enabling compact model deployments.  
- RASO normalizes classification and attribution gradients to remove conflicting components, improving input‑noise stability and reducing sufficiency error.  
- The combined approach yields a mean primary‑metric improvement of 0.0313 over the FP32 baseline (0.0368 with RASO), high prediction agreement (99.9751 %), artifact size reduced to 70 % of source checkpoints, and up to 2.39× CPU speedup.

## Methodology  
The authors extend ZACH‑ViT by converting its PyTorch model into ONNX INT8 graphs that use 16 signed INT8 MatMulInteger projections with INT32 accumulation, preserving classification performance while enabling mixed‑precision inference. RASO is a recursive optimization loop that matches the norm of classification gradients to attribution gradients and discards attribution terms that diverge, thereby stabilizing training and explanations.

## Results  
Across 210 checkpoints (7 datasets × 50 training images per class × 10 seeds), qZACH‑ViT improves the primary metric by an average of 0.0313; adding RASO raises this to 0.0368. Prediction agreement across 964,920 source‑to‑INT8 comparisons is 99.9751 %, with a maximum absolute change of 0.004386. Intrinsic maps exhibit cosine similarity 0.999955, rank correlation 0.9944, and top‑10 % overlap 0.9692. RASO reduces sufficiency error relative to Adam while maintaining the same attribution loss.

## Significance  
This work bridges efficiency and interpretability for medical imaging AI, delivering a deployable model that retains high accuracy and provides reliable intrinsic explanations. RASO enhances stability without sacrificing predictive performance, supporting responsible XAI in resource‑constrained clinical settings.

## Related Concepts  
ZACH‑ViT (zero‑token classification), quantization‑aware training, ONNX INT8 conversion, intrinsic attribution maps, recursive optimization, sufficiency error, mixed‑precision inference, MedMNIST dataset.
