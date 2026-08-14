---
title: Foundation models for movement data: Are they ready for prime-time?
published: 2026-08-13T14:39:53Z
authors: Alexander Bräuer, Benjamin Cauchi, Nils Strodthoff
url: http://arxiv.org/abs/2608.13316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Foundation models for movement data: Are they ready for prime-time?

## Abstract
Foundation models (FMs) trained on large-scale accelerometer data have been proposed as general-purpose feature extractors for health monitoring, but systematic evidence of their advantages is lacking. We present the first comprehensive evaluation of four open-source accelerometer FMs against supervised baselines covering 19 tasks across the domains of activity recognition including activities of daily living, clinical monitoring, and physiological inference. We find task-dependent performance results: supervised models remain competitive with FMs on human action recognition (HAR), with no consistent advantage for either, while selected FMs lead on fall and stress detection and are the most robust to sensor-placement variation. As frozen feature extractors, FMs are strongest for demographic inference, whereas sleep staging performance remains near chance level for all models. The internal FM representations show strong similarity across layers, highlighting potential for future FM improvements. Linear and frozen probing reveals that UniMTS provides the strongest representations and is the only FM that surpasses the supervised baselines without finetuning. Concept discovery analysis shows all models capture high-intensity activities clearly but struggle with sedentary, complex or ambiguous activities. We provide scenario-based deployment recommendations. Furthermore, we identify FM-derived activity profile inference-moving beyond fixed category classification-as a promising research direction.

## Metadata
- **Published**: 2026-08-13T14:39:53Z
- **Authors**: Alexander Bräuer, Benjamin Cauchi, Nils Strodthoff
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13316v1)