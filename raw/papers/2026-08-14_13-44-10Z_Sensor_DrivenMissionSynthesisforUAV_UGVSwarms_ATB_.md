---
title: Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety
published: 2026-08-14T13:44:10Z
authors: Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi
url: http://arxiv.org/abs/2608.14306v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety

## Abstract
This paper presents a coordination architecture for heterogeneous UAV/UGV swarms that synthesises mission actions from uncertain, multi-modal sensor evidence while preserving hardware-enforced safety at the actuation boundary. The approach combines radar, RF, acoustic, and visual observations with Topic-Based Communication Space Petri Net (TB-CSPN) orchestration to support incremental mission formation under partial and evolving information. Consultant agents transform sensor outputs into temporally bounded semantic tokens, while supervisor agents provide authorisation and policy-governed release of mission transitions. This separation between interpretation, coordination, and execution yields auditable decision paths, constrains non-determinism within the coordination layer through guards and synchronisation, and enables bounded-time integration of heterogeneous evidence. To improve resilience in contested environments, including cyber compromise, spoofing, jamming, and communication loss, the digital coordination layer is complemented by independent analogue safety envelopes that clamp or veto unsafe actuator commands issued to individual vehicles. A coastal-surveillance case study illustrates how the proposed architecture enables dependable, governed, and physically safe swarm coordination under operational uncertainty.

## Metadata
- **Published**: 2026-08-14T13:44:10Z
- **Authors**: Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14306v1)