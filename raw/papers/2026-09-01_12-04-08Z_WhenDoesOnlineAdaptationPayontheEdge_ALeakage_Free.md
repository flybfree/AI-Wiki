---
title: When Does Online Adaptation Pay on the Edge? A Leakage-Free Evaluation of Warmup, Learning-Rate Selection, and Resource Trade-offs for Time-Series Forecasting
published: 2026-09-01T12:04:08Z
authors: Takumi Fujimoto, Hiroaki Nishi
url: http://arxiv.org/abs/2609.01126v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Does Online Adaptation Pay on the Edge? A Leakage-Free Evaluation of Warmup, Learning-Rate Selection, and Resource Trade-offs for Time-Series Forecasting

## Abstract
Online adaptation can help edge time-series forecasting under distribution drift, but its measured benefit is sensitive to evaluation choices. We study six public multivariate streams, including building-sensor and smart-meter data, under a leakage-free streaming protocol. We identify two additional sources of comparison bias. First, the warmup budget of the static baseline has a two-sided effect: insufficient warmup undertrains the baseline, whereas excessive warmup can degrade its pre-drift generalization. Across six dataset-backbone settings, the estimated adaptation benefit changes by 3.0 to 18.8 percentage points (pp) over the 1,000-20,000-step warmup range. Second, comparing SGD with momentum (SGD+m) and Adam at a shared default learning rate conflates optimizer quality with rate sensitivity. We select both the warmup budget and each optimizer's online rate using a held-out pre-drift validation slice without accessing test data. Under this validation-only procedure, Adam outperforms SGD+m in 310 of 360 evaluated cells, while 4 Adam cells remain below the static baseline. We further characterize accuracy against adaptation-state memory and A100-measured per-update latency for full, head-only, and calibration-based adaptation. In the evaluated PatchTST frontier settings, several parameter-efficient variants are nondominated on the adaptation-state-memory axis. Smart-meter analyses also show that reported gains depend on meter-selection rules. These findings support a validation-only commissioning procedure, while target-device latency and energy remain to be measured. Code, data, and all reported numbers: https://github.com/keiotakmin/tsf-edge-adaptation.

## Metadata
- **Published**: 2026-09-01T12:04:08Z
- **Authors**: Takumi Fujimoto, Hiroaki Nishi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01126v1)