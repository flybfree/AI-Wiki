---
title: Brain-Language-Action (BLA) Models: Language-Conditioned EEG for Robotics Control
published: 2026-08-29T00:37:52Z
authors: Alexandr Plashchinsky
url: http://arxiv.org/abs/2608.28967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Brain-Language-Action (BLA) Models: Language-Conditioned EEG for Robotics Control

## Abstract
Electroencephalography (EEG)-based robotic control is commonly formulated as a direct classification problem, in which electrical neural signals are mapped to a fixed set of discrete actions. However, the limited separability and high noise of EEG signals make it difficult to scale this approach to fine-grained robotic control spaces. We introduce Brain-Language-Action (BLA) models, a framework in which language conditions the interpretation of neural representations for robotic action generation. In a BLA, a small set of reliably distinguishable brain states can be dynamically associated with different actions through a language-defined control mapping, allowing a small number of neural classes to apply to a larger global action space.   We develop a proof-of-concept BLA for drone control using motor-imagery EEG from the BCI Competition IV 2a dataset. The system is trained in two stages. First, we evaluate multiple candidate EEG encoder architectures using subject-specific four-class motor-imagery classification, converting 250Hz, 3.5-second, 22-channel EEG samples into five 128-dimensional brain-token embeddings. Second, these embeddings are projected into the embedding space of a pretrained large language model (LLM) and jointly fine-tuned with language instructions to autoregressively generate structured three-token drone actions. Across 840 possible language-defined mappings between four neural states and seven flight action combinations, the resulting BLA achieves 90% per-token accuracy during evaluation. These results provide an initial demonstration that language conditioning can expand the effective control range of EEG-based robotic interfaces without requiring a corresponding increase in the number of directly distinguishable neural states.

## Metadata
- **Published**: 2026-08-29T00:37:52Z
- **Authors**: Alexandr Plashchinsky
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28967v1)