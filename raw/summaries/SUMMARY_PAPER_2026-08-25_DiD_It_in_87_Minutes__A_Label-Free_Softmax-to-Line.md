---
title: DiD It in 87 Minutes: A Label-Free Softmax-to-Linear Adaptation of Vision Transformers for Object Detection
url: http://arxiv.org/abs/2608.22368v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-23_11-21-16Z_DiDItin87Minutes_ALabel_FreeSoftmax_to_LinearAdapt.md
generated_at: 2026-08-25 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Detector-Interface Distillation (DiD), a label-free method to convert a Softmax-attention Vision Transformer into a linear-attention one while preserving the detector interface. On DOTA-v1.5 it matches supervised linear models and reduces inference latency by 62% with lower memory.

## Key Takeaways
- DiD aligns detector-facing interface tensors between frozen Softmax teacher and trained linear backbone, ensuring feature compatibility.
- The conversion avoids direct operator swapping which causes severe performance loss.
- Adaptation finishes in about 87 minutes on four GPUs, cutting latency and peak memory.

## Context
Vision Transformers dominate object detection but their full attention scales poorly. Linear attention offers a scalable alternative yet requires careful interface handling. This work bridges that gap without retraining the detector.

## Implications
Practitioners can reuse existing detectors with minimal effort to achieve faster inference. Interface-aware conversion objectives may become standard in architecture adaptation research, encouraging more modular and efficient model deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22368v1)
