---
title: Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation
url: http://arxiv.org/abs/2607.27627v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_03-32-19Z_Arm2Air_Cross_EmbodimentSkeletonTransferfor3DRelay.md
generated_at: 2026-07-30 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Arm2Air, a method that transfers obstacle‑avoidance skeletons from robot arms to UAV relay placement using cross‑embodiment learning. By pretraining a transformer with limited target data and low‑rank adaptation, the method achieves significant speedups in 3D urban planning while improving reliability under high obstruction.

## Key Takeaways
- Arm2Air reduces median end‑to‑end planning runtime by 64.9 percent compared to the fastest conventional planner on nine held‑out urban maps.  
- In a dense‑obstruction group, it raises bottleneck capacity by 32.6 percent and cuts maximum hop distance variance by 75.2 percent while only updating 0.134 million parameters versus 1.383 million for full fine‑tuning.  
- The transferred skeleton lowers root mean square error of relay positions by 53.6 percent with three target maps, demonstrating efficient cross‑domain adaptation.

## Context
The work addresses the challenge of deploying UAV relays in cluttered urban environments where line‑of‑sight and obstacle constraints must be balanced. By leveraging transfer learning across heterogeneous embodied tasks, it reduces reliance on extensive domain‑specific data and computational resources.

## Implications
Arm2Air offers a scalable framework for transferring structured priors from one robot platform to another, lowering deployment costs and enabling rapid adaptation in dynamic settings. Practitioners can adopt this approach to accelerate UAV network planning without sacrificing performance or requiring large labeled datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27627v1)
