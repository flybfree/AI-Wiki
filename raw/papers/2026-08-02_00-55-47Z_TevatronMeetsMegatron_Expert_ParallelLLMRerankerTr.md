---
title: Tevatron Meets Megatron: Expert-Parallel LLM Reranker Training on an Academic Budget
published: 2026-08-02T00:55:47Z
authors: Zhichao Xu, Xueguang Ma, Shengyao Zhuang, Luyu Gao, Wenqian Ye, Yu Wang, Jamie Callan, Jimmy Lin
url: http://arxiv.org/abs/2608.00916v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tevatron Meets Megatron: Expert-Parallel LLM Reranker Training on an Academic Budget

## Abstract
Modern reranking recipes---billion-scale cross-encoders, mixture-of-experts (MoE) backbones, and distillation against strong teachers---have outpaced the training infrastructure available to most academic groups. Existing Tevatron reranker training relies on the Hugging Face Trainer with DeepSpeed or PyTorch FSDP1, but these backends lack efficient support for large-scale MoE training. We present Tevatron 3.0, which integrates a Megatron-Core training backend into Tevatron while preserving its data pipeline, evaluation workflow, and Hugging Face-compatible checkpoints. We benchmark existing distributed training configurations against the new backend, showing that Megatron matches FSDP reranker quality and training efficiency under comparable data-parallel settings, is up to 22% faster in the recommended single-node configuration, and supports both LoRA and full-parameter fine-tuning. Crucially, expert parallelism enables training a 30B-parameter Qwen3-30B-A3B MoE reranker, which is infeasible with PyTorch FSDP1. Using this framework, we conduct a controlled comparison of MoE versus dense models, LoRA versus full-parameter tuning, and distillation versus contrastive training on BEIR-15 with three first-stage retrievers, and report serving throughput for Hugging Face and vLLM. We find that the MoE reranker matches dense 8B quality while activating less than half as many parameters and achieving substantially higher inference throughput. We will release the framework and trained checkpoints.

## Metadata
- **Published**: 2026-08-02T00:55:47Z
- **Authors**: Zhichao Xu, Xueguang Ma, Shengyao Zhuang, Luyu Gao, Wenqian Ye, Yu Wang, Jamie Callan, Jimmy Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00916v1)