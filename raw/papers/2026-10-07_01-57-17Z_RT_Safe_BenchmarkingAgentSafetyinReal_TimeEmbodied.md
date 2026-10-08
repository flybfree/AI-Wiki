---
title: RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment
published: 2026-10-07T01:57:17Z
authors: Tianruo Rose Xu, Jiawei Ren, Yichi Yang, Zhaoxu Zheng, Lianhui Qin
url: http://arxiv.org/abs/2610.09294v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment

## Abstract
Rapid progress in AI agents has brought growing attention to agent safety, with extensive evaluation focused on digital environments. As agents move into the physical world, embodied safety becomes increasingly important: failures can cause human injury and costly hardware damage. Beyond selecting safe actions, embodied agents must also operate under real-time constraints: the physical world does not pause while an agent reasons. As pedestrians move and vehicles approach during inference, an action that appears safe at observation time may become unsafe before execution. Real-time embodied safety therefore depends on both decision quality and decision latency. We introduce RT-SAFE, a simulated urban benchmark for evaluating embodied-agent safety under real-time constraints. RT-SAFE combines navigation tasks with moving actors, environmental hazards, and traffic rules, while allowing the world to evolve throughout inference and action execution. Across eight VLMs, agents achieve high task completion yet almost never complete safely: in the hardest setting, only 0.7% of episodes finish without a safety event. More strikingly, matched static and real-time evaluations yield task completion rates of 91.3% and 94.1%, respectively, while real-time execution increases collisions by $12.3\times$. These results reveal that standard task success can mask substantial safety failures, and that decision latency itself can become a source of physical risk. Finally, we show that RT-SAFE can support offline RL training and substantially reduce collision rates while achieving strong task completion.

## Metadata
- **Published**: 2026-10-07T01:57:17Z
- **Authors**: Tianruo Rose Xu, Jiawei Ren, Yichi Yang, Zhaoxu Zheng, Lianhui Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09294v1)