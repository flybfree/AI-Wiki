---
title: Automatic Field-of-View Adjustment for a View-Expansive Microscope via LSTM-Based Gaze and Pipette Motion Interpretation
url: http://arxiv.org/abs/2608.10401v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_02-49-27Z_AutomaticField_of_ViewAdjustmentforaView_Expansive.md
generated_at: 2026-08-11 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an AI‑driven system that automatically adjusts the field‑of‑view of a view‑expansive microscope during intracytoplasmic sperm injection (ICSI) using long short‑term memory (LSTM) models. By interpreting pipette motion and operator gaze, the model predicts the optimal FOV size, eliminating manual lens changes. The system cuts average procedure time from 60.5 to 48.0 seconds with statistical significance (p < 0.001).

## Key Takeaways
- The LSTM predicts the appropriate FOV based on real‑time pipette position and velocity combined with gaze data, enabling seamless visual adaptation.
- The method removes the need for physical lens switching, directly reducing procedure duration and operator fatigue.
- Novice operators achieve ICSI speeds equivalent to those of expert operators after AI assistance.

## Context
This work advances multimodal AI integration in medical robotics by fusing visual input with kinematic sensor streams into a temporal prediction model. LSTM networks excel at modeling sequential dependencies, making them suitable for real‑time control where past and present data jointly inform future decisions. The approach exemplifies how deep learning can automate repetitive tasks without hardware changes.

## Implications
Faster ICSI procedures lower costs and improve patient throughput in fertility clinics. Training efficiency is enhanced as novices receive immediate performance gains, reducing reliance on expert supervision. The technology may be extended to other surgical or diagnostic processes requiring precise visual adjustments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10401v1)
