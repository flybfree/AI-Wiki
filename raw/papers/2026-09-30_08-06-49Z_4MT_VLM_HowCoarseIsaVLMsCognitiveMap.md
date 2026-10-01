---
title: 4MT-VLM: How Coarse Is a VLMs Cognitive Map?
published: 2026-09-30T08:06:49Z
authors: Markus Frey
url: http://arxiv.org/abs/2609.39238v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# 4MT-VLM: How Coarse Is a VLMs Cognitive Map?

## Abstract
An agent that moves must recognise a place from a viewpoint it has never seen. We introduce 4MT-VLM, a dataset of procedurally generated landscapes, each rendered across five stimulus modes that remove appearance cues while holding layout fixed: shape and colour, shape only, colour only, bare terrain peaks with no objects, and a valley viewpoint that puts the peaks on the horizon. The last condition is commonly used in clinics to probe hippocampal function in human patients. We test this benchmark across sixteen different open and closed-source models and report 4AFC performance, a measure which is also used to grade human participants. We observe that models identify a place from the studied viewpoint but lose it once the camera moves, dropping below the 25% chance level at 135° where a human observer scores 85%. Frontier models (Gemini 3.8 Flash, GPT-5.6) answer only 39% and 31% of rotated trials correctly, recovering to 85% and 55% only when distractors are moved more than 30 meters apart. Our benchmark demonstrates that while current VLMs possess rudimentary cognitive maps, their spatial resolution remains fundamentally too coarse to maintain a stable, 3D understanding of the world once the viewpoint changes.

## Metadata
- **Published**: 2026-09-30T08:06:49Z
- **Authors**: Markus Frey
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39238v1)