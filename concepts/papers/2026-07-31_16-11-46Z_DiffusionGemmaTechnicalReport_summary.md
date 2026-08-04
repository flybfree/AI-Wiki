# Summary: 2026-07-31_16-11-46Z_DiffusionGemmaTechnicalReport.md
Saved: 2026-08-03 20:14
Source: 2026-07-31_16-11-46Z_DiffusionGemmaTechnicalReport.md
Model: None

---

## Summary  
The paper introduces DiffusionGemma, an open‑weight language model that leverages discrete diffusion to generate text at exceptional speed by refining blocks of 256 tokens in parallel, thereby bypassing the sequential bottleneck inherent in conventional autoregressive (AR) models. By fine‑tuning a mixture‑of‑experts Gemma‑4 architecture with 3.8 B activated and 25.2 B total parameters, DiffusionGemma achieves a new Pareto frontier that balances generation speed with model capability while preserving multimodal inputs and long‑context support.

## Key Contributions  
- DiffusionGemma refines tokens in parallel using discrete diffusion, delivering roughly 20 tokens per forward pass and about 1,500 output tokens per second on a single NVIDIA H100 GPU.  
- The two‑stage training pipeline—supervised fine‑tuning for bidirectional denoising followed by reinforcement learning guided by sampler distillation—uses less than 10 % of the original AR model’s total token budget, yet retains multimodal and long‑context capabilities.  
- DiffusionGemma establishes a new trade‑off between generation speed and quality, maintaining AR generation with only minor performance degradation.

## Methodology  
The authors adopt a fine‑tuning approach: first stage applies supervised fine‑tuning to teach the model how to denoise 256‑token blocks bidirectionally; second stage employs reinforcement learning combined with sampler distillation to jointly optimise generation quality and inference efficiency, enabling parallel refinement without full autoregressive decoding.

## Results  
Experiments show DiffusionGemma generates approximately 1,500 tokens per second on a single H100 GPU, surpassing the best state‑of‑the‑art speculative decoding. Quantitative evaluation reveals only a modest performance drop compared with pure AR generation, confirming that diffusion fine‑tuning does not severely compromise model ability.

## Significance  
This work demonstrates that diffusion can be seamlessly integrated into large language models without sacrificing speed, opening a path toward hybrid diffusion‑AR pipelines that could dramatically reduce latency in real‑time applications while preserving the original model’s capabilities.

## Related Concepts  
- Diffusion models  
- Autoregressive (AR) decoding  
- Mixture‑of‑experts architectures  
- Sampler distillation  
- Speculative decoding
