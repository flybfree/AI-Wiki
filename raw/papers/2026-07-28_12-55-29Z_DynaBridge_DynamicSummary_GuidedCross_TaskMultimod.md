---
title: DynaBridge: Dynamic Summary-Guided Cross-Task Multimodal Fusion for DASS-Structured Mental Health Assessment
published: 2026-07-28T12:55:29Z
authors: Shiyu Teng, Haichen Yu, Jiaqing Liu, Hao Sun, Yu Song, Shurong Chai, Ruibo Hou, Lanfen Lin, Yen-Wei Chen
url: http://arxiv.org/abs/2607.25679v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DynaBridge: Dynamic Summary-Guided Cross-Task Multimodal Fusion for DASS-Structured Mental Health Assessment

## Abstract
Multimodal behavioral analysis offers a scalable approach to assessing depression, anxiety, and stress, yet generic fusion models often ignore the psychometric structure of questionnaire labels. In DASS-21, risk labels are derived from ordered symptom items through fixed item-to-subscale mappings. We propose \textbf{DynaBridge}, a dynamic summary-guided cross-task multimodal framework for DASS-structured mental health assessment. DynaBridge encodes acoustic, visual, and textual cues across multiple sessions and augments them with frozen-LLM-generated DASS-aware summaries as participant-level semantic evidence. It predicts ordinal item distributions, reconstructs depression, anxiety, and stress risk evidence from item-level soft scores, and fuses this evidence with direct multimodal risk predictions. A confidence-aware refinement strategy further incorporates high-confidence semantic cues conservatively. On the official AdoDAS validation split, DynaBridge outperforms the official baseline and representative multimodal methods, achieving 0.5012 mean F1 for D/A/S risk prediction and 0.3216 mean QWK for DASS-21 item prediction. These results show the value of bridging multimodal cues, semantic summaries, and DASS-21 psychometric structure.

## Metadata
- **Published**: 2026-07-28T12:55:29Z
- **Authors**: Shiyu Teng, Haichen Yu, Jiaqing Liu, Hao Sun, Yu Song, Shurong Chai, Ruibo Hou, Lanfen Lin, Yen-Wei Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25679v1)