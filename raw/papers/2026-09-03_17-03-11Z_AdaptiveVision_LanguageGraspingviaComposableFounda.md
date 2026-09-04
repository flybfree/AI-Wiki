---
title: Adaptive Vision-Language Grasping via Composable Foundation Priors and Generalizable Grasp Synthesis
published: 2026-09-03T17:03:11Z
authors: Sixu Yan, Shikang Wang, Binhua Huang, Xuanlai Tang, Guohua Fan, Fan Huang, Haoxuan Li, Yongkang Li, Yuhan Li, Bencheng Liao, Zeyu Zhang, Wenyu Liu, Hangxin Liu, Xinggang Wang
url: http://arxiv.org/abs/2609.04096v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Vision-Language Grasping via Composable Foundation Priors and Generalizable Grasp Synthesis

## Abstract
This paper proposes AdaRoboVLG, a task-adaptive Vision-Language-Grasp (VLG) framework that supports generalizable grasp synthesis across different robotic hands. Unlike existing VLG methods that tightly couple foundation models with end-to-end grasp policies, AdaRoboVLG learns an efficient generalizable base policy that generates and evaluates physically feasible grasp candidates through explicit kinematic mapping and force-closure-based stability estimation, while offloading task-dependent understanding to specialized foundation-model modules. These modules provide composable priors that are integrated into the grasp synthesis process, enabling contextually adaptive grasp synthesis without retraining the underlying grasp policy. Through extensive simulation and real-world experiments, we demonstrate that (i) the base policy exhibits efficient learning and strong cross-hand generalization, (ii) the framework effectively incorporates spatial, cognitive, and temporal priors to address three representative grasping challenges without compromising grasp synthesis performance compared to state-of-the-art methods, and (iii) these priors can operate jointly to enable functional grasping in cluttered and dynamic environments. These results indicate that decoupling physical grasp synthesis from task-dependent understanding provides a scalable paradigm for robotic grasping, allowing future advances in foundation models to be directly translated into improved grasp capabilities without redesigning or retraining the underlying grasp policy. Supplementary videos are available at https://adarobovlg.github.io/

## Metadata
- **Published**: 2026-09-03T17:03:11Z
- **Authors**: Sixu Yan, Shikang Wang, Binhua Huang, Xuanlai Tang, Guohua Fan, Fan Huang, Haoxuan Li, Yongkang Li, Yuhan Li, Bencheng Liao, Zeyu Zhang, Wenyu Liu, Hangxin Liu, Xinggang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04096v1)