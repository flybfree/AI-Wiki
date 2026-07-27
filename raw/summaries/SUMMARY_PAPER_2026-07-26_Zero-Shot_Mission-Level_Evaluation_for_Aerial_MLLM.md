---
title: Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents
url: http://arxiv.org/abs/2607.22014v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_06-22-50Z_Zero_ShotMission_LevelEvaluationforAerialMLLMAgent.md
generated_at: 2026-07-26 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MissionBench, a benchmark for evaluating multimodal large language models in aerial 3D environments without fine‑tuning. Across 22 MLLMs, the best model achieves only about 35% mission success versus 84.4% human performance, showing that zero‑shot embodied tasks remain hard.

## Key Takeaways
- The strongest model succeeds on fewer than 35% of missions compared to 84.4% human performance, highlighting the difficulty of multi‑step embodied tasks.
- Large models show gains from scaling, indicating stronger zero‑shot embodied capabilities when scaled up.
- Mission competence requires coordinating multiple capabilities beyond spatial perception, such as multi‑step planning and adaptive reasoning.

## Context
Multimodal large language models are being integrated into embodied AI systems that must act in 3D spaces using only egocentric observations. This work addresses a gap by providing a standardized mission‑level evaluation that isolates zero‑shot performance from task‑specific fine‑tuning, offering a benchmark for future research.

## Implications
The results suggest that scaling alone may not solve embodied reasoning challenges, urging researchers to develop closed‑loop evaluations that better capture multi‑modal coordination. Practitioners should consider these limitations when deploying MLLMs in real aerial robotics, as current models still fall short of human performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22014v1)
