---
title: Towards Context-Aware Clinical Motion Understanding in Daily Living at Home: Freezing of Gait Detection with Egocentric Vision
published: 2026-08-13T14:16:49Z
authors: Vayalet Stefanova, Diwas Lamsal, Margot Genbrugge, Maxim Yudayev, Christian Schlenstedt, Moran Gilat, Bart Vanrumste, Benjamin Filtjens
url: http://arxiv.org/abs/2608.13283v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Context-Aware Clinical Motion Understanding in Daily Living at Home: Freezing of Gait Detection with Egocentric Vision

## Abstract
Understanding motion in daily living requires context beyond kinematics, because similar inertial patterns during activities of daily living (ADLs) can reflect intentional stopping, object interaction, or pathological movement impairment. Egocentric vision provides task-related context that may help disambiguate these cases. We investigate this challenge through freezing of gait (FOG) detection in Parkinson's disease (PD), a symptom strongly influenced by contextual factors during ADLs. Using synchronized egocentric video, wearable IMUs, and expert-annotated FOG labels collected from 13 PD participants in their homes, we evaluate frozen representations from pretrained ego-video and time-series foundation models, alongside an IMU-based TCN trained from scratch, under leave-one-subject-out evaluation. The IMU-based TCN achieved the strongest event-detection performance, reaching 42.3 F1 and 83.0 AUROC, compared with 32.6 F1 and 77.2 AUROC for V-JEPA2 ego-video features. Although ego-video alone did not outperform IMU-based sensing, it showed above-chance discrimination, and qualitative analyses suggest that egocentric vision may capture FOG-relevant information independent of IMUs. Together, these results support the use of pretrained ego-video representations to add contextual information to wearable-sensor-based clinical motion understanding in daily living.

## Metadata
- **Published**: 2026-08-13T14:16:49Z
- **Authors**: Vayalet Stefanova, Diwas Lamsal, Margot Genbrugge, Maxim Yudayev, Christian Schlenstedt, Moran Gilat, Bart Vanrumste, Benjamin Filtjens
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13283v1)