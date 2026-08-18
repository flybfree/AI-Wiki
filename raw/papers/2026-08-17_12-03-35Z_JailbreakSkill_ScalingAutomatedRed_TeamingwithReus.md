---
title: JailbreakSkill: Scaling Automated Red-Teaming with Reusable and Ever-Evolving Skills
published: 2026-08-17T12:03:35Z
authors: Xiaoyu Wen, Jiajia Li, Zhida He, Peng Yu, Chenxu Wang, Han Qi, Ziyuan Zhou, Cheng Jin, Ying Wen, Xingcheng Xu, Shuyue Hu, Tianhang Zheng, Chaochao Lu, Qiaosheng Zhang
url: http://arxiv.org/abs/2608.16465v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JailbreakSkill: Scaling Automated Red-Teaming with Reusable and Ever-Evolving Skills

## Abstract
Automated red-teaming has produced a growing collection of attack strategies, yet they typically remain scattered across prompts and workflows, making them difficult to systematically integrate, reuse, and improve at scale. We introduce \textsc{JailbreakSkill}, a skill-centric framework for scaling automated red-teaming through reusable and continuously evolving attack capabilities. \textsc{JailbreakSkill} packages existing attack strategies into modular, agent-ready skills that can be directly reused and adaptively selected across tasks and target models. Beyond reuse, it closes the loop between attacking and learning: attack experience is used to diagnose, refine, combine, and discover new skills, which are added back to an ever-growing skill library. This evolution lifts macro-average ASR by 17.5 percentage points on AdvBench and 13.4 points on HarmBench, including a 48.6-point gain against GPT-5.4 on AdvBench, while yielding novel attack strategies such as reframing a direct request as an unfinished document-completion task. Several evolved skills also generalize to unseen prompts and target models without further adaptation. Our code is available at https://github.com/BattleWen/JailbreakSkill.

## Metadata
- **Published**: 2026-08-17T12:03:35Z
- **Authors**: Xiaoyu Wen, Jiajia Li, Zhida He, Peng Yu, Chenxu Wang, Han Qi, Ziyuan Zhou, Cheng Jin, Ying Wen, Xingcheng Xu, Shuyue Hu, Tianhang Zheng, Chaochao Lu, Qiaosheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16465v1)