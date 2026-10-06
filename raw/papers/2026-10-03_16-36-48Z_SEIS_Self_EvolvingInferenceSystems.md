---
title: SEIS: Self-Evolving Inference Systems
published: 2026-10-03T16:36:48Z
authors: Zhen Xu, Jingyu Liu, Zongze Li, Tahseen Rabbani, Ce Zhang
url: http://arxiv.org/abs/2610.04646v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SEIS: Self-Evolving Inference Systems

## Abstract
Inference systems determine how fast and how cheaply language models can be served, so making them faster has direct practical value. However, prior work focuses mostly on optimizing certain parts such as kernels or memory within the large system. In this work, we take a holistic approach and apply agentic self-evolution to optimize the whole system end-to-end. Our SEIS (Self-Evolving Inference Systems) autonomously optimizes the entire mini-sglang engine without human intervention through iterative sessions with inherited experiences and code changes. Serving Qwen3-0.6B on H100, the resulting engine reaches 3.27X the throughput of the original mini-sglang implementation and beats SOTA engines like vLLM, TensorRT-LLM, and SGLang in the single-request workload. The correctness of the optimized inference engine by SEIS is tested in terms of numerical difference and downstream accuracy on math and long-context retrieval tasks. The code and session histories show that the speedup comes from redesigning the whole engine and that building on earlier sessions beats independent attempts. These results suggest that agentic self-evolution can optimize a complex system end-to-end. The evaluation also has to evolve with the engine, and letting agents evolve it is a natural next step.

## Metadata
- **Published**: 2026-10-03T16:36:48Z
- **Authors**: Zhen Xu, Jingyu Liu, Zongze Li, Tahseen Rabbani, Ce Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04646v1)