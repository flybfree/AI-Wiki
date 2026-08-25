---
title: Macro-Action Topological Navigation under Noisy Localization using Reinforcement Learning
published: 2026-08-24T09:57:43Z
authors: Simon Hakenes, Tobias Glasmachers
url: http://arxiv.org/abs/2608.23055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Macro-Action Topological Navigation under Noisy Localization using Reinforcement Learning

## Abstract
Navigating large, photorealistic 3D apartments from raw pixels is widely considered infeasible for plain reinforcement learning. We build an agent that does it anyway, estimating its own pose from the camera alone. The agent has to reach several target objects in sequence, and their positions change between episodes, so it must explore to find them. It builds on our earlier object-centric topological controller, which still read the agent's true pose and its object detections from the simulator. Here we replace that true pose with an onboard, object-centric estimate. For each object we keep a bank of ORB features that, when the object is seen again, yield a rough pose measurement, which a minimal Extended Kalman Filter (EKF) fuses with a motion model. As on a real robot, the executed motions are noisy. The estimate drifts, but the agent and the nearby objects drift together, so a locally consistent pose is enough to follow each short edge and then home in visually on the target, which lets us replace full SLAM with a much smaller model, closer to how biological navigation appears to work. In the photorealistic Habitat simulator, the agent reaches its target objects from vision alone, with a pose that only needs to be locally consistent.

## Metadata
- **Published**: 2026-08-24T09:57:43Z
- **Authors**: Simon Hakenes, Tobias Glasmachers
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23055v1)