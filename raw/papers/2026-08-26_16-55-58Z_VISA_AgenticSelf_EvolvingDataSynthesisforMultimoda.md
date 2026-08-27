---
title: VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following
published: 2026-08-26T16:55:58Z
authors: Min Zeng, Guanxin Tan, Libin Cen, Yawei Wen, Rui Hu, Liuyang Bian, Xiaolong Chen, Xiaoxin Chen
url: http://arxiv.org/abs/2608.26013v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following

## Abstract
Multimodal instruction-following models require training data that is accurate, diverse, verifiable, and challenging. Existing synthesis pipelines typically follow a one-pass generate-and-filter paradigm, discarding feedback from failed samples, verifier outcomes, and target-model errors. We present VISA (Visual Instruction Synthesis Agent), an agentic framework that reformulates multimodal instruction synthesis as a self-evolving loop. At each round, VISA analyzes an image to filter incompatible constraints and discover new verifiable ones, samples diversity- and difficulty-aware constraint sets from persistent memory, generates candidate instructions, and verifies the resulting samples with executable tools and structured large language model judges. Failed samples trigger diagnostic-guided recovery, while accepted samples are probed against the target model to estimate difficulty. The resulting verifier signals and target-model failure profiles are written back to memory, allowing subsequent rounds to adaptively expand the constraint space, reduce template repetition, and focus on unresolved model weaknesses. The same verifier contracts further provide reward signals for reinforcement learning without a separately trained reward model. Experiments on MM-IFEval show that VISA consistently improves multimodal instruction following over strong baselines, while preserving general multimodal capability across seven public benchmarks.

## Metadata
- **Published**: 2026-08-26T16:55:58Z
- **Authors**: Min Zeng, Guanxin Tan, Libin Cen, Yawei Wen, Rui Hu, Liuyang Bian, Xiaolong Chen, Xiaoxin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26013v1)