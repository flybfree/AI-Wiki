# Summary: 2026-07-24_14-31-54Z_IQ_JEPA_AJoint_EmbeddingPredictiveArchitecturewith.md
Saved: 2026-07-26 21:51
Source: 2026-07-24_14-31-54Z_IQ_JEPA_AJoint_EmbeddingPredictiveArchitecturewith.md
Model: None

---

## Summary  
The paper introduces IQ‑JEPA, a joint‑embedding predictive architecture that learns to estimate tissue sound speed and attenuation directly from raw in‑phase/quadrature (IQ) ultrasound data using a Hermitian Vision Transformer. By leveraging both unlabeled pre‑training on massive simulated acquisitions and a small amount of labeled fine‑tuning, IQ‑JEPA achieves high accuracy with far fewer labels than conventional supervised inversion methods. The core contribution is an equivariant encoder that treats the complex IQ signal as a continuous quantity, preserving phase invariance while extracting sound‑speed information analogous to classical coherence measures. This approach represents a first step toward a foundation model for quantitative ultrasound imaging.

## Key Contributions  
- [Finding 1] An Hermitian Vision Transformer encoder can be pretrained on 63 k unlabeled Fullwave simulations, reaching an average sound speed of 15.60 m/s with only 10 k labeled points, a three‑fold improvement in label efficiency over supervised training.  
- [Finding 2] The frozen features extracted by the encoder directly reveal both sound speed and attenuation, enabling cross‑distribution transfer between layered and abdominal phantoms with minimal accuracy loss.  
- [Finding 3] Self‑supervision dominates performance gains; increasing unlabeled pre‑training data yields a roughly four‑fold boost in label efficiency down to 1 k labels.

## Methodology  
IQ‑JEPA comprises an encoder that processes the complex IQ signal directly, using a Hermitian attention mechanism whose attention is equivariant to global phase shifts and whose conjugate‑product feed‑forward layers are invariant. This design allows the model to read a quantity analogous to classical coherence without explicit phase normalization. The encoder is first pretrained on 79 293 simulated acquisitions at 2.5 MHz, then fine‑tuned on 10 000 labeled maps. The same frozen representation can be used for attenuation estimation and transferred across phantom types.

## Results  
On the full test set, IQ‑JEPA predicts sound speed at 8.71 m/s with a mean absolute error of ~2.2 m/s compared to InversionNet, which achieved 9.05 m/s (error ≈ 3.4 m/s). The label efficiency is quantified as a three‑fold gain over supervised methods and up to four‑fold at 1 k labels. Cross‑distribution pretraining between layered and abdominal phantoms incurs only ~0.2 % MAE increase.

## Significance  
By decoupling the encoder from labeling, IQ‑JEPA dramatically reduces the need for expensive simulated label generation while preserving high accuracy, paving the way toward scalable quantitative ultrasound that can be applied across diverse imaging modalities and patient populations.

## Related Concepts  
- Hermitian Vision Transformer (equivariant attention)  
- Self‑supervised learning on unlabeled ultrasound data  
- InversionNet (baseline supervised inversion)  
- Sound speed estimation in tissue  
- Attenuation modeling from IQ signals
