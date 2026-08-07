---
title: Beyond Rotations: AuroOFT for Expressive Quantized Orthogonal Fine-Tuning
published: 2026-08-05T16:05:13Z
authors: Yue Han, Dianlin Wang
url: http://arxiv.org/abs/2608.05253v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Rotations: AuroOFT for Expressive Quantized Orthogonal Fine-Tuning

## Abstract
Quantized orthogonal fine-tuning (qoft) enables parameter-efficient adaptation of low-bit language models by learning structured activation rotations before frozen quantized weights. However, its task-specific updates remain constrained to linear orthogonal transformations, limiting input-dependent nonlinear corrections. We introduce AuroOFT, which keeps qoft as a stable quantization-compatible branch while attaching a zero-start gated low-rank nonlinear residual to each adapted linear layer. AuroOFT maps activations into an RMS-normalized compact latent space and uses adaptive nonlinear bases with bounded or token-dependent gating. The zero-initialized up projection makes AuroOFT functionally identical to qoft at initialization, while orthogonality remains a branch-level stability property rather than a property of the combined nonlinear layer. Under matched data, optimization, decoding, and parser protocols, AuroOFT improves Macro-6 over matched qoft by 1.30-2.70% on the 1.5B/3B Qwen2.5 settings, exceeds QLoRA by 6.52-10.62%, and saves 32.3-44.7% trainable parameters relative to QLoRA in representative scales. The small exam-style multiple-choice math set is treated only as a protocol-sensitivity diagnostic. Our code is available at the anonymous repository: https://anonymous.4open.science/r/AuroOFT-F3FD.

## Metadata
- **Published**: 2026-08-05T16:05:13Z
- **Authors**: Yue Han, Dianlin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05253v1)