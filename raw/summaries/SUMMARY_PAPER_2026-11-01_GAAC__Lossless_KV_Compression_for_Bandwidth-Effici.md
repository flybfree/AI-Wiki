---
title: GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices
url: http://arxiv.org/abs/2610.38210v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-28_03-03-51Z_GAAC_LosslessKVCompressionforBandwidth_EfficientLL.md
generated_at: 2026-11-01 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
GAAC (Group-Adaptive Additive Codec) is a lossless key-value compression system designed to reduce the memory footprint and accelerate attention computation for long-context LLM inference on personal devices. By exploiting exponent redundancy in BF16 KV tensors, GAAC achieves approximately 1.4× lossless compression while also delivering 1.19–1.27× decode attention speedups on NVIDIA hardware and 1.02–1.25× speedups on Apple M4, all without introducing any approximation to KV values.

## Key Takeaways
- GAAC encodes BF16 exponents using calibrated per-channel base-plus-offset codes over contiguous ranges, adapting code widths across small groups to preserve KV values bit-for-bit. This achieves 1.405–1.407× lossless BF16 KV compression across five tested models, and also extends to FP8 E4M3 (1.09–1.14×) and E5M2 (1.25–1.30×) low-precision caches, demonstrating broad applicability across quantization tiers.
- A fused attention kernel reconstructs KV tiles on the fly during inference, avoiding full-cache decompression. Combined with block-wise compression and fixed-capacity slots, this supports incremental cache updates and paged serving, reducing resident KV memory by approximately 26% and increasing aggregate throughput by 13–29% under comparable KV-memory budgets on NVIDIA DGX Spark.
- The system demonstrates cross-platform portability, achieving 1.02–1.25× attention speedups on Apple M4 hardware, showing that the compression and fused-kernel approach is not tied to a single GPU architecture and can benefit personal-device inference broadly.

## Context
As LLMs scale toward million-token context windows, the KV cache has become the dominant memory bottleneck for on-device inference, far exceeding model weight storage in many practical scenarios. Existing approaches rely on lossy quantization or eviction strategies that degrade output quality. GAAC addresses this gap by targeting the structural redundancy inherent in floating-point exponent fields, offering a compression path that is orthogonal to weight quantization and compatible with existing W4A16 serving pipelines. This positions lossless KV compression as a complementary technique to the well-established weight-only quantization literature.

## Implications
For practitioners deploying LLMs on laptops, phones, and edge hardware, GAAC provides a practical mechanism to extend usable context lengths without sacrificing numerical fidelity, directly enabling longer conversations and retrieval-augmented workflows on constrained devices. For the broader serving infrastructure, the 13–29% throughput gains under fixed memory budgets suggest that lossless KV compression could reduce the hardware cost of production inference clusters. The cross-platform validation on Apple silicon further signals that such techniques can be integrated into heterogeneous inference stacks without vendor-specific optimization, lowering the barrier for open-source and on-device LLM deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.38210v1)
