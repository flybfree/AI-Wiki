---
title: Amplifying Latency and Cost of LLM Inference via Rowhammer Attack
url: http://arxiv.org/abs/2610.30798v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_06-24-35Z_AmplifyingLatencyandCostofLLMInferenceviaRowhammer.md
generated_at: 2026-10-22 22:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces LLVMhammer, the first Rowhammer attack that degrades GPU-based LLM inference performance by inducing a bit-flip in Triton's MLIR/LLVM-based compilation pipeline. The attack causes Triton to generate a functionally correct but suboptimal GPU kernel, leading to persistent inference slowdowns of 4–16% across multiple LLMs and GPU vendors, while also demonstrating the potential to corrupt model outputs with BERTScore reductions as low as 25%.

## Key Takeaways
- A single Rowhammer-induced bit-flip in a performance-critical optimization pass within Triton's compilation pipeline causes the JIT compiler to emit a functionally identical but suboptimal GPU kernel. Because Triton caches generated kernels on disk, the degraded kernel persists across all subsequent inference executions, making the slowdown permanent rather than transient.
- The attack is GPU vendor-agnostic because Triton's target-independent compilation stages are shared across vendors. The authors evaluate LLVMhammer on both NVIDIA RTX 4090 and AMD RX 7900 XTX GPUs across diverse models including Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, and Deepseek-llm-7b-chat, confirming broad applicability.
- The authors develop Karnage, a tool that automatically isolates exploitable bit-flip locations in Triton's target-independent pipeline without requiring manual inspection, enabling systematic identification of vulnerable optimization passes. Beyond latency amplification, LLVMhammer can corrupt LLM outputs, reducing BERTScore to as low as 25%, revealing security implications beyond mere performance degradation.

## Context
Rowhammer attacks have historically been studied in the context of memory corruption in operating systems, databases, and security-sensitive applications. This paper extends the threat model into the domain of AI infrastructure, specifically targeting the just-in-time compilation toolchains (Triton, MLIR, LLVM) that underpin modern GPU-accelerated LLM serving. As LLM inference increasingly relies on JIT-compiled kernels for performance, the integrity of the compilation pipeline becomes a critical attack surface. The work bridges hardware-level DRAM vulnerabilities with software-level compiler correctness, a connection that had not been previously explored in the LLM serving literature.

## Implications
For practitioners operating multi-GPU LLM inference servers, a 4–16% latency increase per GPU can compound into substantial annual operating cost penalties at fleet scale, particularly in cloud and data-center deployments where energy and time budgets are tightly constrained. The finding that a single hardware-level bit-flip can silently degrade performance without altering output correctness means traditional correctness-based monitoring may fail to detect such regressions, motivating the need for performance-integrity monitoring in production LLM serving stacks. Additionally, the demonstrated ability to corrupt outputs (BERTScore dropping to 25%) elevates Rowhammer from a performance concern to a potential security and reliability threat for AI systems deployed in safety-critical or regulated environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30798v1)
