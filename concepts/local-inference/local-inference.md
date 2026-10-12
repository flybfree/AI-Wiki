---
title: "Local Inference Engines and Serving Stacks"
date: 2026-10-11
tags: [local-inference, self-hosted, llama-cpp, ollama, vllm, lm-studio, strata, ninfer]
---

# Local Inference Engines and Serving Stacks

## Summary

Local inference is the practice of running model inference on hardware controlled by the user or organization rather than sending every request to a hosted API. The current ecosystem is separating into several layers:

- **Desktop and developer runtimes**: Ollama and LM Studio optimize for setup speed and experimentation.
- **Portable low-level runtimes**: llama.cpp provides broad hardware support, GGUF execution, CPU/GPU hybrid inference, and fine-grained memory control.
- **Production serving engines**: vLLM emphasizes batching, concurrency, and throughput.
- **Specialized next-generation engines**: Strata focuses on fitting large models across heterogeneous consumer memory, while NInfer focuses on high-performance Qwen serving and agent-oriented APIs.

The right choice depends on workload, hardware, concurrency, context length, and whether the goal is experimentation, a personal assistant, or a multi-agent service.

## Runtime Comparison

| Runtime | Primary strength | Best fit | Main tradeoff |
|---|---|---|---|
| [Ollama](https://github.com/ollama/ollama) | Fastest setup and model management | CLI users, local development, simple services | Less control over advanced serving behavior |
| [LM Studio](https://lmstudio.ai/) | GUI workflow and easy local API | Desktop experimentation and model testing | Limited production-oriented concurrency controls |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Portability and memory control | CPU/GPU hybrid systems, edge devices, constrained VRAM | More operational tuning than Ollama or LM Studio |
| [vLLM](https://github.com/vllm-project/vllm) | Batching and concurrent serving | Multi-user and multi-agent GPU services | More complex deployment and GPU requirements |
| [Strata](https://github.com/Niko1221/Strata) | Heterogeneous memory placement | Large local models on consumer hardware | Young project with hardware- and model-specific behavior |
| [NInfer](https://github.com/Neroued/ninfer) | Specialized serving performance | Qwen workloads, long context, concurrent agent APIs | CUDA-oriented and narrower than general runtimes |

## Strata

[Strata](https://stratat.com/) is a local inference engine targeting Windows and Linux systems with NVIDIA and AMD GPUs. Its central idea is to distribute model state across **VRAM**, system RAM, and NVMe storage so users can attempt larger models without relying only on increasingly aggressive quantization.

### Design emphasis

- Heterogeneous memory placement across GPU memory, system memory, and NVMe.
- Support for consumer hardware, including NVIDIA and AMD systems.
- OpenAI-compatible API integration for applications and coding agents.
- Positioning around large Qwen-family models and other models that exceed ordinary GPU memory.
- Hardware-specific optimization rather than one fixed performance profile.

### Practical role

Strata is best understood as a **memory-capacity and consumer-hardware reach** project. It is interesting when the constraint is not merely tokens per second, but whether a model can fit and remain usable on available hardware.

Treat performance figures as project claims until independently reproduced on the target model, quantization, context length, and hardware. Memory capacity does not automatically imply low latency.

## NInfer

[NInfer](https://github.com/Neroued/ninfer) is a C++/CUDA local serving engine focused on high-performance Qwen-family inference and agent-facing APIs.

### Reported capabilities

- Long-context inference.
- Concurrent requests and continuous batching.
- Speculative decoding.
- OpenAI-compatible and Anthropic-compatible interfaces.
- GPU-oriented optimization for Qwen-family workloads.
- [NInfer Studio](https://github.com/Neroued/ninfer) for model management, vision chat, coding-agent workflows, throughput metrics, and GPU presets.

### Practical role

NInfer is best understood as a **serving-throughput and kernel-optimization** project. It is more relevant when one local model must serve multiple users, coding agents, or concurrent requests than when the goal is simply to launch a model from a desktop GUI.

As with Strata, benchmark claims should be validated against the exact model, context length, batch size, quantization, GPU, and API workload.

## How They Fit Together

The projects solve different bottlenecks:

- **Ollama** solves installation and model-management friction.
- **LM Studio** solves GUI-based experimentation.
- **llama.cpp** solves portability and fine-grained local execution.
- **vLLM** solves high-throughput serving at established production scale.
- **Strata** attacks the memory-capacity problem by using more of the local memory hierarchy.
- **NInfer** attacks the serving-performance problem through specialized kernels and concurrency features.

The emerging pattern is a layered local stack:

```text
Agent or application
        |
OpenAI-compatible API
        |
Runtime selected by workload
  |       |        |        |
Strata  NInfer  llama.cpp  vLLM
        |
GPU VRAM + system RAM + NVMe
```

## Selection Guide

- Choose **Ollama** when setup speed matters most.
- Choose **LM Studio** when exploring models interactively on a desktop.
- Choose **llama.cpp** when hardware support, CPU/GPU splitting, GGUF control, or edge deployment matters.
- Choose **vLLM** when multiple users or agents need concurrent GPU serving.
- Evaluate **Strata** when the main problem is fitting a large model across available consumer memory.
- Evaluate **NInfer** when the main problem is serving Qwen models efficiently to concurrent agents or applications.

## Evaluation Checklist

Do not compare local runtimes using a single tokens-per-second number. Measure:

1. Time to first token.
2. Prompt-processing speed.
3. Decode speed.
4. Concurrent-request throughput.
5. Peak VRAM, RAM, and NVMe usage.
6. Context-window stability.
7. Tool-calling and structured-output reliability.
8. Startup time and model-switching cost.
9. API compatibility with the target agent framework.
10. Energy use and tokens per watt.

## Related Concepts

- [[concepts/self-improving-ai-loops/2026-06-10_Lesson2_InferenceLayer.md|Inference Layer: Self-Hosted LLMs]]
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson3_AbstractionLayer.md|Abstraction Layer: Model Swapping & Normalization]]
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson8_DIYArchitecture.md|DIY Architecture]]
- [[concepts/frameworks/unsloth.md|Unsloth]]

## Sources

- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Ollama](https://github.com/ollama/ollama)
- [LM Studio](https://lmstudio.ai/)
- [vLLM](https://github.com/vllm-project/vllm)
- [Strata](https://github.com/Niko1221/Strata)
- [Strata project site](https://stratat.com/)
- [NInfer](https://github.com/Neroued/ninfer)
- [Mozilla AI local-server benchmarking](https://blog.mozilla.ai/benchmarking-local-llm-servers-llama-cpp-llamafile-lm-studio-and-ollama/)

## Revision History

- **2026-10-11**: Created the local inference hub and added Strata and NInfer as specialized runtime projects.
