---
title: From Bit-Position Sensitivity to Unequal Error Protection for DNN Inference Memory
published: 2026-07-21T23:07:56Z
authors: Muhammad Husnain Mubarik, Karthik Mohan Kumar, Pedro Antonio Pena, Keshavan Varadarajan, Kunal Tyagi
url: http://arxiv.org/abs/2607.19623v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Bit-Position Sensitivity to Unequal Error Protection for DNN Inference Memory

## Abstract
We characterize per-bit-position fault sensitivity in ML inference across 16 workloads -- spanning transformer-based models and attention-free CNNs -- and across three floating-point formats. Our central empirical finding is a sharp bit-sensitivity transition: flipping any of the least-significant fraction bits up to a data-type-specific threshold, Xsafe, degrades task metrics by less than 1% under deterministic single-bit stress tests. Sensitivity rises through the upper fraction bits and spikes at the exponent-mantissa boundary, where a single-bit flip causes catastrophic collapse. Because low-order bits are largely inconsequential while high-order and exponent bits are critical, uniform SECDED protection -- which guards every bit equally at 12.5% storage overhead -- is unnecessarily conservative. We derive per-data-type Xsafe floors (FP16: 6, BF16: 4, FP32: 15) and workload-aware tiers that widen the unprotected region for resilient model classes, raising ECC savings to 37.5-62.5% without retraining. Text-conditioned diffusion models dictate the conservative floor; vision encoders, NLU models, and resilient LLMs tolerate wider bypass regions. These floors and tiers drive an Unequal Error Protection (UEP) codec with per-cacheline data-type tags and a dual-partition SRAM architecture for ML accelerators. Validation across 870+ fault-injection runs confirms selective protection holds under contiguous 2- and 3-bit upsets. The codec reduces ECC area by 27.8% relative to uniform SECDED; dual-voltage operation of the non-critical partition lowers gross BF16 read energy by about 17%, with a roughly 4% dual-partition macro-area overhead.

## Metadata
- **Published**: 2026-07-21T23:07:56Z
- **Authors**: Muhammad Husnain Mubarik, Karthik Mohan Kumar, Pedro Antonio Pena, Keshavan Varadarajan, Kunal Tyagi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19623v1)