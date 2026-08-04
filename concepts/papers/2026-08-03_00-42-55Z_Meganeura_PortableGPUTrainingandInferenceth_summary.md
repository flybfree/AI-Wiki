# Summary: 2026-08-03_00-42-55Z_Meganeura_PortableGPUTrainingandInferencethroughVu.md
Saved: 2026-08-03 23:34
Source: 2026-08-03_00-42-55Z_Meganeura_PortableGPUTrainingandInferencethroughVu.md
Model: None

---

## Summary  
Meganeura proposes a single native compiler that can generate both training and inference code for consumer GPUs using Vulkan and Metal, eliminating the need for separate export‑conversion steps. The system builds a typed static graph with automatic differentiation, an optimizer, checkpointing support, and a memory planner that lower‑levels programs through the graphics APIs. Experiments on five matched PyTorch workloads across NVIDIA, AMD discrete GPUs, an AMD APU, Apple silicon, and an Intel iGPU demonstrate that Meganeura can achieve competitive performance while reducing binary size to 13 MiB. The approach also enables a portable deployment pipeline where a trained decoder is transferred to an Android XR app sharing the graphics queue.

## Key Contributions  
- [Finding 1] A unified static graph and optimizer produce training and inference kernels that run on Vulkan, Metal, ROCm, OpenXR, and iGPU without runtime conversion.  
- [Finding 2] Forty‑eight of fifty device‑workload‑mode cells pass both strict‑f32 and validated fast‑path gates, with only two unresolved backward‑reference issues on the APU.  
- [Finding 3] Compilation times drop from 6–96 seconds to 0.1–2.4 seconds, yielding a median training gap of 1.8× faster than torch.compile on supported GPUs.

## Methodology  
The authors constructed a portable compiler pipeline that first builds a typed static graph representing the computation graph with automatic differentiation, then applies an optimizer and memory planner to generate Vulkan or Metal kernels. The compiled binary is stripped to 13 MiB and dispatched via a profile‑driven runtime that separates strict f32 arithmetic from validated fast paths, allowing independent forward and backward passes.

## Results  
On discrete AMD GPUs, four inference workloads are within 1.10× of compiled ROCm PyTorch and three training workloads run faster; the worst training gap is 4.6× under accelerated contracts. Compilation latency ranges from 0.1 to 2.4 seconds versus 6–96 seconds for torch.compile, and the stripped binary size is 13 MiB. Dispatch profiles pin the largest gaps to convolution derivatives and attention backward passes.

## Significance  
Meganeura demonstrates that consumer graphics APIs can host a compact shared train‑to‑deploy stack, offering vendor‑competitive inference performance while drastically reducing compilation overhead and binary footprint, which is crucial for mobile and edge devices.

## Related Concepts  
typed static graph, automatic differentiation, Vulkan, Metal, ROCm, OpenXR, iGPU, checkpointing, memory planner, static analysis.
