# Taming Outlier Tokens in Diffusion Transformers
Saved: 2026-05-07 22:08
Source: 2026-05-06_17-59-42Z_TamingOutlierTokensinDiffusionTransformers.md

---

## Summary
This paper studies outlier tokens in diffusion transformers used for image generation. The authors show that high-norm outlier representations appear both in pretrained ViT encoders and in the denoiser component of modern RAE-DiT pipelines, especially in intermediate layers. They argue that simply masking outliers is insufficient and instead introduce Dual-Stage Registers (DSR) to reduce outlier artifacts and improve generation quality.

## Key Takeaways
- Outlier tokens arise in both the encoder and denoiser of diffusion pipelines.
- The issue appears tied to corrupted local patch semantics, not just extreme token norms.
- Register-based interventions can improve quality across ImageNet and text-to-image generation.

## Context
The paper builds on prior observations of outlier tokens in vision transformers and extends them to generative diffusion models. It evaluates the method on large-scale image generation settings.

## Implications
Controlling token outliers may be an important lever for improving diffusion transformer robustness and sample quality. The work also suggests that token-level pathologies can propagate from pretrained encoders into generative systems.

## Original Reference
- Title: Taming Outlier Tokens in Diffusion Transformers
- Authors: Xiaoyu Wu, Yifei Wang, Tsu-Jui Fu, Liang-Chieh Chen, Zhe Gan, Chen Wei
- Published: 2026-05-06T17:59:42Z
- URL: http://arxiv.org/abs/2605.05206v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-05-06_17-59-42Z_TamingOutlierTokensinDiffusionTransformers.md