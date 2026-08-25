---
title: Inferring Action from Future Latent State for Robotic Manipulation
published: 2026-08-22T18:17:36Z
authors: Fenghao Lei, Zhixiong Huang, Long Yang, Jiabao Chen, Jie Cheng, Peilin Huang, Han Fu, Zhuo Li, Xiaoxue Ren
url: http://arxiv.org/abs/2608.22067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inferring Action from Future Latent State for Robotic Manipulation

## Abstract
World-Action Models (WAMs) build robot control on video-generation backbones, which jointly predict dense future visual trajectories and robot actions. We argue that video generation is an unnecessary intermediate objective for world-action modeling. For robotic manipulation, the goal of a world model is not to reproduce how the world looks at every intermediate moment, but to predict the state that the world will reach after an action is executed. The intermediate frames only describe the visual transition between physical states, which consumes substantial model capacity and computation, but do not directly specify the physical outcome that the robot action is intended to produce. In this paper, we propose DELE-w0.5, which infers robot actions from predicted future states without relying on video generation. Concretely, DELE-w0.5 infers the action sequence from its corresponding compact future latent state. The future latent state captures the action-relevant physical outcome of robot interaction and serves as an explicit bridge between world modeling and action generation. The core design principle of DELE-w0.5 is to model how the physical world changes under robot actions, rather than how its visual appearance evolves frame by frame. This formulation removes the high-dimensional visual redundancy introduced by dense video representations, and it therefore enables cheaper training and low-latency inference. Across 480 real-robot trials on four long-horizon manipulation tasks, our DELE-w0.5 achieves the best performance among all compared policies, attaining 62.5 overall full-task success and 81.3 macro ordered-stage progress, outperforming the strongest baseline by 47.5 and 30.7 percentage points, respectively.

## Metadata
- **Published**: 2026-08-22T18:17:36Z
- **Authors**: Fenghao Lei, Zhixiong Huang, Long Yang, Jiabao Chen, Jie Cheng, Peilin Huang, Han Fu, Zhuo Li, Xiaoxue Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22067v1)