---
title: Glance, Scrutinize, and Think: Advancing Video Anomaly Detection from Training-Free to Agentic Reasoning
url: http://arxiv.org/abs/2608.11260v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-07_17-07-49Z_Glance_Scrutinize_andThink_AdvancingVideoAnomalyDe.md
generated_at: 2026-08-12 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a training-free video anomaly detection framework that combines global coarse grounding with local fine understanding. It proposes Glance then Scrutinize (GtS) and an agentic tool‑augmented method to improve both accuracy and inference speed. Experiments on VAGU‑T show substantial gains over existing baselines.

## Key Takeaways
- GtS uses static and dynamic textual guidance to ground anomalies without retraining, balancing speed and performance.
- The agentic model can invoke a cropping tool, inspect resampled frames, and self‑correct hypotheses via reinforcement learning with a joint reward.
- JeAUG jointly measures semantic interpretability and temporal precision, providing a unified evaluation metric.

## Context
Video anomaly detection remains challenged by the split between when an event occurs and what it means. Prior methods either lack precise timing or cannot explain events in human terms. This work bridges that gap by integrating reasoning across modalities and tools.

## Implications
The approach offers a practical template for deploying VAD in surveillance and autonomous systems where real‑time inference is critical. By enabling agents to reason step‑by‑step, it could reduce false positives and improve trust in automated video analysis pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11260v1)
