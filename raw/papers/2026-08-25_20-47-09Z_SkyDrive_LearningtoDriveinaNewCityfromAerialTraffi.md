---
title: SkyDrive: Learning to Drive in a New City from Aerial Traffic Monitoring
published: 2026-08-25T20:47:09Z
authors: Weijiang Xiong, Lan Feng, Alexandre Alahi, Nikolas Geroliminis
url: http://arxiv.org/abs/2608.25142v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkyDrive: Learning to Drive in a New City from Aerial Traffic Monitoring

## Abstract
Autonomous driving has made remarkable progress through imitation learning with massive human demonstration data. However, a trained planner often degrades severely when applied to a new environment zero-shot, because of domain shifts in traffic regulations, road layout and driving behaviors. Therefore, adapting a trajectory planner to a new city typically requires resource-demanding local data collection with a vehicle sensor suite. In this work, we show that driving behavior can be learned from a scalable and efficient alternative. We introduce \emph{SkyDrive}, a framework that utilizes drone-based traffic monitoring to provide efficient supervision for autonomous driving agents in a new environment. While vehicle-based data collection logs the ego and its surroundings, an aerial platform naturally observes many road users simultaneously over an extended field of view. As a result, every vehicle can be a data source with grounded driving behavior, effectively scaling up the amount of supervision. Based on 137 hours of aerial traffic monitoring footage, we extract 650K driving samples and construct a benchmark for trajectory planners and motion predictors. Zero-shot experiments with multiple models reveal significant cross-city domain gaps, but many of them can be alleviated by limited supervision from the sky, e.g., 30 minutes of monitoring per location. Our findings show that aerial traffic monitoring is an efficient and scalable data source for adapting autonomous driving systems in new cities. Data and code will be made publicly available.

## Metadata
- **Published**: 2026-08-25T20:47:09Z
- **Authors**: Weijiang Xiong, Lan Feng, Alexandre Alahi, Nikolas Geroliminis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25142v1)