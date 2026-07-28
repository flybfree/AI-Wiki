---
title: Cortex: Compact Behavior Cloning for Quake with Frozen Visual Features
url: http://arxiv.org/abs/2607.22739v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-22_18-34-30Z_Cortex_CompactBehaviorCloningforQuakewithFrozenVis.md
generated_at: 2026-07-27 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Cortex, a compact behavior‑cloning policy for the first‑person shooter Quake that uses only 10.98 million trainable parameters in a six‑layer transformer with a frozen DINOv3 encoder. The authors report that under strict time limits, Cortex reaches key environmental milestones and even records kills, outperforming several larger released checkpoints on short test episodes.

## Key Takeaways
- Cortex achieves notable progress without reinforcement learning or explicit memory, relying solely on a frozen visual encoder and a small policy head.  
- The model’s performance is limited by covariate shift between training data and the game environment, leading to consistent failures despite reaching many level landmarks.  
- Ablations reveal that richer visual tokens boost combat success while longer optimization improves offline metrics without necessarily enhancing playability.

## Context
The work highlights a growing interest in lightweight, parameter‑efficient neural policies for complex games where full reinforcement learning is impractical. By freezing high‑level visual encoders and using compact transformers, researchers aim to bridge the gap between human‑like behavior and computational efficiency.

## Implications
For game developers, Cortex suggests that simple policy baselines can still produce engaging gameplay loops when visual features are well aligned with training data. Practitioners should consider covariate shift as a primary limitation rather than model capacity, guiding targeted data collection for improved performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22739v1)
