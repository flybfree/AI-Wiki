---
title: DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models
url: http://arxiv.org/abs/2610.36950v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_10-11-04Z_DCKV_LearnedTransformCodingofthePromptKVCacheinHyb.md
generated_at: 2026-10-27 22:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
DCKV introduces a differentiable, end-to-end trained codec for compressing the key-value (KV) cache in hybrid language models, which retain full-attention layers only in a small subset of their architecture. By jointly optimizing the transform, quantizer, and entropy models against a frozen language model, DCKV achieves over 55x compression relative to bf16 storage with at most 1.8 points of accuracy loss on long-context benchmarks, and over 100x compression with at most 3.6 points of loss, demonstrating that learned compression can dramatically reduce memory and bandwidth costs without severely degrading model performance.

## Key Takeaways
- DCKV is the first KV-cache codec trained end to end, meaning its transform, quantizer, and entropy models are all optimized jointly against the frozen language model rather than being designed independently or in a pipeline fashion. This end-to-end training allows the codec to minimize both the code length assigned by the entropy models and the actual change in the language model's output, aligning compression objectives directly with downstream task performance.
- The entropy models in DCKV are conditioned on the prompt tokens and on already decoded neighbouring positions, enabling the codec to exploit the structured, sequential nature of KV cache data. This conditioning allows the entropy models to assign shorter codes to predictable cache entries, significantly improving compression ratios beyond what static or context-free quantization schemes can achieve.
- On Qwen3.5-2B, DCKV stores a compressed token in more than 55 times fewer bytes than standard bf16 representation while incurring at most 1.8 points of degradation across three long-context benchmarks, and achieves more than 100x compression with at most 3.6 points of loss. These results show that aggressive compression is feasible in practice when the codec is trained to preserve the model's functional behavior rather than merely minimizing reconstruction error.

## Context
Hybrid language models, which combine full-attention layers with more efficient attention mechanisms such as sliding-window or linear attention, have emerged as a promising architecture for handling long contexts while reducing computational overhead. However, even in these hybrid designs, the KV cache in the remaining full-attention layers still grows linearly with prompt length and must be stored or transferred for reuse, creating a significant memory and bandwidth bottleneck. Prior compression approaches for KV caches have typically relied on hand-designed quantization schemes or post-hoc pruning, none of which were trained jointly with the language model. DCKV fills this gap by treating the entire compression pipeline as a differentiable component that can be optimized end to end, representing a methodological shift from heuristic compression to learned, task-aware compression in the context of large language model inference.

## Implications
For practitioners deploying hybrid language models at scale, DCKV offers a practical path to reducing the memory footprint and inter-device transfer costs of KV caches by one to two orders of magnitude, which is critical for serving long-context queries on constrained hardware or in distributed inference settings. The end-to-end training paradigm demonstrated here suggests that future model architectures could incorporate learned compression as a native component during training rather than as an afterthought, potentially enabling new efficiency-accuracy trade-offs that static codecs cannot achieve. Industry teams building inference infrastructure for long-document processing, retrieval-augmented generation, or multi-turn conversational agents stand to benefit directly from the compression ratios and bounded accuracy degradation reported in this work.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36950v1)
