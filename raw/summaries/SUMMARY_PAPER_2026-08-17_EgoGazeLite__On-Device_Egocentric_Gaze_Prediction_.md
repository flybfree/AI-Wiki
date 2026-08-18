---
title: EgoGazeLite: On-Device Egocentric Gaze Prediction for Token-Efficient Multimodal LLM Video Input
url: http://arxiv.org/abs/2608.15614v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_08-28-01Z_EgoGazeLite_On_DeviceEgocentricGazePredictionforTo.md
generated_at: 2026-08-17 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces EgoGazeLite, a lightweight dual-process model that predicts egocentric gaze from on‑device video without requiring eye‑tracking hardware. The authors demonstrate that the predicted crops are indistinguishable from ground‑truth crops across ten test cases while running the entire pipeline in real time on consumer accelerator hardware.

## Key Takeaways
- EgoGazeLite reduces visual tokens by roughly tenfold compared with full‑resolution video, enabling token‑efficient multimodal LLMs.  
- The model runs at 15.7 million parameters and 6.71 GFLOPs, completing the gaze‑crop pipeline in under 22 ms per frame on a smartphone accelerator.  
- All ten evaluation cases show no significant difference between predicted‑gaze crops and ground‑truth crops, confirming equivalence.

## Context
Current multimodal LLMs struggle with high‑resolution video due to memory and compute constraints, limiting their use in wearable devices. Existing solutions rely on hardware eye‑tracking, which is impractical for consumer smart glasses. EgoGazeLite offers a software alternative that balances accuracy and efficiency, aligning with the trend toward fully on‑device AI.

## Implications
The result removes hardware dependencies, making egocentric video understanding feasible for mass‑market devices. Practitioners can integrate gaze‑conditioned MLLMs into applications without costly sensors, accelerating deployment in AR, education, and health monitoring.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15614v1)
