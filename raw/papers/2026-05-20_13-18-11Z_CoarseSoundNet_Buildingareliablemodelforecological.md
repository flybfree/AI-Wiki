---
title: CoarseSoundNet: Building a reliable model for ecological soundscape analysis
published: 2026-05-20T13:18:11Z
authors: Alexander Gebhard, Andreas Triantafyllopoulos, Dominik Arend, Sandra Müller, Svenja Schmidt, Michael Scherer-Lorenzen, Björn W. Schuller
url: http://arxiv.org/abs/2605.21143v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoarseSoundNet: Building a reliable model for ecological soundscape analysis

## Abstract
A soundscape is composed of three types of sound: biophony (sounds made by animals), geophony (natural abiotic sounds) and anthropophony (sounds made by humans). A key research question in the field of soundscape ecology is how these components interact with each other, specifically how biophony responds to geophony and anthropophony. Nevertheless, as of today, there are not many analytical instruments that enable the distinct quantification of these elements. Recent machine learning (ML) approaches aim to support automated analysis but often rely on task-specific or clean data, limiting generalisation to noisy passive acoustic monitoring (PAM) recordings. This study presents a clear and reproducible structure to build ML models for coarse soundscape classification and introduces CoarseSoundNet, a deep learning model trained to distinguish biophony, geophony, and anthropophony under realistic PAM conditions. We systematically investigate model architectures, the influence of an additional training class, data composition, and evaluation strategies. Our findings suggest that model performance improves with additional PAM data, especially when similar to the target domain, and by introducing an explicit silence class during training. Class-specific decision thresholds and duration-based constraints further enhance performance, particularly for anthropophony and geophony. Error analyses exhibit challenges for anthropophony due to masking effects and confusions for silence and insect sounds for geophony and biophony. Finally, we conduct an ecological case study which shows that pre-filtering recordings with CoarseSoundNet yields acoustic index trends comparable to ground-truth filtering, supporting its use as an effective preprocessing tool for ecoacoustic analyses.

## Metadata
- **Published**: 2026-05-20T13:18:11Z
- **Authors**: Alexander Gebhard, Andreas Triantafyllopoulos, Dominik Arend, Sandra Müller, Svenja Schmidt, Michael Scherer-Lorenzen, Björn W. Schuller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.21143v1)