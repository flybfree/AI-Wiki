---
title: Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy
url: http://arxiv.org/abs/2609.00103v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_17-05-17Z_GoodMemoryHasECC_EvaluatingtheMemoryofVision_Langu.md
generated_at: 2026-09-01 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ECCBench, a benchmark that evaluates the memory capabilities of vision‑language models beyond simple accuracy scores. The authors find that pretrained VLMs compress text inputs efficiently but fail to do so for video and are poorly calibrated on both modalities, indicating a mismatch between raw performance and real‑world long‑horizon task requirements.

## Key Takeaways
- ECCBench measures memory through three axes: efficiency (FLOPs), compression (accuracy/efficiency trade‑off), and calibration (error handling via abstention).  
- Pretrained VLMs compress text well but do not compress video, showing modality‑specific limitations.  
- The models are poorly calibrated, meaning they generate answers despite uncertainty rather than abstaining when uncertain.

## Context
Memory remains a critical unsolved challenge for large language and vision‑language systems, as current benchmarks focus on long‑text or long‑video accuracy without capturing computational cost or error handling. This work expands the evaluation framework to include efficiency and calibration, which are essential for practical deployment in agents that must operate over extended horizons.

## Implications
For researchers, ECCBench provides a more holistic view of memory performance, guiding the selection of architectures that balance compression and calibration. Practitioners can use these insights to design agents capable of handling long‑horizon tasks with lower computational overhead and appropriate uncertainty management.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00103v1)
