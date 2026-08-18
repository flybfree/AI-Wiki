---
title: EgoGazeLite: On-Device Egocentric Gaze Prediction for Token-Efficient Multimodal LLM Video Input
published: 2026-08-16T08:28:01Z
authors: Matteo Stoiber, Niels Buus Lassen
url: http://arxiv.org/abs/2608.15614v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EgoGazeLite: On-Device Egocentric Gaze Prediction for Token-Efficient Multimodal LLM Video Input

## Abstract
The use of multimodal LLMs (MLLMs) for egocentric video understanding with wearable devices is constrained by the token budget. Memory and compute cost scale with the number of visual tokens, and high-resolution video quickly becomes expensive to transmit and process at scale. Prior work (GazeLLM) addresses this by cropping the video around the camera wearer's gaze. This reduces the number of visual tokens by about tenfold while maintaining or improving the quality of full-resolution descriptions. However, this compression strategy depends on dedicated eye-tracking hardware, which is unavailable on consumer smart glasses. Building a software-only substitute poses a joint constraint: the predictor must be accurate enough to preserve downstream description quality, yet light enough to run on-device, within the power and compute budget of a smartphone. We address this with EgoGazeLite, a lightweight dual-process gaze predictor for egocentric video. Across two MLLMs, three automated metrics, and two LLM judges, predicted-gaze crops show no significant difference from ground-truth-gaze crops. Equivalence is confirmed in all ten cases. EgoGazeLite achieves this at 15.7M parameters, 6.71 GFLOPs, and runs the full gaze-and-crop pipeline end-to-end in real time (21.6 ms/frame) on consumer accelerator hardware. Together, these results remove the need for eye-tracking hardware for token-efficient, gaze-conditioned egocentric video understanding with MLLMs.

## Metadata
- **Published**: 2026-08-16T08:28:01Z
- **Authors**: Matteo Stoiber, Niels Buus Lassen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15614v1)