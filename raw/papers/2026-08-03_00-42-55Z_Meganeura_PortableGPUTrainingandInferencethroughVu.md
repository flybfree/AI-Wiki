---
title: Meganeura: Portable GPU Training and Inference through Vulkan and Metal
published: 2026-08-03T00:42:55Z
authors: Dzmitry Malyshau
url: http://arxiv.org/abs/2608.01563v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Meganeura: Portable GPU Training and Inference through Vulkan and Metal

## Abstract
Training and deployed inference often cross export, conversion, and platform-specific runtime boundaries. Meganeura asks whether one compact native compiler can span both phases on consumer GPUs. Its typed static graph, automatic differentiation, optimizer, checkpoint, memory planner, and runtime lower specialized programs through Vulkan and Metal.   We compare five matched workloads with PyTorch on NVIDIA and AMD discrete GPUs, an AMD APU, Apple silicon, and an Intel iGPU. The protocol separates strict f32 from validated fast paths and gates forward and backward independently. Forty-eight of 50 device-workload-mode cells pass both gates; the other two share one unresolved backward-reference disagreement on a newly supported APU. In strict f32, Meganeura wins 12 of 20 GPU-referenced minimal-latency cells and has a median valid training gap of 1.8x. On the discrete AMD GPU, four of five inference workloads are within 1.10x of compiled ROCm PyTorch and three training workloads are faster. Under accelerated contracts, the worst training gap is 4.6x.   Compilation takes 0.1-2.4 seconds versus 6-96 seconds for torch.compile on supported GPU paths; the stripped binary is 13 MiB. Dispatch profiles localize the largest gaps to convolution derivatives and attention backward. A physical Android XR case study transfers a Meganeura-trained decoder into an Adreno/OpenXR application sharing the graphics queue. The results show that general consumer graphics APIs can support a compact shared train-to-deploy stack at useful, sometimes vendor-competitive performance. The measured gaps point to kernel coverage, scheduling, and arithmetic policy rather than an identified API limitation.

## Metadata
- **Published**: 2026-08-03T00:42:55Z
- **Authors**: Dzmitry Malyshau
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01563v1)