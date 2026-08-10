---
title: Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection
published: 2026-08-07T02:02:19Z
authors: Jiazhuo Li, Yiming Fei, Zhiruo Zhou, Heikichi Hayashi
url: http://arxiv.org/abs/2608.06706v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection

## Abstract
Latent world models plan by predicting future states from an action, but when a scene contains motion the agent does not control, they quietly go action-blind: predictions for different actions become indistinguishable even as the training loss keeps improving. Existing remedies suppress this distraction with reconstruction, task reward, or auxiliary objectives, each adding machinery or assumptions. We show that a minimal alternative suffices, borrowed from the dueling decomposition of value into a state baseline and an action advantage: in latent dynamics, subtracting a prediction's mean effect over actions cancels whatever the actions share--the action-independent variation where distractors live--leaving a clean, controllable channel, with no reward, no reconstruction, and no distractor-specific auxiliary loss. Because this is only a subtraction at readout time, it applies unchanged to any action-conditioned world model, including frozen pretrained ones. Across a gridworld, synthetic generators with known factors, distracting continuous control, and natural-pixel Atari, the isolated channel recovers the agent's own effect where entangled predictors fail, with nuisance leak indistinguishable from zero; applied post hoc it surfaces an action channel in off-the-shelf models that their raw readouts miss, and it converts into goal-reaching control in the gridworld. We prove the cancellation is exact in finite samples for both discrete and sampled action sets, and we state its measured boundary--distractors whose motion tracks the action--together with the remaining limitations in the appendix.

## Metadata
- **Published**: 2026-08-07T02:02:19Z
- **Authors**: Jiazhuo Li, Yiming Fei, Zhiruo Zhou, Heikichi Hayashi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06706v1)