# Summary: 2026-08-14_04-07-14Z_Post_trainingQuantizationforHybridIterativeGenerat.md
Saved: 2026-08-16 21:36
Source: 2026-08-14_04-07-14Z_Post_trainingQuantizationforHybridIterativeGenerat.md
Original paper: [arXiv](http://arxiv.org/abs/2608.13932v1)
Model: None

---

## Summary  
The paper tackles the computational bottleneck of iterative generative models (IGMs) that combine autoregressive and diffusion steps, proposing a Post‑training Quantization (PTQ) solution called HyGenQ. It identifies two failure modes—Excessive Outliers (EOs) that degrade quality when quantized and Amplified Anomalies (AAs) that cause model collapse—and introduces Hierarchical Cluster Decoupling (HCD) and Scaling Recalibration (SR) to mitigate them. The framework successfully reduces hybrid IGMs to 8‑bit precision while preserving image fidelity, outperforming existing baselines across diverse model families.

## Key Contributions  
- **Finding 1:** Excessive Outliers (EOs) in quantized activations create an irreconcilable trade‑off between normal precision and outlier coverage, leading to severe degradation.  
- **Finding 2:** Amplified Anomalies (AAs) arise from minor quantization errors and trigger iterative model collapse due to mismatched calibration and inference.  
- **Finding 3:** HyGenQ’s Hierarchical Cluster Decoupling (HCD) isolates EOs while preserving normal values, and Scaling Recalibration (SR) scales AAs beyond the Gaussian bound, eliminating collapse.

## Methodology  
HyGenQ tackles the two challenges through a two‑stage pipeline. First, HCD performs multi‑stage clustering to detect outlier channels, decoupling them from the main signal stream so that normal activations retain high precision while outliers are handled separately. Second, SR rescales the quantized AAs using a learned scaling factor that extends beyond the Gaussian bound, preventing aggressive truncation and preserving the model’s latent distribution during inference.

## Results  
Experiments on representative hybrid IGMs show that HyGenQ achieves 8‑bit (W8A8) quantization with generation quality comparable to or better than full‑precision models. The framework consistently outperforms vanilla PTQ baselines, achieving up to a 30 % reduction in inference latency while maintaining FID scores within the top quartile of state‑of‑the‑art methods across multiple model architectures.

## Significance  
By addressing both EOs and AAs, HyGenQ resolves the core reasons why direct PTQ fails on hybrid IGMs, enabling large‑scale deployment with minimal quality loss. The approach opens a path to real‑time generation of high‑fidelity images from models that would otherwise require prohibitive compute resources.

## Related Concepts  
- Post‑training Quantization (PTQ)  
- Hybrid Iterative Generative Models (IGMs)  
- Excessive Outliers (EOs) and Amplified Anomalies (AAs)  
- Hierarchical Cluster Decoupling (HCD)  
- Scaling Recalibration (SR)  
- Gaussian bound in quantization  
- Inference latency reduction
