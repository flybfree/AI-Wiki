---
title: CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1-8-Bit Weights
published: 2026-08-07T03:36:07Z
authors: Xuetian Gao
url: http://arxiv.org/abs/2608.06763v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1-8-Bit Weights

## Abstract
Weight quantization for large-language-model inference must balance adaptive reconstruction levels with representations regular enough for efficient GPU execution. Uniform integers constrain each group to a linear grid. Low-bit floating-point formats use a fixed exponent-mantissa structure, while learned codebooks gain flexibility at the cost of irregular decoding and additional metadata.   We introduce CubicQuant, a parametric non-uniform scalar format that preserves a dense integer code stream while adapting reconstruction levels within each weight group. A monotonic cubic curve, specified by two shape parameters and one scale, maps uniformly spaced magnitude codes to non-uniform levels. The family spans 1-8-bit weight payloads, contains symmetric uniform integer quantization as an exact special case, and has effective width B + 64/G bits per weight for payload width B and group size G. We derive population distortion under Uniform, Gaussian, and Laplace distributions, formulate continuous and Dynamic-A8-carrier-aware fitting objectives, and describe direct packed-weight GPU execution.   For finite groups of G=128 with 15,360 samples per distribution, W4 CubicQuant reduced reconstruction RMSE relative to optimally clipped four-bit uniform integer quantization by 3.90% on Uniform, 13.49% on Gaussian, and 28.14% on Laplace samples. Relative to the best enumerated four-bit finite floating-point format, the reductions were 3.90%, 9.44%, and 6.27%. Preliminary H200 kernel measurements show a workload-dependent crossover: model-dtype execution is faster for narrow GEMV, while Dynamic A8 becomes favorable as row count grows. The results establish the format's representational promise and direct executability; downstream model quality and cross-device end-to-end performance remain open evaluation questions.

## Metadata
- **Published**: 2026-08-07T03:36:07Z
- **Authors**: Xuetian Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06763v1)