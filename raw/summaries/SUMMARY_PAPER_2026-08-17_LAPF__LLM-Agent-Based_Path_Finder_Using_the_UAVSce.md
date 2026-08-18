---
title: LAPF: LLM-Agent-Based Path Finder Using the UAVScenes Dataset
url: http://arxiv.org/abs/2608.15175v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_11-28-21Z_LAPF_LLM_Agent_BasedPathFinderUsingtheUAVScenesDat.md
generated_at: 2026-08-17 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LAPF, an LLM‑agent based path finder for UAV navigation using the UAVScenes dataset, achieving shorter paths than straight line and CoT prompting by integrating perception, memory, planning and action modules in a closed loop.

## Key Takeaways
- The framework couples each detected hazard to a bounded corrective action, resulting in zero clamp events compared with 14.0 events for CoT prompting.
- LAPF reduces path length from the straight‑line optimum by 17.2% (512.83 m vs 497.33 m) and by 15.6% in obstacle‑injected scenarios, while maintaining near‑goal stability.
- The three independent trials show absolute path efficiencies of 97.1% and 98.1%, demonstrating strong performance across open‑field and obstacle conditions.

## Context
Autonomous UAV navigation faces challenges from dynamic environments where traditional optimization or ML methods lack adaptability, prompting interest in agentic reasoning that can reason step‑by‑step and act on sensor data without retraining.

## Implications
LAPF demonstrates that integrating LLMs with explicit memory and action modules can improve real‑world path planning, offering a template for other robotics tasks where safety and efficiency are critical. Practitioners may adopt this architecture to reduce reliance on pre‑trained models and enable continuous adaptation during missions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15175v1)
