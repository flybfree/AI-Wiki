# Summary: 2026-07-26_15-17-41Z_TheIntruderThreshold_ASpectralLawforLoRAFine_Tunin.md
Saved: 2026-07-27 21:29
Source: 2026-07-26_15-17-41Z_TheIntruderThreshold_ASpectralLawforLoRAFine_Tunin.md
Model: None

---

## Summary  
LoRA fine‑tuning can introduce intruder dimensions—new leading singular vectors that are nearly orthogonal to the pretrained spectrum and cause catastrophic forgetting.  In this paper we derive a per‑layer critical update strength \(s^{\ast}= \bar\theta/(\gamma\sigma_{1}(BA))\) using only the measured spectrum of the original weight matrix, providing a theoretical threshold for when these intruders first appear.  Our work also supplies an exact secular‑equation characterization that predicts the updated spectrum without any fitted parameters.

## Key Contributions  
- **Finding 1:** A per‑layer critical update strength \(s^{\ast}\) is computed solely from \(\sigma_{1}(BA)\) via a rectangular spiked‑deformation transform, giving a concrete threshold for intruder emergence.  
- **Finding 2:** An exact secular‑equation formulation of the updated LoRA spectrum is derived without any external fitting, enabling closed‑form predictions.  
- **Finding 3:** Empirical validation across four dense Transformer families, a state‑space model, a mixture‑of‑experts architecture, and an encoder‑decoder with 18 adapters shows the threshold localizes within a factor of two on 82 % of layers and yields high AUC (0.89) for separating intruder‑bearing from intruder‑free layers.

## Methodology  
The authors measured the first singular value \(\sigma_{1}(BA)\) of the pretrained weight matrix \(W\) using a rectangular spiked‑deformation transform, which isolates the most vulnerable eigenvector.  The critical strength is then computed as \(s^{\ast}= \bar\theta/(\gamma\sigma_{1})\).  This scalar is applied to each layer across multiple model families; the updated LoRA matrix spectrum is analyzed with an exact secular equation that predicts whether a new leading singular vector (intruder) will dominate.  No additional parameters or validation sweeps are required.

## Results  
The law localizes the empirical threshold within a factor of two on 82 % of layers, separating intruder‑bearing from intruder‑free layers at deployment with an AUC of 0.89.  The method holds unchanged on six third‑party adapters, and combined edge evaluations (threshold crossing + perplexity degradation) achieve 98 % accuracy, confirmed out‑of‑bag at 0.997.  Full fine‑tuning stays far below the threshold of every layer, resolving the asymmetry between LoRA and full fine‑tuning.  A spike‑budget rule requiring one SVD per layer reduces forgetting by 62 % on the most fragile model with no task cost.

## Significance  
This work provides the first theoretical threshold for intruder emergence in LoRA fine‑tuning, enabling proactive mitigation strategies that require only a single SVD per layer.  It clarifies why full fine‑tuning is less prone to forgetting and offers a practical rule—spike budget based on thresholds—that can be applied without sacrificing task performance.

## Related Concepts  
- Intruder dimensions  
- Singular value \(\sigma_{1}(BA)\)  
- Rectangular spiked‑deformation transform  
- Secular equation (exact spectrum prediction)  
- LoRA fine‑tuning  
- Catastrophic forgetting  
- Threshold crossing  
- Spike budget rule
