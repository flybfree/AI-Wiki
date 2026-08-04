---
title: TRAM: Enhancing Multimodal Reasoning with Trajectory-Derived Auxiliary Memory
published: 2026-08-03T08:57:00Z
authors: Kang Liu, Zijing Wang, Yongkang Liu, Mengjie Zhao, Xiaocui Yang, Shi Feng, Yifei Zhang, Daling Wang
url: http://arxiv.org/abs/2608.01922v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRAM: Enhancing Multimodal Reasoning with Trajectory-Derived Auxiliary Memory

## Abstract
Multimodal Large Reasoning Models (MLRMs) have achieved strong performance on tasks requiring visual understanding and multi-step inference. However, as reasoning trajectories grow, models may become less effective at using information established earlier in the context, increasing the risk of reasoning errors. Existing approaches primarily address this problem by sustaining visual grounding throughout reasoning. However, reasoning also transforms visual observations into task-specific relations, constraints, and intermediate conclusions whose influence may weaken over long trajectories. Our attribution analysis suggests that correctness is not consistently separated by image attribution alone, but is more closely associated with whether trajectories retain and integrate such reasoning-derived information across stages. Motivated by this, we introduce TRAM (TRajectory-derived Auxiliary Memory), a training-free method that augments standard decoding with an auxiliary memory pathway derived from the model's own reasoning trajectory. TRAM consolidates completed reasoning into a compact latent memory, updates it online through fast and slow recurrent streams, and feeds it back into selected decoder layers through a lightweight residual pathway. Experiments across four MLRM variants on eight benchmarks show that TRAM improves performance over vanilla decoding on mathematical, scientific, and general visual reasoning tasks without additional training.

## Metadata
- **Published**: 2026-08-03T08:57:00Z
- **Authors**: Kang Liu, Zijing Wang, Yongkang Liu, Mengjie Zhao, Xiaocui Yang, Shi Feng, Yifei Zhang, Daling Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01922v1)