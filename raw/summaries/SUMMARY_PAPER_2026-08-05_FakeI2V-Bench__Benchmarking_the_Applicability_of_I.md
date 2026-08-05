---
title: FakeI2V-Bench: Benchmarking the Applicability of Image-level Deepfake Detectors for Deepfake Video Detection
url: http://arxiv.org/abs/2608.03096v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_04-13-31Z_FakeI2V_Bench_BenchmarkingtheApplicabilityofImage_.md
generated_at: 2026-08-05 01:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FakeI2V-Bench a benchmark that evaluates video-level deepfake detectors while focusing on the performance of image-level detectors in video settings. The study shows an 80.16% AUC for the best image-level detector which slightly exceeds the top video-level detector at 79.99%. It also presents IV‑Bridge a framework that aggregates frame predictions to boost image-level methods beyond state-of-the-art.

## Key Takeaways
- FakeI2V-Bench provides 97,548 videos covering diverse categories and generation models to stress test both video and image detectors.
- The best image-level detector achieves an 80.16% AUC which marginally surpasses the strongest video-level model at 79.99% AUC.
- IV‑Bridge combines a random forest with statistical features from frame predictions allowing eleven image-level detectors to reach up to 93.80% AUC.

## Context
The rapid evolution of deepfake generation models has outpaced existing detection benchmarks which often neglect video contexts for image classifiers. This work addresses the gap by creating a comprehensive dataset and evaluation framework that directly compares image‑based approaches with dedicated video detectors. The results highlight the surprising capability of image detectors when adapted to temporal data.

## Implications
For practitioners, IV‑Bridge offers a practical method to retrofit existing image models into video pipelines without retraining from scratch. Industry stakeholders can leverage this benchmark to assess model robustness and prioritize research on multimodal detection strategies. Future AI systems will benefit from systematic evaluation that bridges image and video modalities in deepfake security.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03096v1)
