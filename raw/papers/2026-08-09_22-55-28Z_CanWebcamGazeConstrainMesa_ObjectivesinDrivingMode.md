---
title: Can Webcam Gaze Constrain Mesa-Objectives in Driving Models? An Instrument Precision Analysis
published: 2026-08-09T22:55:28Z
authors: Lennox Anderson, Ahmed Boutar, Jonah Mulcrone, Tal Erez
url: http://arxiv.org/abs/2608.08947v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Webcam Gaze Constrain Mesa-Objectives in Driving Models? An Instrument Precision Analysis

## Abstract
Current hazard detection systems in autonomous driving may develop mesa objectives, learned internal goals that achieve high training performance through spurious correlations rather than genuine hazard recognition. We investigate whether human gaze patterns, captured via webcam-based eye tracking (WebGazer.js), can serve as privileged information to constrain mesa-objective formation. We collected 137,663 frame-level gaze samples synchronized with hazard annotations across 388 real dashcam clips, then test this hypothesis across two calibration protocols (9-point/45-click and 11-point/440-click), two model architectures (Random Forest and causal Transformer), and five random seeds per experiment with paired t-tests. No experiment yields a statistically significant improvement from gaze (p = 0.919, 0.578, and 0.667 respectively). A geometric analysis reveals the root cause: WebGazer's reported error (~130-257 px depending on configuration) exceeds 93% of detected hazard object sizes (median 36 px), rendering object-level gaze attribution physically impossible at this instrument precision.

## Metadata
- **Published**: 2026-08-09T22:55:28Z
- **Authors**: Lennox Anderson, Ahmed Boutar, Jonah Mulcrone, Tal Erez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08947v1)