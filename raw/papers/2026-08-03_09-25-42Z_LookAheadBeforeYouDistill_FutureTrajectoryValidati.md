---
title: Look Ahead Before You Distill: Future Trajectory Validation of Teacher Guidance for Agentic On-Policy Distillation
published: 2026-08-03T09:25:42Z
authors: Chishui Chen, Yaoyou Fan, Te Sun, Yi Yang, Chenghao Sun, Delin Mao, Hongbo Qiao, Zuowei Zhang, Junxi Wang, Chenxing Sun, Yangen Hu, Lu Pan, Xuyang Liu, Linfeng Zhang
url: http://arxiv.org/abs/2608.01953v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Look Ahead Before You Distill: Future Trajectory Validation of Teacher Guidance for Agentic On-Policy Distillation

## Abstract
On-policy distillation (OPD) provides teacher supervision on states visited by the student, reducing the distribution gap between training and inference. However, in multi-turn agentic tasks, student deviations may accumulate over time, gradually moving the trajectory away from states where teacher guidance remains effective. Our quantitative analysis further shows that high-disagreement states offer promising opportunities for teacher guidance, but determining whether such guidance is beneficial requires examining its effect on subsequent student trajectories. We propose FutureBridge-OPD (FTB), which executes a short teacher bridge at a high disagreement state and uses the resulting student continuation to assess whether the bridge increases the density of positive distillation signals relative to the teacher. On ALFWorld, WebShop, and ScienceWorld, under the main Qwen3-32B teacher to Qwen3-1.7B student setting, FTB outperforms vanilla OPD and TCOD by an average of 16.6 and 7.6 points, respectively, and remains effective across student scales and teacher settings. Our code is publicly available at https://github.com/ChenChiShui/FutureBridge-OPD.

## Metadata
- **Published**: 2026-08-03T09:25:42Z
- **Authors**: Chishui Chen, Yaoyou Fan, Te Sun, Yi Yang, Chenghao Sun, Delin Mao, Hongbo Qiao, Zuowei Zhang, Junxi Wang, Chenxing Sun, Yangen Hu, Lu Pan, Xuyang Liu, Linfeng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01953v1)