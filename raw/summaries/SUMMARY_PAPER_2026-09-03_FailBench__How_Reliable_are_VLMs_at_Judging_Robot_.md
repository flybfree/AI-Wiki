---
title: FailBench: How Reliable are VLMs at Judging Robot Task Success?
url: http://arxiv.org/abs/2609.03611v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_09-58-55Z_FailBench_HowReliableareVLMsatJudgingRobotTaskSucc.md
generated_at: 2026-09-03 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FailBench, a benchmark that tests vision‑language models’ ability to detect robot manipulation failures across diverse real‑world and simulated tasks. Evaluating 13 VLM detectors on 2,197 attempts, the best model reaches only 0.77 balanced accuracy, highlighting significant performance gaps.

## Key Takeaways
- The top detector achieves merely 0.77 mean balanced accuracy, far below random performance, indicating poor reliability in failure detection.  
- Models underperform both general‑purpose VLMs and their own pretrained baselines when fine‑tuned for this specific task.  
- Performance collapses to near chance (<0.60) on contact‑intensive assembly tasks where visual evidence is ambiguous.

## Context
The rapid adoption of vision‑language models in robotics has created a need for reliable failure detection, yet existing benchmarks lack cross‑domain validation. FailBench addresses this gap by combining real‑world and simulated data to assess generalization under varied conditions.

## Implications
For industry practitioners, the results warn against trusting VLM‑based detectors without domain‑specific tuning or input preprocessing. The finding that spatial cropping improves performance suggests practical solutions for enhancing model robustness in production settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03611v1)
