---
title: FedOrbit: Adaptive Personalized Federated Learning for Non-IID LEO Satellite Constellations
url: http://arxiv.org/abs/2608.09687v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_14-53-48Z_FedOrbit_AdaptivePersonalizedFederatedLearningforN.md
generated_at: 2026-08-11 12:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FedOrbit, an adaptive personalized federated learning framework designed for non‑iid LEO satellite data where orbit geometry creates disjoint class distributions. By integrating continuous inter‑satellite training with class‑aware aggregation and adaptive feature decomposition, FedOrbit achieves the highest accuracy in five of six benchmark settings and remains within 0.9 percentage points of the best result in the sixth.

## Key Takeaways
- Continuous orbit-level training over inter-satellite links enables class‑aware hierarchical aggregation that balances global consistency with local diversity.  
- Quality-weighted feature aggregation with return-rate dampening reduces impact of noisy or infrequent data while preserving useful signals.  
- Adaptive feature decomposition based on inter-orbit class similarity minimizes per‑orbit accuracy spread, yielding the smallest variance across settings.

## Context
Federated learning struggles when training data are non-iid and geographically distributed, as seen in satellite constellations where orbital geometry creates disjoint class distributions. Traditional global aggregation fails to capture these patterns, leading to suboptimal performance. This work addresses those limitations by integrating orbital dynamics into the learning pipeline.

## Implications
For space‑based AI services, FedOrbit offers a scalable solution that can be deployed across thousands of satellites with minimal communication overhead. Practitioners can leverage its adaptive mechanisms to maintain high accuracy even when data partitions are highly non-iid, supporting real‑time decision making in remote sensing and Earth observation applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09687v1)
