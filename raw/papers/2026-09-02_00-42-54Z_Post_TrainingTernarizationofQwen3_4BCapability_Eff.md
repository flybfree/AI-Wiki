---
title: Post-Training Ternarization of Qwen3-4B Capability, Effective Bit Budget, Storage Compression, and Deployment
published: 2026-09-02T00:42:54Z
authors: Anirudh Malik, M Sparsh Mehra, Poojith Devan
url: http://arxiv.org/abs/2609.01962v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Post-Training Ternarization of Qwen3-4B Capability, Effective Bit Budget, Storage Compression, and Deployment

## Abstract
Ultra-low-bit language models can reduce storage and memory bandwidth, but a nominal "1.58-bit" label does not fully describe the stored representation, retained capability, or runtime behavior.   We study an end-to-end post-training conversion of Qwen, an instruction-tuned 4B-parameter model, using KOTMS rotation, E2M-ATQ ternarization, and GPTQ-style error compensation from TWLA. The experiment is weight-only: activations remain at 16-bit precision, so ILA-AMP is omitted. We evaluate effective bit accounting, task capability retention, perplexity, calibration sensitivity, checkpoint composition, and deployment behavior.   The final conversion uses 1.641 effective bits per weight for quantized linear weights, with 81.62% of model parameters targeted. Across ten scored capability comparisons, accuracy falls from 64.5% to 54.7%. Degradation is uneven: BoolQ retains 84.6% chance-corrected teacher performance, while ARC-Challenge retains 43.8%. Perplexity rises from 13.639 to 18.748 on WikiText-2, 24.700 to 31.992 on PTB, and 19.831 to 28.966 on C4.   A subsequent packing run preserves the ternary planes and scales, reducing reported model size from 8.29 GiB to 3.96 GiB with essentially unchanged perplexity. A separate third-party packing attempt was lossy and is excluded from the primary artifact claim. The packed artifact has not been benchmarked end-to-end for task accuracy or generation throughput. A preliminary Triton GEMV microbenchmark is 4.6x slower than FP16 cuBLAS on one tested shape. We therefore do not claim that compression alone yields faster inference.

## Metadata
- **Published**: 2026-09-02T00:42:54Z
- **Authors**: Anirudh Malik, M Sparsh Mehra, Poojith Devan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01962v1)