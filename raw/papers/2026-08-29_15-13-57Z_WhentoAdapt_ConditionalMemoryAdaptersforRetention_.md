---
title: When to Adapt: Conditional Memory Adapters for Retention-Preserving Domain Specialization
published: 2026-08-29T15:13:57Z
authors: Jiayu Hou, Lei Wang
url: http://arxiv.org/abs/2608.29327v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When to Adapt: Conditional Memory Adapters for Retention-Preserving Domain Specialization

## Abstract
Large language models deployed in specialized domains must improve in-domain performance without sacrificing general capabilities. Existing parameter-efficient fine-tuning methods are typically always on: their learned perturbations are applied to every input, which can degrade out-of-domain (OOD) performance. We propose Engram Adapter, a framework that repurposes pretraining-time conditional memory as a post-hoc adapter for frozen LLMs. It uses multi-channel matching over local n-gram patterns with explicit occupancy tracking as a lightweight selectivity prior, making residual injection more likely on in-domain inputs while a learned scalar gate suppresses incoherent OOD retrievals. We evaluate on Qwen3-4B and Qwen3-8B with AG-News and MedMCQA as adaptation tasks and OOD benchmarks spanning reasoning, translation, code generation, and legal reasoning. Engram Adapter improves in-domain accuracy while preserving 99.4%--100.1% of average OOD performance; on LegalBench it slightly exceeds the frozen base model on average, whereas comparable always-on baselines degrade sharply. Mechanistic analyses show that although OOD activations are non-zero, gate and projection attenuation reduce residuals to approximately 0.08% of hidden-state norm, yielding small KL drift and negligible accuracy change. These results suggest conditional activation is a promising route toward modular, retention-preserving domain specialization over frozen backbones.

## Metadata
- **Published**: 2026-08-29T15:13:57Z
- **Authors**: Jiayu Hou, Lei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29327v1)