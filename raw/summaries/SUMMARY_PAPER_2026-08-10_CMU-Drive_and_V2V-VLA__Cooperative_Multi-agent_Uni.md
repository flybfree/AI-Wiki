---
title: CMU-Drive and V2V-VLA: Cooperative Multi-agent Unified Driving with Reasoning Benchmark and Vehicle-to-Vehicle Vision-Language-Action Models
url: http://arxiv.org/abs/2608.07621v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-07_09-00-39Z_CMU_DriveandV2V_VLA_CooperativeMulti_agentUnifiedD.md
generated_at: 2026-08-10 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CMU-Drive, a benchmark for cooperative autonomous driving that evaluates multiple connected vehicles navigating safety‑critical scenarios with background traffic participants. It also presents V2V-VLA, a vision‑language‑action model that jointly generates driving actions, future waypoints, reasoning steps, and communication policies within a single forward pass. Experiments demonstrate the first end‑to‑end cooperative VLA framework for multi‑agent autonomous driving.

## Key Takeaways
- The benchmark CMU-Drive provides a closed‑loop evaluation of multiple CAVs interacting with both each other and surrounding traffic, enabling realistic testing of safety‑critical cooperative behaviors.
- V2V-VLA integrates all components—driving actions, waypoint planning, language reasoning, and communication policies—into one end‑to‑end model, reducing latency compared to separate modules.
- The released code, benchmark suite, and pre‑trained checkpoint make the framework accessible for open‑source research on multi‑agent autonomous driving.

## Context
The rapid advancement of vision‑language‑action models has transformed single‑agent autonomous systems, but cooperative scenarios remain under‑explored. This work addresses that gap by creating a unified testbed where multiple agents must reason and act together, reflecting the complexity of real‑world connected vehicle networks.

## Implications
For researchers, the CMU-Drive benchmark offers a standardized platform to compare new multi‑agent VLA approaches. Industry stakeholders can leverage the model to prototype safety protocols for future autonomous fleets, while practitioners gain tools to evaluate end‑to‑end cooperative perception and planning in a single pipeline.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07621v1)
