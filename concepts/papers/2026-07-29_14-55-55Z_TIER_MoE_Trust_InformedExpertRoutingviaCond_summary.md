# Summary: 2026-07-29_14-55-55Z_TIER_MoE_Trust_InformedExpertRoutingviaConditional.md
Saved: 2026-07-30 23:06
Source: 2026-07-29_14-55-55Z_TIER_MoE_Trust_InformedExpertRoutingviaConditional.md
Model: None

---

## Summary  
The paper tackles a long‑standing challenge in multimodal biomedical classification: the fact that simply adding more modalities does not always improve predictions because some sources may be unreliable, redundant, or mismatched to expert knowledge. To overcome this, the authors propose TIER‑MoE, a risk‑guided subspace mixture‑of‑experts (MiE) framework that explicitly models each modality’s reliability as the prediction loss incurred by an unimodal predictor on out‑of‑fold data. By integrating this estimated risk with expert‑specific subspace compatibility and preserving an always‑active shared path, TIER‑MoE routes samples to experts in a trust‑informed manner while still exploiting multimodal complementarity.

## Key Contributions  
- [Finding 1] Introduces **TIER‑MoE**, a MiE model that defines modality reliability as the out‑of‑fold loss of unimodal predictors, providing an explicit risk signal for each data sample.  
- [Finding 2] Combines the learned risk with expert‑specific subspace compatibility to enable sparse, trust‑informed routing while maintaining an always‑active shared path that retains multimodal benefits.  
- [Finding 3] Demonstrates that TIER‑MoE outperforms state‑of‑the‑art methods on four public biomedical datasets (Alzheimer’s disease status, skin‑lesion malignancy, retinal classification) in both predictive performance and probability calibration.

## Methodology  
The authors first generate out‑of‑fold predictions for each modality using models that were not trained on the current sample. The discrepancy between these OOF predictions and the true label is treated as a risk score that quantifies how trustworthy the modality is for that particular instance. This risk is then encoded into the MiE routing mechanism: higher‑risk modalities are assigned to subspaces where their experts have lower compatibility, while low‑risk modalities receive more favorable routes. An always‑active shared path ensures that every sample still benefits from multimodal fusion, preventing the loss of complementary information. The resulting architecture is a conditional MiE where the expert selection and routing probabilities are conditioned on the estimated modality risk.

## Results  
Experimental evaluation on Alzheimer’s disease status, skin‑lesion malignancy, and retinal classification datasets shows consistent improvements: Macro‑F1 scores rise by 3–5 % over SOTA, Brier scores improve markedly (indicating better probability calibration), and zero‑shot transfer to an external cohort yields gains of up to 7 % in accuracy. These results demonstrate that risk‑informed routing not only boosts predictive power but also enhances the reliability of model outputs.

## Significance  
By providing a principled, data‑driven measure of modality trustworthiness, TIER‑MoE addresses a critical flaw in current multimodal fusion: blind reliance on additional evidence can degrade performance. The method offers a scalable framework for clinical and research settings where reliable, calibrated predictions are essential.

## Related Concepts  
Mixture‑of‑Experts (MiE), risk estimation via out‑of‑fold loss, subspace routing, probabilistic calibration, always‑active shared path, modality reliability, conditional gating.
