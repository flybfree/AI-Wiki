---
title: Learning from Scarce Labels: Multi-View Echocardiography for Ejection Fraction Prediction
url: http://arxiv.org/abs/2609.02969v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_09-13-36Z_LearningfromScarceLabels_Multi_ViewEchocardiograph.md
generated_at: 2026-09-03 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new dataset of over 25,000 parasternal long-axis echocardiographic videos labeled with left ventricular ejection fraction and trains the first reproducible model using view classifiers and proxy labeling. The model achieves a mean absolute error of 6.86% which matches clinical standards.

## Key Takeaways
- The authors created a large labeled PLAX-EF dataset by correlating clinical notes with video timestamps, enabling supervised training where direct labels were scarce.
- Fine‑tuning view classifiers and using proxy labels allowed the model to reach a MAE of 6.86%, comparable to apical four‑chamber methods that report 6‑7% error.
- Simple unweighted late fusion of PLAX and A4C predictions improves both single‑view baselines, lowering MAE to 6.37%.

## Context
This work addresses the longstanding challenge of limited labeled medical imaging data in AI research, where generating synthetic labels is difficult. By combining temporal clinical information with visual models, it demonstrates a practical path toward scalable diagnostic tools.

## Implications
For clinicians, the model offers an alternative EF estimation method when apical views are unavailable, reducing reliance on invasive measurements. For industry, the dataset and open‑source demos accelerate research in medical image AI, fostering reproducible solutions that can be integrated into clinical workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02969v1)
