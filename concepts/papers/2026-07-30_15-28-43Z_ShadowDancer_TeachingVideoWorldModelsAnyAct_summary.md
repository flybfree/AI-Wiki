# Summary: 2026-07-30_15-28-43Z_ShadowDancer_TeachingVideoWorldModelsAnyActionbyLe.md
Saved: 2026-07-30 22:16
Source: 2026-07-30_15-28-43Z_ShadowDancer_TeachingVideoWorldModelsAnyActionbyLe.md
Model: None

---

## Summary  
ShadowDancer introduces a novel approach for teaching any‑action, frame‑level control of interactive video world models by learning unified dynamics representations from a video together with its shadow. It addresses the representational problem where existing interfaces either encode actions loosely or require exact, hard‑to‑acquire signals. By constructing shadow pairs and learning cross‑shadow prediction, the method enables precise action control across diverse dynamics without fine‑tuning. The approach makes demonstration videos reusable assets for new scenes.

## Key Contributions  
- Shadow pairs: video pairs that replay the same dynamics under independently resampled appearance, built at scale in a library so that a dynamics family becomes controllable exactly when such pairs can be constructed for it.  
- Cross‑shadow prediction: learns actions by predicting one shadow from the other, discarding arbitrary pairing resampling and preserving only the action, yielding a unified dynamics representation that drives a block‑causal world model.  
- Block‑causal world model integration: the learned representation is used as input to a block‑causal controller, enabling any‑action rollout in new environments.

## Methodology  
The authors first generate a large Shadow Library containing many videos paired with their shadows under different resamplings. They then train a cross‑shadow predictor to infer one shadow from another, which reveals the underlying dynamics independent of appearance. This predictor outputs an action vector that is fed into a block‑causal world model, allowing frame‑level control. The system can roll out actions in new scenes without additional labels or motion estimators.

## Results  
Experiments across diverse dynamics families show improved action transfer and longer rollouts compared to latent‑action and interactive world model baselines. The average blinded win rate in rollout comparisons is 86 %. Video examples are available at https://ShadowDancer-1.github.io

## Significance  
This work decouples dynamics from appearance, enabling universal action control across scenes, reducing reliance on fine‑tuning and motion estimation, and opening a scalable path for interactive video generation.

## Related Concepts  
unified dynamics representation, shadow pairs, cross‑shadow prediction, block‑causal world models, any‑action control, interactive video generation.
