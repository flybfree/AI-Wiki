---
title: Analyzing Speech Condition Effects in Dysarthric ASR: A Layer-wise Probing Study
published: 2026-08-03T08:14:26Z
authors: Darwin Jelestin Muthu, Navya Gupta, Wei Lin Tay, Zhengchen Zhang, Daniel Wang Zhengkui, Rong Tong
url: http://arxiv.org/abs/2608.01865v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Analyzing Speech Condition Effects in Dysarthric ASR: A Layer-wise Probing Study

## Abstract
Automatic speech recognition (ASR) performance degrades sharply on dysarthric speech, yet how disordered articulation reshapes a model's internal representations is underexplored. We present a layer-wise probing analysis of a transformer ASR encoder on Mandarin dysarthric speech under three transcript-matched conditions: original dysarthric speech, speaker conditioned zero-shot TTS resynthesis, and unconditioned TTS. The probes reveal a task-dependent hierarchy: phoneme boundary information stays weak for dysarthric speech at every layer, phoneme identity becomes recoverable toward the upper layers, and recognition difficulty is encoded in the deepest layers. Tone-sensitive evaluation shows Mandarin lexical tone is a persistent error source. Cross-condition similarity divergence grows with depth, indicating that disordered speech affects high-level representations more than low-level acoustic features. Guided by these findings, single-layer LoRA at layer 7 and adaptation on subset layers 5-8 achieve performance within 3.5% and 2.48% relative margins of full encoder adaptation, respectively, while upper-layer adaptation is less effective for dysarthric speech. These findings link representation analysis to parameter-efficient fine-tuning and motivate layer-aware adaptation for low-resource Mandarin dysarthric ASR.

## Metadata
- **Published**: 2026-08-03T08:14:26Z
- **Authors**: Darwin Jelestin Muthu, Navya Gupta, Wei Lin Tay, Zhengchen Zhang, Daniel Wang Zhengkui, Rong Tong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01865v1)