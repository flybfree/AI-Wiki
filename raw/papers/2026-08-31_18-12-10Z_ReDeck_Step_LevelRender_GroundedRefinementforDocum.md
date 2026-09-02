---
title: ReDeck: Step-Level Render-Grounded Refinement for Document-to-Slide Generation
published: 2026-08-31T18:12:10Z
authors: Muzhao Tian, Zezi Zeng, Yifan Yang, Xin Gao, Yan Li, Zisu Huang, Xiaohua Wang, Changze Lv, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Xiaoqing Zheng, Ji Li, Chong Luo
url: http://arxiv.org/abs/2609.00194v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReDeck: Step-Level Render-Grounded Refinement for Document-to-Slide Generation

## Abstract
Document-to-slide generation is challenging because slides are dense editable artifacts that require both faithful content selection and precise spatial layout. Recent slide agents adopt iterative reflection, but typically follow a monolithic "one version, one feedback" loop: a slide or deck is rewritten, rendered afterward, and critiqued only at the turn boundary. This delayed feedback makes local failures such as overflow, overlap, clipping, and off-canvas placement difficult to attribute and repair. We propose ReDeck, a step-level render-grounded refinement framework that decomposes slide revision into atomic edit actions and returns renderer-derived observations after each step, turning refinement into "one edit, one observation." To balance local repair with global quality, ReDeck uses multi-granular feedback: step-level render feedback for spatial errors, a turn-level adaptive critic for semantic and design guidance, and a submission-level gate for hard layout validation. We further introduce DeckQuiz, a benchmark that decouples content fidelity, spatial correctness, and design quality. Across GPT-5.4, Claude-4.6, and Gemini-3.1, ReDeck consistently outperforms existing slide-generation agents, and ablations confirm that feedback timing and granularity are critical for reliable slide refinement.

## Metadata
- **Published**: 2026-08-31T18:12:10Z
- **Authors**: Muzhao Tian, Zezi Zeng, Yifan Yang, Xin Gao, Yan Li, Zisu Huang, Xiaohua Wang, Changze Lv, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Xiaoqing Zheng, Ji Li, Chong Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00194v1)