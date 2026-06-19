---

title: "TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload"
url: http://arxiv.org/abs/2605.20179v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-19_17-59-08Z_TIDE_EfficientandLosslessMoEDiffusionLLMInferencew.md
generated_at: "2026-06-11 10:43"
model: nvidia/nemotron-3-nano-4b

---


## Summary
TIDE proposes a resource‑efficient inference system for diffusion large language models that exploits the temporal stability of expert activations during block processing to schedule expert refreshes in an I/O‑aware manner. By solving an optimization problem, it minimizes both I/O traffic and CPU computation while remaining lossless and requiring no model training. On a GPU‑CPU system TIDE achieves up to 1.4× throughput improvement on LLaDA2.0‑mini and 1.5× on LLaDA2.0‑flash.

## Key Takeaways
- TIDE leverages the temporal stability of expert activations within a block to propose an interval‑based refresh strategy that updates expert placement in an I/O‑aware fashion.
- It formulates inference scheduling as a mathematical programming problem to minimize I/O traffic and CPU computation, providing lossless optimization without any training.
- On a GPU‑CPU system TIDE delivers up to 1.4× and 1.5× throughput improvements over prior baselines on LLaDA2.0‑mini and LLaDA2.0‑flash.

## Context
Diffusion LLMs offer parallel block‑level decoding that can improve hardware utilization, yet scaling them with MoE architectures creates I/O bottlenecks on limited devices. This work addresses the trade‑off between compute and storage constraints inherent in large model deployment.

## Implications
The findings enable efficient inference of massive diffusion models on resource‑constrained hardware, lowering operational costs and supporting real‑time applications. Practitioners can adopt TIDE’s scheduling approach to maximize throughput without retraining or additional hardware investments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.20179v1)
