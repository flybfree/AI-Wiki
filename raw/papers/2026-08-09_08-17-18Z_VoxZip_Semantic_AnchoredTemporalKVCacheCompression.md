---
title: VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference
published: 2026-08-09T08:17:18Z
authors: Wenxu Jia, Dongjie Fu, Xize Cheng, Fangming Feng, Linjun Li, Wenshi Chen, Yingming Li, Zhou Zhao, Tao Jin
url: http://arxiv.org/abs/2608.08569v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference

## Abstract
Recent advancements in Speech Large Language Models have demonstrated remarkable capabilities in understanding complex audio tasks. Despite this progress, their long-context inference remains severely bottlenecked by prohibitive KV cache memory demands. Existing text-centric compression methods struggle here, often disrupting speech continuity or discarding crucial semantic cues. To address this, we propose VoxZip, a train-free, two-stage semantic-anchored KV cache compression framework. The first stage uses automatic speech recognition (ASR) transcriptions as explicit semantic anchors to temporally align, compress, and fuse audio tokens, significantly reducing the initial KV cache while elevating token information density. To further improve the compression ratio, the second stage employs a dynamic filtering strategy based on temporally decayed accumulated attention to evict non-essential tokens while mitigating early-token bias. Comprehensive evaluations on Qwen3-Omni across six diverse audio benchmarks demonstrate the superiority of our approach. VoxZip excels in long-audio reasoning and consistently maintains high-fidelity perception on short-form tasks. Notably, it sustains over 90\% of the uncompressed baseline performance even under an aggressive 20x KV cache compression in long-context scenarios. Furthermore, at a 4x compression ratio, VoxZip yields a 1.9x increase in inference throughput alongside a 3.3x reduction in peak memory overhead. Code and models will be available at https://github.com/MM-Speech/VoxZip.

## Metadata
- **Published**: 2026-08-09T08:17:18Z
- **Authors**: Wenxu Jia, Dongjie Fu, Xize Cheng, Fangming Feng, Linjun Li, Wenshi Chen, Yingming Li, Zhou Zhao, Tao Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08569v1)