---
title: VoLN: Vision-Only Long-Horizon Navigation---Paradigm, Benchmark, and Method
url: http://arxiv.org/abs/2607.21400v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_15-02-01Z_VoLN_Vision_OnlyLong_HorizonNavigation___Paradigm_.md
generated_at: 2026-07-23 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Vision-Only Long-Horizon Navigation (VoLN), a paradigm that replaces route‑level instructions with locally observable in‑scene cues for open, GPS‑denied aerial navigation. The authors present VoLN-UAV, a 7,210‑episode benchmark, and the baseline model VoLN-MLLM, which achieves modest success rates on Easy, Normal, and Hard episodes (7.4%, 4.5%, 1.8%). These results highlight both progress and remaining challenges in long‑horizon evidence integration.

## Key Takeaways
- The benchmark VoLN-UAV tests navigation under continuous 3D motion, large viewpoint changes, and context‑dependent beacon selection, emphasizing the difficulty of maintaining a stable trajectory over long horizons.  
- The baseline model VoLN-MLLM predicts short‑horizon waypoint segments using visual–semantic tokens and proprioception, showing that structured semantic alignment can improve performance but still falls short in unseen environments.  
- Success rates on Test‑Unseen split reveal substantial gaps in integrating distant evidence, matching goals across view changes, and achieving closed‑loop stability.

## Context
Vision-and-Language Navigation (VLN) has advanced by moving from static route instructions to dynamic perception‑driven planning, yet most systems still rely on external cues that are unavailable in GPS‑denied settings. VoLN pushes this research toward truly self‑sufficient navigation where all guidance is derived from onboard sensors and visual observations.

## Implications
For autonomous aerial platforms, VoLN demonstrates a viable approach to reduce dependence on pre‑programmed waypoints, enabling adaptable operation in complex urban or wilderness environments. Practitioners can leverage the benchmark and model to evaluate perception‑centric navigation strategies, informing future deployments where real‑time visual feedback is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21400v1)
