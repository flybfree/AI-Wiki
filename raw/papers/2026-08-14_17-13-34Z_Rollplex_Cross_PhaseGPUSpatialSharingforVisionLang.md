---
title: Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training
published: 2026-08-14T17:13:34Z
authors: Hanfeng Lu, Tianyu Feng, Suyi Li, Yuheng Zhao, Wei Gao, Shaopan Xiong, Ju Huang, Siran Yang, Jiamang Wang, Lin Qu, Wei Wang
url: http://arxiv.org/abs/2608.14498v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training

## Abstract
Vision-language models (VLMs) enable embodied agents to reason and act from visual observations and language instructions. Reinforcement learning (RL) post-training enhances these capabilities using task feedback, but current on-policy RL runtimes execute rollout, reference scoring, and actor training in strict serial phases. While effective for text-only RL, this phase-granular execution is wasteful for VLMs, where processing dense video inputs and prompt prefixes occupies a large fraction of each phase. Because prefix processing is independent of the generated response, it can be run alongside rollout decoding, which leaves GPU compute capacity underutilized, without breaking synchronous on-policy semantics.   We present Rollplex, a runtime that decomposes the reference and training phase and moves the prefix computation into the rollout decode window. Realizing this schedule requires more than concurrent kernel launches: naive colocation of Qwen2.5-VL-32\,B requires roughly 165\,GiB per GPU, while rollout and training prefer different tensor-parallel (TP) degrees and weight layouts. Rollplex addresses these constraints with two mechanisms. Phase-aware memory management controls HBM residency according to producer--consumer lifetimes. Parallelism-aware weight sharing uses the same physical storage for layout-compatible tensors across distinct TP degrees and reconstructs only incompatible tensors, avoiding a complete second actor copy. On 32 H800 GPUs, Rollplex achieves $1.23\times$--$1.30\times$ speedup over serial colocation and $1.57\times$--$2.24\times$ over disaggregation under the same GPU budget, while preserving the synchronous RL update.

## Metadata
- **Published**: 2026-08-14T17:13:34Z
- **Authors**: Hanfeng Lu, Tianyu Feng, Suyi Li, Yuheng Zhao, Wei Gao, Shaopan Xiong, Ju Huang, Siran Yang, Jiamang Wang, Lin Qu, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14498v1)