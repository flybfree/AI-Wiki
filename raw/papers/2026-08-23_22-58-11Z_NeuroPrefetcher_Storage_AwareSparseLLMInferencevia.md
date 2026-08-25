---
title: NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching
published: 2026-08-23T22:58:11Z
authors: Nobel Dhar, Md Romyull Islam, Xuechen Zhang, Gongjin Sun, Sahidul Islam, Bobin Deng, Kun Suo
url: http://arxiv.org/abs/2608.22643v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching

## Abstract
Deploying large language models on edge devices is increasingly limited by a widening gap between model size and available memory. Existing approaches such as quantization, smaller models, and offloading can raise the effective memory limit, but they still assume that the model can be compressed or partitioned to fit within some budget. We target the harder model-exceeds-memory setting, in which the model remains larger than resident memory throughout execution and storage becomes an active source of weights on the critical path. We observe that MLP activity during autoregressive decoding has strong temporal locality: approximately 82-85% of active neurons persist from one token to the next. This means that most sparse weights needed for the current token are already resident, and only the newly needed rows must be fetched from storage. We present NeuroPrefetcher, a storage-backed LLM inference system that exploits this property through predictive delta prefetching. After layer 0, a single GPU-resident predictor, occupying 2.86% of base model parameters, predicts sparse activity for all downstream MLP layers in one forward pass. The runtime compares these predictions against resident GPU buffers and issues application-scheduled NVMe reads only for incoming delta rows, replacing reactive operating-system demand paging with explicit, model-aware weight movement. On real unified-memory edge hardware, NeuroPrefetcher achieves 7.9-12.0x speedup over llama.cpp across constrained memory budgets.

## Metadata
- **Published**: 2026-08-23T22:58:11Z
- **Authors**: Nobel Dhar, Md Romyull Islam, Xuechen Zhang, Gongjin Sun, Sahidul Islam, Bobin Deng, Kun Suo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22643v1)