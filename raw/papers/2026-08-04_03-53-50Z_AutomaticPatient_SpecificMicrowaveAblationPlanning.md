---
title: Automatic Patient-Specific Microwave Ablation Planning Accelerated by a Physics-Guided Deep Learning Model
published: 2026-08-04T03:53:50Z
authors: Seonaeng Cho, Minjee Seo, Minju Seol, Juil Park, Joon Ho Kwon, Kyungho Yoon
url: http://arxiv.org/abs/2608.03086v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automatic Patient-Specific Microwave Ablation Planning Accelerated by a Physics-Guided Deep Learning Model

## Abstract
Microwave ablation (MWA) is a promising minimally invasive treatment for liver tumors, but its therapeutic outcome strongly depends on patient-specific planning of antenna insertion trajectory, power, and treatment duration. Accurate numerical simulation can provide physically reliable ablation predictions; however, its high computational cost limits its use in optimization-based planning, where repeated forward evaluations are required. To address this issue, we propose a digital twin-based automatic planning framework that combines a neural ablation prediction model with a genetic algorithm. The model was trained on multiphysics simulation data generated from patient-specific tumor and vessel structures, antenna configurations, and treatment conditions, and was used as a fast forward model during planning. The prediction model achieved a Dice score of 95.1%, enabling accurate deep learning-based optimization. In 13 unseen planning cases, the proposed method improved ablation efficiency by 54.3% and reduced organ damage by 55.0% compared with clinician-defined planning, while slightly shortening the insertion path length by 3.3%. Most generated plans were also judged clinically applicable by MWA specialists. Furthermore, the framework enabled approximately 420-fold faster planning than numerical-simulation-based planning, demonstrating its potential as a fast digital twin for quantitative and personalized MWA treatment planning. The code is available at: https://github.com/SeonAengCho/MWA-Planning.git

## Metadata
- **Published**: 2026-08-04T03:53:50Z
- **Authors**: Seonaeng Cho, Minjee Seo, Minju Seol, Juil Park, Joon Ho Kwon, Kyungho Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03086v1)