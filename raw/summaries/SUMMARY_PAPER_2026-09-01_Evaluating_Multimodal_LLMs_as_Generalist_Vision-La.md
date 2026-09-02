---
title: Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching
url: http://arxiv.org/abs/2609.01404v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-27-43Z_EvaluatingMultimodalLLMsasGeneralistVision_Languag.md
generated_at: 2026-09-01 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DroneCATS-Agent and DroneCATS to evaluate multimodal large language models as generalist vision-language-action agents controlling a drone. It finds that even simple embodied tasks reveal a paradox where smaller open models often succeed more reliably than frontier models, yet fail due to premature or missing termination actions.

## Key Takeaways
- Small open models navigate into the success radius more reliably than frontier models but lose episodes by declaring arrival prematurely or not at all.
- Multi-drone commanding amplifies this divide, with small models blindly copying a single coordinate across distinct views instead of adapting to each view.
- The core issue is not navigation but the discipline to sustain a declared protocol and emit the correct terminating action.

## Context
Multimodal large language models excel at perceiving visual information yet their ability to act end-to-end on real-world devices remains underdeveloped. This work bridges perception and control by treating the model as an independent variable in a benchmark, highlighting gaps between capability and deployment readiness.

## Implications
The findings suggest that practical edge AI systems must prioritize protocol discipline over raw performance metrics. For industry practitioners, this underscores the need for lightweight models that can reliably execute long‑term action plans without costly fine‑tuning or external schemas.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01404v1)
