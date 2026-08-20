---
title: Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation
published: 2026-08-19T07:51:50Z
authors: Harry Robertshaw, Maxence Boels, Nikola Fischer, Sebastien Ourselin, Christos Bergeles, Alejandro Granados, Thomas C Booth
url: http://arxiv.org/abs/2608.18647v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation

## Abstract
Autonomous endovascular navigation could support the delivery of mechanical thrombectomy to underserved areas, but controllers must navigate long, multi-stage paths across varying vascular anatomies. This study investigates Progressive Experience Fusion (PEF) to train a multi-task TD-MPC2 controller. We additionally evaluate a heuristic that changes the Model Predictive Path Integral planning horizon using residual action-sequence dispersion, and fine-tuning in a patient-specific simulation. Across five subtasks in ten known training anatomies with held-out targets, PEF achieved a mean success rate of 74%, compared with 37% for Soft Actor-Critic (p < 0.001) and 65% for base TD-MPC2 (p = 0.053). A PEF controller with adaptive-horizon planning trained on 30 vasculatures achieved a mean success rate of 90% in ten held-out vasculatures. The PEF agent successfully transferred to an unseen in vitro stroke patient vasculature under fluoroscopy, achieving a mean path ratio improvement from 63% to 80% with fine-tuning (p < 0.001), following 40x103 fine-tuning steps (corresponding to approximately 107 min of clinical inter-hospital transfer time). This work represents a proof of concept for multi-vasculature training and patient-specific adaptation, while further validation is required before clinical deployment.

## Metadata
- **Published**: 2026-08-19T07:51:50Z
- **Authors**: Harry Robertshaw, Maxence Boels, Nikola Fischer, Sebastien Ourselin, Christos Bergeles, Alejandro Granados, Thomas C Booth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18647v1)