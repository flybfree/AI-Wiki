---
title: Adaptation of Generalist Robot Policies with Minimal Data
published: 2026-08-11T19:15:26Z
authors: Shreyas Kowshik, Sreyas Venkataraman, Leo Wang, Niharika Pant, Max Simchowitz, Aviral Kumar
url: http://arxiv.org/abs/2608.11363v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptation of Generalist Robot Policies with Minimal Data

## Abstract
A central goal in robot learning is to move beyond task-specific human data collection toward robots that improve through autonomous interaction. Yet fully autonomous learning remains difficult with current policies: sparse rewards and weak zero-shot exploration make it unlikely that a robot will discover successful behavior from scratch. We study minimal-data adaptation, a regime in which a pre-trained robot policy must learn a new task from as little as one demonstration followed by autonomous online interaction. This setting serves as the closest tractable proxy for fully autonomous improvement, allowing us to study whether minimal human guidance can bootstrap autonomous learning and what algorithmic ingredients make it feasible. We build MiDAS, a simple offline-to-online RL recipe that first anchors a pre-trained VLA to the target task with behavior cloning on single/few demonstrations, then improves it through value-based online RL on a residual policy parameterization. Across LIBERO and RoboCasa, MiDAS recovers strong task performance from as little as one demonstration, substantially outperforming baselines and generalizing beyond demonstrated conditions. We further evaluate MiDAS on a bimanual YAM platform. Starting from a fragile low-success policy obtained from a single demonstration, MiDAS improves its robustness and learns new successful behaviors over ~6 hours of online interaction. To the best of our knowledge, this is the first demonstration of reliable robot policy adaptation from a single task demonstration.

## Metadata
- **Published**: 2026-08-11T19:15:26Z
- **Authors**: Shreyas Kowshik, Sreyas Venkataraman, Leo Wang, Niharika Pant, Max Simchowitz, Aviral Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11363v1)