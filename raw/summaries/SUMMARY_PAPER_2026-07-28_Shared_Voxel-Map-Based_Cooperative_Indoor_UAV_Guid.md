---
title: Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller
url: http://arxiv.org/abs/2607.25728v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_13-52-12Z_SharedVoxel_Map_BasedCooperativeIndoorUAVGuidancew.md
generated_at: 2026-07-28 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a cooperative indoor UAV guidance system that uses a shared voxel‑map world model and a multi‑agent Soft Actor‑Critic controller. In simulation the learned policy reaches a 90.3% success rate in corridor navigation, beating Astar planning and other methods.

## Key Takeaways
- The framework fuses 360 LiDAR scans into a common occupancy map that is turned into a compact bird’s‑eye‑view crop for each drone, enabling decentralized yet spatially consistent control.  
- The controller combines BEV features, near‑field obstacles and peer states within a centralised training but decentralised execution setup.  
- Offline imitation fine‑tuning from real data resolves sim‑to‑real mismatch, allowing stable two‑UAV operation in GNSS‑denied indoor settings.

## Context
This work advances the field of multi‑agent reinforcement learning by integrating a shared spatial representation with learned policies, demonstrating how centralized training can support distributed execution for complex navigation tasks.

## Implications
The approach offers scalable, robust guidance for swarm robots where reliable perception and decentralized control are critical. Practitioners can apply this model to improve real‑world indoor robot coordination without sacrificing autonomy or safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25728v1)
