---
title: Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology
published: 2026-08-13T17:38:13Z
authors: Yunsung Chung, Yingshuo Liu, Abboud F. Hassan, Han Feng, Mary M. Maleckar, Nassir Marrouche, Jihun Hamm
url: http://arxiv.org/abs/2608.13518v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology

## Abstract
Many clinical prediction models treat post-intervention outcomes as a one-step mapping from baseline measurements to a future endpoint. However, recovery after a procedure often unfolds as an irregular trajectory: clinical observations, medication changes, repeat interventions, and physiological measurements are recorded asynchronously and can change risk assessment over time. We propose an intervention-aware clinical world model that represents each patient with a structured latent state and evolves it through time-ordered post-intervention events. The model first encodes baseline imaging into a 3D spatial latent state. It then updates this state using procedural context, static covariates, elapsed time, and peri-event physiological embeddings. Follow-up imaging provides training-only supervision through a latent forecasting objective. We apply the framework to atrial fibrillation ablation. During the 90-day recovery window, irregular post-procedure records provide clinically meaningful evidence for long-term recurrence risk. In repeated internal cross-validation on DECAAF-II, our model achieves AUROC 0.756 and AUPRC 0.777 for recurrence prediction. It also achieves a scar-extent MAE of 2.971 percentage points without requiring follow-up MRI intensities at inference. The learned state supports recurrence-risk queries at different horizons and retrospective input editing of blanking-period records.

## Metadata
- **Published**: 2026-08-13T17:38:13Z
- **Authors**: Yunsung Chung, Yingshuo Liu, Abboud F. Hassan, Han Feng, Mary M. Maleckar, Nassir Marrouche, Jihun Hamm
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13518v1)