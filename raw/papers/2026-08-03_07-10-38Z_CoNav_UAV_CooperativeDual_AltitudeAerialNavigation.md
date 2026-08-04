---
title: CoNav-UAV: Cooperative Dual-Altitude Aerial Navigation via Stackelberg Learning
published: 2026-08-03T07:10:38Z
authors: Junru Song, Wenhao Zhang, Yang Yang, Xuekai Qiu, Feifei Wang, Weien Zhou, Tingsong Jiang, Ying Wen, Yang Li, Wen Yao
url: http://arxiv.org/abs/2608.01802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoNav-UAV: Cooperative Dual-Altitude Aerial Navigation via Stackelberg Learning

## Abstract
Target-oriented vision-and-language navigation (VLN) on aerial platforms is attracting growing attention for missions such as disaster rescue, infrastructure inspection, and security patrol. In this task, an unmanned aerial vehicle (UAV) needs to locate targets given only a concise description of their appearance and surroundings. This requires global exploration and grounding as well as collision-free close-range approach, two interleaved processes difficult to reconcile within a single agent. Most existing methods transfer the ground VLN paradigm to a low-altitude UAV and compensate for its inefficient exploration with external assistance. A recent attempt deploys two UAVs at complementary altitudes yet still relies on privileged information and trains its two agents independently, precluding any mutual adaptation essential for cooperation. Here we propose CoNav-UAV, which explicitly models the task as a Stackelberg game between a high-altitude leader and a low-altitude follower, with the system operating on onboard visual and linguistic inputs alone. To solve this game, we introduce Iterative Stackelberg Learning. The leader's high-level vision-language reasoning is refined via memory-based in-context learning, while the follower's precise motion control is updated via DAgger-style expert distillation. The alternation drives both agents toward a Stackelberg equilibrium. CoNav-UAV consistently outperforms single- and dual-agent baselines across three high-fidelity urban scenes from the AerialVLN benchmark. Success rate improves by up to 30.8 points on the learning scene, and 9.0 points under cross-scene transfer while using about 3x less adaptation data. Further analyses validate the complementary gains of the leader and follower updates and reveal robust gains yet distinct learning dynamics across VLM backbones.

## Metadata
- **Published**: 2026-08-03T07:10:38Z
- **Authors**: Junru Song, Wenhao Zhang, Yang Yang, Xuekai Qiu, Feifei Wang, Weien Zhou, Tingsong Jiang, Ying Wen, Yang Li, Wen Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01802v1)