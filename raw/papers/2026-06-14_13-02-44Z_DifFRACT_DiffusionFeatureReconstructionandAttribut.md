---

title: "DifFRACT: Diffusion Feature Reconstruction and Attribution for Circuit Tracing"
published: "2026-06-14T13:02:44Z"
authors: Artyom Mazur, Nina Konovalova, Aibek Alanov
url: http://arxiv.org/abs/2606.15796v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# DifFRACT: Diffusion Feature Reconstruction and Attribution for Circuit Tracing



**Source**: [Original Paper](http://arxiv.org/abs/2606.15796v1)
## Abstract
Mechanistic interpretability seeks to explain neural network behavior by decomposing model computations into interpretable features and circuits. While transcoder-based circuit tracing has recently enabled detailed causal analyses of large language models, multimodal diffusion transformers for image generation remain comparatively opaque. We still lack tools for understanding how semantic information propagates across denoising steps and how text and image representations interact within double-stream MM-DiT architectures. Existing methods provide only partial insight: attention maps expose a limited view of token interactions, while sparse autoencoders can discover interpretable features but do not directly reveal how these features are transformed and composed through nonlinear MLP layers. In this work, we extend transcoder-based circuit tracing to multimodal diffusion transformers. We train timestep-conditioned transcoders that faithfully approximate the input-output behavior of MLP sublayers in FLUX.1[schnell]. By replacing MLPs with transcoders and linearizing the remaining computation, we obtain exact feature-to-feature attribution and recover compact, interpretable circuits. Empirically, our transcoders match or slightly outperform sparse autoencoders on the sparsity-faithfulness tradeoff. The resulting circuits reveal mechanisms underlying attribute binding and cross-stream semantic propagation, and provide causal explanations for systematic generation errors. Moreover, circuit-guided interventions are substantially more precise and effective than standard SAE-based steering. Our results demonstrate that transcoder-based circuit analysis is feasible for state-of-the-art diffusion transformers and provides a powerful framework for understanding and controlling multimodal generative models. The code is available at https://github.com/Artalmaz31/DifFRACT

## Metadata
- **Published**: 2026-06-14T13:02:44Z
- **Authors**: Artyom Mazur, Nina Konovalova, Aibek Alanov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.15796v1)