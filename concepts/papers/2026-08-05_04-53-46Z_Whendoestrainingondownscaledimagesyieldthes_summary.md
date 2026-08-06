# Summary: 2026-08-05_04-53-46Z_Whendoestrainingondownscaledimagesyieldthesamegrad.md
Saved: 2026-08-05 23:12
Source: 2026-08-05_04-53-46Z_Whendoestrainingondownscaledimagesyieldthesamegrad.md
Model: None

---

## Summary  
The paper investigates whether training diffusion transformers on downscaled images preserves the same gradients as full‑resolution training and, if so, under which conditions this occurs. It proposes a two‑term model that explains gradient preservation: a noise‑dependent term that decays at high noise and a σ‑independent floor set by the absolute token count. By measuring the (downscale ratio, σ) map of gradient differences, the authors identify specific windows where the downscaled gradient remains within a small margin of the native one.

## Key Contributions  
- [Finding 1] The gradient preservation can be decomposed into two components: one dependent on noise level and downscale ratio, the other independent of σ.  
- [Finding 2] There exists a window (0.65 < σ < 0.95) at the 1024→768 route where the downscaled gradient stays within a small margin of the native gradient regardless of noise.  
- [Finding 3] Training LoRA adapters restricted to this route and noise window reduce training time by ~14.6 % while keeping weights near‑native.

## Methodology  
The authors analyze how scaling down latent dimensions affects the gradient signal, using a theoretical decomposition that separates a noise‑dependent term from a σ‑independent floor. They then empirically measure the (downscale ratio, σ) map of gradient error across many training steps and noise levels, extracting regions where the error is minimal.

## Results  
Theoretical analysis shows the two‑term model accurately reproduces measured gradients. Experimentally, LoRA fine‑tuning limited to the identified route and σ window cuts training time by 14.6 % while preserving weight similarity to full‑resolution training.

## Significance  
This work provides a practical guideline for reducing diffusion model training cost without sacrificing quality, enabling efficient fine‑tuning of large models through targeted downscale steps and LoRA adapters.

## Related Concepts  
Diffusion transformers, latent space scaling, gradient preservation, σ‑independent floor, token count floor, LoRA adapters, spectral premise, route analysis.
