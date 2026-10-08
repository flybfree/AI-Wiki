---
title: ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals
url: http://arxiv.org/abs/2610.10381v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_16-40-21Z_ResidualQuant_KVCacheQuantizationforLoopedTransfor.md
generated_at: 2026-10-07 22:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ResidualQuant addresses the KV cache memory bottleneck in Looped Transformers by exploiting the high similarity of KV states across recurrent loops, using the final-loop KV states as a reference and encoding the remaining loops as low-precision residuals. The method achieves accurate INT2 quantization through least-square scaling, rotations, and loop-wise mixed precision, delivering an 80.7% reduction in theoretical KV storage while maintaining accuracy close to BF16 and outperforming rotation-based baselines by up to 13.0% at equivalent memory budgets.

## Key Takeaways
- Looped Transformers reuse shared Transformer blocks across multiple recurrent loops to increase computational depth without adding parameters, but the KV cache still scales linearly with the number of loops, creating a severe memory bottleneck that limits batch size and inference throughput. ResidualQuant directly targets this scaling problem by recognizing that KV states across loops are highly similar, enabling a residual-based representation rather than storing each loop's KV cache independently.
- The quantization pipeline combines three complementary techniques: using the final-loop KV states as a high-precision reference anchor, applying least-square scaling and rotations to the residual differences to minimize quantization error, and employing loop-wise mixed precision so that different loops can be quantized at different bit-widths. This combination allows the method to push down to INT2 precision while preserving reconstruction fidelity, a regime where existing KV quantization methods typically suffer substantial accuracy degradation.
- On hardware benchmarks using an RTX 5090, the reduced KV memory traffic translates into concrete throughput gains: fixed-batch decode throughput improves by up to 2.73x, and the smaller memory footprint permits up to 2x larger batches, yielding peak throughput improvements of up to 4.15x. These gains are validated across multiple looped Transformer models on mathematical reasoning and code generation benchmarks, demonstrating consistent accuracy-memory tradeoff improvements over state-of-the-art rotation-based KV quantization.

## Context
KV cache quantization has become a critical research area as large language models push inference memory to its limits, with rotation-based methods like QuaRot and SpinQuant representing the current frontier. Looped Transformers, which trade parameter count for computational depth through weight sharing across recurrent iterations, introduce a distinct memory profile where the KV cache—not the weights—dominates inference cost. ResidualQuant fills a gap in this landscape by tailoring quantization specifically to the structural redundancy inherent in looped architectures, rather than applying generic low-bit quantization uniformly across all loops.

## Implications
For practitioners deploying looped or recurrent Transformer architectures at scale, ResidualQuant offers a practical path to near-BF16 accuracy at 2-bit KV precision, dramatically expanding feasible batch sizes and decode throughput on consumer-grade GPUs like the RTX 5090. For the broader field, the paper demonstrates that architecture-aware quantization—exploiting structural priors such as inter-loop KV similarity—can unlock aggressive compression regimes that generic methods cannot reach, suggesting a promising direction for future inference optimization in parameter-efficient model families.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10381v1)
