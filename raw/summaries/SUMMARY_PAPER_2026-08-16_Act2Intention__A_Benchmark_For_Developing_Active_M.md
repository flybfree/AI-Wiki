---
title: Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions
url: http://arxiv.org/abs/2608.14132v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_09-36-59Z_Act2Intention_ABenchmarkForDevelopingActiveMobileA.md
generated_at: 2026-08-16 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Act2Intention, a framework that integrates understanding, predicting user intentions, and executing decisions to create an active mobile agent. The authors present the Act2Intention Benchmark containing 72,511 intentions and over 700,000 actions across 52 apps, and demonstrate that supervised fine‑tuning on this data yields significant gains: +32.0 Acc‑S, +10.25 Acc‑S, and +6.9 SSR points for understanding, prediction, and execution respectively.

## Key Takeaways
- The Act2Intention Benchmark is the first large‑scale collection of intention‑action trajectories for evaluating proactive agents.
- Fine‑tuning on this benchmark improves all three core components—understanding, prediction, and execution—by substantial margins compared to baseline models.
- The framework demonstrates that a unified understanding‑prediction‑execution pipeline can be systematically evaluated through continuous trajectory data.

## Context
Active mobile agents rely heavily on interpreting user intent from GUI actions, yet existing research often treats this as a reactive task rather than an active process. This work fills the gap by constructing a comprehensive benchmark and showing how fine‑tuning can enhance each stage of the intention pipeline, aligning with broader trends toward multimodal large language models in human‑computer interaction.

## Implications
The Act2Intention Benchmark provides a standardized platform for developing and assessing proactive agents, enabling researchers to focus on intelligent intent inference rather than isolated task execution. For industry practitioners, this means actionable insights into how to build agents that anticipate user needs, ultimately improving usability and engagement in mobile applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14132v1)
