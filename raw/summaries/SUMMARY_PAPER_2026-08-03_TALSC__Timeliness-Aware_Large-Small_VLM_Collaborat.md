---
title: TALSC: Timeliness-Aware Large-Small VLM Collaboration for Infrastructure-Assisted Autonomous Driving
url: http://arxiv.org/abs/2608.01998v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_09-58-20Z_TALSC_Timeliness_AwareLarge_SmallVLMCollaborationf.md
generated_at: 2026-08-03 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TALSC, a framework that schedules collaboration between small on‑board VLMs and large server‑based VLMs while accounting for the age of information in dynamic driving scenarios. The authors demonstrate that their scheduling algorithm yields up to 12.6 % normalized Micro‑F1 improvement over baselines across various communication and computing settings.

## Key Takeaways
- Age of Information (AoI) is modeled as a function of token length and task performance, providing a quantitative timeliness metric for VLM inference.
- The TALSC algorithm uses a Lyapunov drift‑plus‑estimated‑penalty approach to handle delayed scheduling impacts and unknown output tokens, guaranteeing performance stability.
- Simulation on the nuScenes dataset shows that TALSC outperforms existing methods under both limited bandwidth and high latency conditions.

## Context
Vision‑Language Models are central to autonomous driving but face computational constraints on vehicles. Infrastructure‑assisted collaboration promises accuracy gains at the cost of latency, a challenge that has not been fully addressed in prior work. This research bridges the gap by integrating timeliness considerations into real‑time scheduling decisions.

## Implications
The TALSC framework offers a practical solution for edge AI systems where both performance and speed are critical, enabling higher quality perception without sacrificing real‑time responsiveness. Practitioners can adopt this model to design more robust autonomous driving pipelines that balance large‑scale reasoning with on‑device efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01998v1)
