---
title: Understanding the Synergy between SFT, RLVR, and OPD in LLM Post-Training
published: 2026-09-25T18:39:32Z
authors: Emre Can Acikgoz, Yang Li, Zeyu Leo Liu, Srijan Bansal, Dilek Hakkani-Tür, Shafiq Joty, Semih Yavuz
url: http://arxiv.org/abs/2609.31900v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding the Synergy between SFT, RLVR, and OPD in LLM Post-Training

## Abstract
Modern LLM post-training composes supervised fine-tuning (SFT), reinforcement learning with verifiable rewards (RLVR), and on-policy distillation (OPD) into multi-stage pipelines, yet these stages are typically designed and evaluated in isolation. We show that this composition is consequential: a stage that improves the current model can make the next stage less effective. Through controlled experiments with Qwen3 models on math and science reasoning, we first characterize OPD across nine student-teacher pairs spanning 2x to 53x parameter ratios and show that OPD effectiveness depends on student-teacher compatibility rather than teacher scale alone. The surrounding stages of OPD reshape this compatibility in three ways: (1) A brief SFT warm-up improves subsequent OPD, while an RLVR-strengthened student regresses under distillation from the same teacher. (2) Adapting the teacher with RLVR raises downstream OPD accuracy in proportion to the capability it adds. Following these two interventions, we find that combining teacher adaptation and student warm-up alone raise average OPD accuracy from 29.2\% to 43.8\% (50\% relative improvement) after the same number of distillation steps, with additional preparatory training. (3) At comparable accuracy, OPD leaves a stronger initialization for downstream RLVR than SFT, with a gap that widens as RL compute scales. Our results suggest that each post-training stage should be chosen not only for the capability it adds, but for the learning interface it creates for the next stage.

## Metadata
- **Published**: 2026-09-25T18:39:32Z
- **Authors**: Emre Can Acikgoz, Yang Li, Zeyu Leo Liu, Srijan Bansal, Dilek Hakkani-Tür, Shafiq Joty, Semih Yavuz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31900v1)