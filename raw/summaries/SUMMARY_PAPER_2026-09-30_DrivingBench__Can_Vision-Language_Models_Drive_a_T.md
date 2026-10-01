---
title: DrivingBench: Can Vision-Language Models Drive a Toyota Corolla?
url: http://arxiv.org/abs/2609.38948v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_04-16-59Z_DrivingBench_CanVision_LanguageModelsDriveaToyotaC.md
generated_at: 2026-09-30 21:10
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces DrivingBench, the first benchmark evaluating general-purpose vision-language models on the physical task of driving a real Toyota Corolla through a parking lot cone course. While most frontier models struggled significantly with the long-horizon constraints and inference latency inherent in controlling a moving vehicle, GPT-6 Astra emerged as the sole model to successfully complete the course on its second attempt, highlighting the gap between digital benchmark performance and embodied control capabilities.

## Key Takeaways
- DrivingBench requires models to process camera frames and issue direct steering and velocity commands via three tools, testing abilities under realistic constraints where inference latency impacts control as new commands overwrite running actions while the model thinks.
- In evaluations of four frontier models with up to three attempts per conversation, only GPT-6 Astra finished

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38948v1)
