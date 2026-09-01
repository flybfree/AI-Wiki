---
title: Partition-Aware Unlearning for Removing Spurious Correlations in Large Vision-Language Models
published: 2026-08-30T19:42:47Z
authors: Aditi Sarker, Nazreen Shah, Rafi Ibn Sultan, Rhongho Jang, Dongxiao Zhu, Prashant Khanduri
url: http://arxiv.org/abs/2608.29996v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Partition-Aware Unlearning for Removing Spurious Correlations in Large Vision-Language Models

## Abstract
Large Vision-Language Models (LVLMs) achieve strong performance across many multimodal tasks; however, they often exploit spurious object-background correlations, resulting in predictions driven by contextual shortcuts rather than object-relevant visual evidence. Despite growing interest in hallucination and robustness evaluation, existing benchmarks provide limited control over whether model predictions are grounded in the target object or induced by correlated background cues. In this work, we introduce PURGE (\underline{P}artition-aware \underline{U}nlearning for \underline{R}emoving spurious-correlation \underline{G}enerated \underline{E}rrors), a framework for constructing, benchmarking, and mitigating spurious-correlation-induced failures in LVLMs. The framework consists of: -- (1) Structured dataset construction wherein we develop three complementary structured data construction strategies that partition examples by object-relevant evidence and spurious background cues, enabling controlled diagnosis of shortcut reliance; and -- (2) Partition-aware unlearning, which uses these partitions to selectively remove spurious object-background associations while preserving object-based reasoning. We evaluate the \algo~framework across multiple LVLMs, including LLaVA-1.6-7B, Qwen3-VL-8B-Instruct, and Qwen3.5-9B, together with CLIP as a vision-language encoder, on a diverse suite of benchmarks, including CHAIR, POPE, Causal-HalBench, MM-SpuBench, AMBER, MMHal, and Waterbirds. Our results show that PURGE consistently reduces hallucinations and spurious-correlation-driven errors while maintaining or improving overall performance in most evaluated settings, providing both a reusable evaluation protocol and an effective mitigation framework for more reliable LVLMs.

## Metadata
- **Published**: 2026-08-30T19:42:47Z
- **Authors**: Aditi Sarker, Nazreen Shah, Rafi Ibn Sultan, Rhongho Jang, Dongxiao Zhu, Prashant Khanduri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29996v1)