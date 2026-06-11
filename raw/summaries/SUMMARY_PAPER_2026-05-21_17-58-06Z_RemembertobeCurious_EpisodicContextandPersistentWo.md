---
title: Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration
url: http://arxiv.org/abs/2605.22814v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-21_17-58-06Z_RemembertobeCurious_EpisodicContextandPersistentWo.md
generated_at: 2026-06-11 10:45
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a curiosity‑driven reinforcement learning framework for 3D exploration that combines persistent world modeling and episodic trajectory memory, allowing agents to explore novel regions without getting trapped in local loops. On the HM3D benchmark it outperforms active‑mapping baselines and generalizes zero‑shot to new visual worlds such as Gibson and AI‑generated scenes. The end‑to‑end policy operates on RGB frames at deployment while maintaining an internal 3D reconstruction for exploration.

## Key Takeaways
- The failure of curiosity in photorealistic 3D stems from missing spatial persistence and episodic context, causing agents to revisit states for fresh rewards.
- Effective curiosity requires an online 3D reconstruction as a persistent model that continuously updates the world representation.
- The agent policy is parameterized as a sequence model over RGB observations to retain an episodic trajectory history guiding exploration.

## Context
This work addresses a longstanding challenge in reinforcement learning by integrating memory mechanisms into 3D environments, moving beyond short‑term active mapping toward models that can learn from experience across episodes. It highlights the synergy between world modeling and behavior policy for scalable exploration.

## Implications
The approach enables agents to deploy with only RGB inputs while maintaining robust exploration capabilities, reducing reliance on complex 3D sensors. Practitioners can leverage this design for applications like robotics navigation or game AI where real‑time adaptation is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.22814v1)
