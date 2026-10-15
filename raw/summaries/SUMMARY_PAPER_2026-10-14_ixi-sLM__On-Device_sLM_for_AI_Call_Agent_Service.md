---
title: ixi-sLM: On-Device sLM for AI Call Agent Service
url: http://arxiv.org/abs/2610.19382v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_01-29-08Z_ixi_sLM_On_DevicesLMforAICallAgentService.md
generated_at: 2026-10-14 20:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ixi-sLM, a 1.2-billion-parameter Korean small language model adapted for on-device execution on mobile NPUs to power AI call agent services. Through a technique the authors call ON-DEVICE MODELING—combining domain-adaptive vocabulary trimming with task-aware mixed-precision quantization—the model achieves 94% of a state-of-the-art cloud LLM's task-weighted quality while fitting within an 803 MiB memory budget and consuming only 23% of the CPU's per-call energy. The deployed system serves several million ixi-O subscribers across Qualcomm and Apple NPUs in production.

## Key Takeaways
- Domain-adaptive modeling trims the model's vocabulary by call frequency to shrink the embedding layer and LM head, which together consume nearly half the model under INT4 transformer weights. The tokenizer is refit specifically for call speech, reducing token counts by 18% on real call traffic, which directly addresses the mismatch between Korean STT input and sLM pretraining distributions.
- Task-aware quantization calibrates precision assignments on actual call data rather than generic benchmarks, assigning per-module mixed precision based on activation sensitivity. This allows the 1.2B model to compress to 803 MiB (28% of its FP16 footprint) while maintaining a marginal quality drop on the NPU, preserving 94% of cloud-LLM task-weighted quality across two production services: AI Call Summary and AI Call Answering.
- The on-device deployment satisfies hard mobile constraints—approximately 1 GiB memory budget, in-call latency and thermal limits, and static-integer NPU execution—while remaining network-independent and free of per-query cloud costs. The same modeling recipe transfers across heterogeneous hardware (Qualcomm and Apple NPUs), demonstrating portability of the approach.

## Context
On-device inference for language models has long been constrained by the tension between model quality and the strict memory, latency, thermal, and integer-only execution limits of mobile NPUs. Most prior work focuses on generic quantization or pruning without adapting the model's structural components—such as vocabulary and tokenizer—to the target domain. This paper addresses a concrete production scenario: Korean-language call agents where STT input diverges significantly from pretraining distributions, and where cloud-level quality expectations must be met without cloud connectivity. It represents one of the first documented cases of a sub-1.5B-parameter language model serving millions of real users on heterogeneous mobile NPUs in a commercial service.

## Implications
For practitioners building on-device AI services, this work demonstrates that domain-specific structural modifications (vocabulary trimming, tokenizer refitting) combined with activation-aware quantization can close the quality gap between cloud and edge inference far more effectively than generic compression alone. For the industry, it validates a path toward privacy-preserving, offline-capable AI agents that eliminate per-query cloud costs and network dependencies, potentially reshaping how call-center automation and voice assistants are deployed at scale. For the research community, the cross-platform deployment recipe across Qualcomm and Apple NPUs offers a transferable blueprint for adapting small language models to constrained hardware without sacrificing production-grade quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19382v1)
