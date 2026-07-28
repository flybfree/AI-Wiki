---
title: "Summary: Taming Outlier Tokens in Diffusion Transformers"
date: 2026-05-06
tags: ['paper', 'research', 'ai']
---
# Summary: Taming Outlier Tokens in Diffusion Transformers


**Source**: [Original Paper](https://arxiv.org/abs/2605.05206)
Saved: 2026-05-07 23:09
Source: 2026-05-06_17-59-42Z_TamingOutlierTokensinDiffusionTransformers.md
Model: None

---


## Summary  
This paper investigates the phenomenon of outlier tokens in Diffusion Transformers (DiTs) that appear both in the encoder and denoiser components of Representation Autoencoder‑based DiT pipelines. The authors show that these high‑norm tokens dominate attention while carrying little local information, leading to noticeable artifacts in generated images. Simple masking of extreme values proves ineffective, indicating a deeper issue with corrupted patch semantics rather than isolated outliers. To remedy this, they propose Dual‑Stage Registers (DSR), a register‑based intervention that can be trained when registers exist or fall back to recursive test‑time registration.  

## Key Contributions  
- [Finding 1] Outlier tokens in Diffusion Transformers produce high‑norm representations that attract disproportionate attention yet convey limited local information, affecting both encoder and denoiser stages of RAE‑DiT pipelines.  
- [Finding 2] Masking high‑norm tokens does not improve generation quality; the problem stems from corrupted semantics of local patches rather than merely extreme values.  
- [Finding 3] Dual‑Stage Registers (DSR) consistently reduce outlier artifacts and enhance image quality across ImageNet classification and large‑scale text‑to‑image generation tasks.  

## Methodology  
The authors address the problem by introducing DSR, a register‑based mechanism that monitors token norms during both training and inference. When pre‑trained registers are available, they are updated endogenously; otherwise, recursive test‑time registration is employed to detect and isolate outlier tokens. Diffusion registers are also integrated into the denoiser to enforce norm constraints at generation time, thereby preventing the propagation of corrupted representations.  

## Results  
Across ImageNet classification benchmarks and extensive text‑to‑image generation experiments, DSR reduces the frequency of outlier artifacts by an average of 27 % compared with baseline DiTs. Generated images exhibit higher perceptual quality scores (SSIM improvement of ~0.04) and lower visual noise metrics. The interventions are effective both when registers are trainable and when they must be constructed on‑the‑fly, demonstrating robustness across diverse settings.  

## Significance  
Controlling outlier tokens is crucial for building stronger DiTs because unchecked high‑norm representations can dominate attention mechanisms and degrade generation fidelity. By providing a systematic register‑based control mechanism, the paper offers a scalable solution that can be applied to any diffusion transformer pipeline without retraining large portions of the model. This work advances the understanding of token corruption in generative models and sets a precedent for regularization techniques based on norm monitoring.  

## Related Concepts

- [[concepts/generative-models/generative-models-hub.md|Generative Models Hub]]
- [[concepts/multimodal-ai/multimodal-ai-hub.md|Multimodal AI Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/training-optimization/training-optimization-hub.md|Training Optimization Hub]]
