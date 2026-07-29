---
title: Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories
published: 2026-07-28T10:40:59Z
authors: Jianing Geng, Ruiqi He, Zekun Fei, Biao Yi, Ruijie Wang, Zheli Liu, Xia Hu, Xuansheng Wu, Qingkai Zeng
url: http://arxiv.org/abs/2607.25560v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories

## Abstract
Agent skills package reusable procedures that improve downstream performance. Their lightweight, portable form enables marketplace monetization and private deployment behind cloud-hosted agent interfaces, giving providers incentives to keep high-value skills proprietary. Yet hiding the artifacts does not conceal their behavioral effects, which remain observable in execution trajectories and form a behavioral side channel. We define this exposure as Skill Leakage: reconstructing proprietary skills from trajectories elicited by benign queries, without reference answers or success labels. We introduce SigLeak, a black-box framework that exploits recurring skill signatures in agent behavior. It constructs diverse, decision-rich diagnostic tasks, contrasts matched skill-enabled and skill-disabled trajectories, and iteratively refines a reconstructed skill from the isolated patterns. Across five scenarios, three model families, and three agent frameworks, SigLeak outperforms or matches three baselines in nearly every setting. It raises the success rate by 6.88 percentage points over the skill-disabled reference on average and achieves the highest overall SkillSim, our metric for coarse- and fine-grained semantic similarity. These results show that benign execution trajectories can expose proprietary procedural knowledge. The code is available at https://anonymous.4open.science/r/SigLeak-D1DB.

## Metadata
- **Published**: 2026-07-28T10:40:59Z
- **Authors**: Jianing Geng, Ruiqi He, Zekun Fei, Biao Yi, Ruijie Wang, Zheli Liu, Xia Hu, Xuansheng Wu, Qingkai Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25560v1)