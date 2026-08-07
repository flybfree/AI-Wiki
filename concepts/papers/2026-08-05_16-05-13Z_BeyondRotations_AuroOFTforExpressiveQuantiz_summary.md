# Summary: 2026-08-05_16-05-13Z_BeyondRotations_AuroOFTforExpressiveQuantizedOrtho.md
Saved: 2026-08-06 21:48
Source: 2026-08-05_16-05-13Z_BeyondRotations_AuroOFTforExpressiveQuantizedOrtho.md
Model: None

---

## Summary  
Quantized orthogonal fine‑tuning (qoft) offers a parameter‑efficient way to adapt low‑bit language models by learning structured activation rotations, but its task‑specific updates are limited to linear transformations and cannot capture input‑dependent nonlinearities. AuroOFT extends this framework by attaching a zero‑initialized gated low‑rank residual to each adapted linear layer, enabling expressive corrections while preserving the orthogonality of the quantization branch. The method maps activations into an RMS‑normalized compact latent space using adaptive nonlinear bases with either bounded or token‑dependent gating, thereby improving macro‑6 performance on large Qwen2.5 models without sacrificing quantisation compatibility.

## Key Contributions  
- [Finding 1] AuroOFT introduces a zero‑start gated low‑rank residual that provides task‑specific nonlinear updates while keeping the qoft branch unchanged at initialization, thus maintaining functional equivalence to pure qoft.  
- [Finding 2] The method maps activations into an RMS‑normalized compact latent space using adaptive nonlinear bases with bounded or token‑dependent gating, allowing input‑dependent corrections without breaking orthogonality.  
- [Finding 3] Empirically AuroOFT improves macro‑6 by 1.30–2.70% over matched qoft on the 1.5B/3B Qwen2.5 settings, exceeds QLoRA performance by 6.52–10.62%, and reduces trainable parameters by 32.3–44.7% relative to QLoRA.

## Methodology  
The authors address the limitation of qoft’s linear orthogonal updates by preserving a stable quantization‑compatible branch while adding a zero‑initialized gated low‑rank residual per adapted layer. Each residual projects activations into an RMS‑normalized compact latent space, where adaptive nonlinear bases are employed; these bases can be either globally bounded or token‑specific, providing flexibility in the correction magnitude. Orthogonality is retained as a property of the qoft branch alone, not as a consequence of the combined nonlinear layer, ensuring that the quantised weights remain orthogonal throughout training.

## Results  
On the representative 1.5B and 3B Qwen2.5 models, AuroOFT achieves macro‑6 improvements of 1.30–2.70% compared with matched qoft. It surpasses QLoRA by 6.52–10.62% in performance while saving 32.3–44.7% trainable parameters relative to QLoRA, demonstrating both efficiency and effectiveness.

## Significance  
AuroOFT bridges the gap between parameter‑efficient fine‑tuning and expressive adaptation, offering a pathway to higher accuracy with far fewer trainable parameters. By decoupling orthogonality from the nonlinear residual, it maintains quantisation stability while enabling input‑dependent corrections that linear orthogonal updates cannot provide.

## Related Concepts  
- Quantized orthogonal fine‑tuning (qoft)  
- QLoRA (low‑rank adaptation of large language models with 8‑bit quantisation)  
- RMS‑normalization and compact latent space mapping  
- Low‑rank residual networks  
- Gated nonlinear bases and token‑dependent gating
