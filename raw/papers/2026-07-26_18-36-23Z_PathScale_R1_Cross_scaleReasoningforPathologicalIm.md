---
title: PathScale-R1: Cross-scale Reasoning for Pathological Image Analysis
published: 2026-07-26T18:36:23Z
authors: Chi Phan, Tianyi Zhang, Yufeng Wu, Qiaochu Xue, Jiajie Zhang, Linghan Cai, Zeyu Liu, Sudong Wang, Yueming Jin, Dan Hu
url: http://arxiv.org/abs/2607.23794v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PathScale-R1: Cross-scale Reasoning for Pathological Image Analysis

## Abstract
Pathological diagnosis is inherently multi-scale, requiring the integration of global tissue architecture at low magnification with cellular morphology at higher magnification. However, existing pathology benchmarks and vision-language models (VLMs) are still largely developed under single-scale settings, limiting their ability to learn clinically meaningful multi-magnification reasoning. Moreover, naively constructed visual question answering (VQA) tasks may be susceptible to text-only or superficial visual shortcuts, leading to unreliable assessments of visual understanding. To address these limitations, we introduce a benchmark and training framework for shortcut-resistant cross-scale pathology reasoning. We design an Adversarial Text-only Screening strategy for semantic reasoning questions and a Structure-controlled Distractor Sampling strategy for visual grounding questions, encouraging models to rely on cross-scale visual evidence. Based on this pipeline, we construct PathScale-VQA, a high-quality cross-scale pathology VQA benchmark with 10,373 multiple-choice questions grounded in 1,368 diagnostic paths across multiple magnification levels. Building on the semantic reasoning set, PathScale-R1 is optimized through Difficulty-driven Reasoning Distillation supervised fine-tuning followed by reinforcement learning with a Scale-aware Reasoning Structure reward, which encourages the use of evidence across magnifications. Extensive experiments demonstrate state-of-the-art performance of PathScale-R1 on cross-scale reasoning tasks and effective transfer to conventional single-scale pathology VQA. Our code is available at https://github.com/iMVR-PL/PathScale-R1.

## Metadata
- **Published**: 2026-07-26T18:36:23Z
- **Authors**: Chi Phan, Tianyi Zhang, Yufeng Wu, Qiaochu Xue, Jiajie Zhang, Linghan Cai, Zeyu Liu, Sudong Wang, Yueming Jin, Dan Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23794v1)