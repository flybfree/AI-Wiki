---
title: Is 4 Bits Enough for EEG Sleep Staging? A Subject-Level Benchmark of MXFP4, NVFP4 and FP8
url: http://arxiv.org/abs/2611.31436v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_19-16-45Z_Is4BitsEnoughforEEGSleepStaging_ASubject_LevelBenc.md
generated_at: 2026-11-24 22:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper benchmarks post-training quantization (PTQ) for five-stage sleep staging from single-channel Fpz-Cz EEG, targeting wearable devices that need small, energy-efficient networks while keeping raw EEG private. The authors evaluate 13 PTQ configurations from FP16 down to block-scaled 4-bit MXFP4 and NVFP4, using Sleep-EDF-78 (78 subjects), subject-wise cross-validation, three training seeds, value-exact emulation, and per-subject paired statistics. They find that 8- and 16-bit formats stay within 0.45 percentage points (pp) of FP32 Macro-F1, while full 4-bit weights and activations cost 1.98 to 3.04 pp for an epoch-wise CNN and at most 1.19 pp for a temporal-context network. Keeping the first and last layers in FP8 brings both 4-bit formats within 0.48 pp of FP32, adding at most 2.1% weight storage and no retraining, and is within an exploratory 1-pp margin of quantization-aware training (QAT).

## Key Takeaways
- Full 4-bit quantization is not free: an epoch-wise CNN loses 1.98 to 3.04 pp Macro-F1, while a temporal-context network loses at most 1.19 pp; a same-encoder ablation shows temporal context explains little of this gap, so the difference is not mainly due to context modeling.
- Layer sensitivity is concentrated at the input: the first layer, which quantizes raw EEG, is the most sensitive layer in both networks, and retaining the first and last layers in FP8 recovers most accuracy, bringing MXFP4 and NVFP4 within 0.48 pp of FP32.
- NVFP4 is the more robust 4-bit format: at equal block size it outperforms MXFP4, and on the nested Sleep-EDF-20 subset NVFP4 with FP8 first/last layers stays within 0.25 pp of FP32, whereas under MXFP4 the architecture ranking reverses and FP8 first/last layers fail to fully recover two of three models.
- The 4-bit losses are not random: they fall on the same subjects across architectures (Spearman correlation 0.69 to 0.79) and reduce N3 recall the most, which matters because deep-sleep detection is clinically important.
- The practical recipe is cheap and QAT-like: FP8 first and last layers plus 4-bit elsewhere adds at most 2.1% weight storage, needs no retraining, and is equivalent to QAT within an exploratory 1-pp margin.

## Context
Wearable sleep staging is attractive because it avoids transmitting raw EEG, preserving privacy, and reduces the energy cost of cloud inference. That goal pushes the field toward aggressive quantization, but prior results are often reported at the dataset level rather than per subject, which can hide failures on individual patients. This work addresses that gap by combining subject-level evaluation, paired statistics, and value-exact emulation across two architectures and two 4-bit block-scaled formats.

## Implications
For practitioners, the headline result is that 4-bit EEG sleep staging is viable without retraining if the first and last layers are kept in FP8, especially with NVFP4, which is the safer default across cohorts. The recipe is lightweight enough for edge deployment and should be preferred over naive full-4-bit quantization, particularly for N3 detection and for subjects whose losses recur across architectures. For the field, the study argues that subject-wise, paired benchmarks and explicit first/last-layer handling should be standard when claiming that low-bit EEG models are clinically acceptable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.31436v1)
