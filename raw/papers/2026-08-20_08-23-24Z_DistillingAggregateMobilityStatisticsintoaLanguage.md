---
title: Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation
published: 2026-08-20T08:23:24Z
authors: Tatsuya Amano, Hirozumi Yamaguchi
url: http://arxiv.org/abs/2608.19778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation

## Abstract
Pedestrian simulators need a behaviour rule for every agent, but privacy usually limits the data for setting one to aggregate statistics, namely zone-level device counts and origin-to-destination (OD) flows, with no individual trajectories. Such aggregates under-determine individual behaviour, because many different sets of decisions reproduce the same counts. We fine-tune a language model crowd agent so that the simulated population matches the observed destination composition, the fraction of the departing crowd heading to each point of interest. We read this target from the OD flow and reweight the model's own destination distribution onto it by iterative proportional fitting. Because fine-tuning inflates the dominant destination class, we fit the low-rank adapter to trajectories resampled to a corrected training composition that reaches the target after this inflation. On mobile network counts from two baseball games the fine-tuned agent runs without inference-time correction, cutting the destination-share error by 25%, while the grid correlation remains similar across policies.

## Metadata
- **Published**: 2026-08-20T08:23:24Z
- **Authors**: Tatsuya Amano, Hirozumi Yamaguchi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19778v1)