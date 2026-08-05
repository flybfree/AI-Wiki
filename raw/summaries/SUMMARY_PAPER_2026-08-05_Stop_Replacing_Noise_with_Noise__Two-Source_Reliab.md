---
title: Stop Replacing Noise with Noise: Two-Source Reliability Assessment for Label Correction and Sample Reweighting in Label-Noise Learning
url: http://arxiv.org/abs/2608.03432v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_10-22-02Z_StopReplacingNoisewithNoise_Two_SourceReliabilityA.md
generated_at: 2026-08-05 01:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TRACE, a Two‑Source Reliability Assessment framework that separates the reliability of observed noisy labels from pseudo targets learned during refurbishment. The authors demonstrate that current methods can inadvertently replace one unreliable signal with another, leading to loss of useful information. Experiments on synthetic and real‑world benchmarks show that TRACE improves representative refurbishment baselines and yields more reliable pseudo supervision.

## Key Takeaways
- Reducing trust in the observed label automatically increases trust in the pseudo target because both are controlled by a single cleanliness score, creating hidden coupling.
- The representation diagnostics reveal that noisy supervision redirects deeper layers strongly while shallower relations remain stable, providing information beyond the loss posterior.
- TRACE uses three source‑specific scores—loss fit for the observed label, shallow relation stability, and prediction agreement for the pseudo target—to control correction and supervision strength without assuming complementary reliability.

## Context
In noisy‑label learning, refurbishment aims to balance model predictions with imperfect ground truth. Existing approaches often treat all supervision as a single composite signal, which can mask underlying data quality issues and degrade performance on challenging tasks.

## Implications
For practitioners, TRACE offers a principled way to evaluate and manage the reliability of both label sources, potentially leading to more robust models in domains such as medical imaging and autonomous driving where noisy labels are common. The framework reduces reliance on heuristic cleanliness scores, encouraging systematic assessment that can be integrated into existing training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03432v1)
