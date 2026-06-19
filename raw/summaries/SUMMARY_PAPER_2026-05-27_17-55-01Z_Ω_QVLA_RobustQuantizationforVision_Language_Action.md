---

title: "Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling"
url: http://arxiv.org/abs/2605.28803v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-27_17-55-01Z_Ω_QVLA_RobustQuantizationforVision_Language_Action.md
generated_at: "2026-06-11 10:48"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces Omega-QVLA, a training‑free post‑training quantization method that compresses both the language backbone and the diffusion action head of Vision‑Language‑Action models to uniform W4A4 precision. On benchmark tasks it achieves task success rates comparable to FP16 baselines while cutting static memory usage by over 70 %.

## Key Takeaways
- Omega-QVLA replaces mixed‑precision allocation with a single uniform quantization, eliminating the instability previously blamed on compressing only the action head.
- The composite SVD‑Hadamard rotation equalizes per‑channel weight energy and diffuses residual activation outliers across diffusion steps.
- Per‑step DiT activation scaling quantization absorbs dynamic‑range drift, preserving accuracy throughout denoising.

## Context
Vision‑Language‑Action systems aim to integrate perception, reasoning, and control in a single model, but their large diffusion components hinder on‑device deployment. Prior quantization approaches either leave the action head untouched or rely on mixed precision, which is impractical for edge devices.

## Implications
The uniform W4A4 scheme enables true low‑memory inference without sacrificing performance, opening the door to real‑time manipulation in resource‑constrained environments and encouraging broader adoption of fully quantized VLA models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.28803v1)
