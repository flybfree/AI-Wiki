---
title: Diagnosing as Cardiologists Do: ECG Agents with Doctor-Grounded Priors for Clinical Reasoning Across Diseases and Populations
published: 2026-08-10T03:00:35Z
authors: Hongxiang Gao, He-yang Xu, Yuwen Li, Minghui Zhao, Zhipeng Cai, Xingyao Wang, Chenxi Yang, Jianqing Li, Chengyu Liu
url: http://arxiv.org/abs/2608.09053v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diagnosing as Cardiologists Do: ECG Agents with Doctor-Grounded Priors for Clinical Reasoning Across Diseases and Populations

## Abstract
Cardiologists interpret electrocardiograms by localizing waveform components, measuring rhythm and interval patterns, and translating these structured observations into diagnostic evidence. Whether this expert reading process can serve as an effective prior for ECG agents remains unclear. To address this question, we introduce LuminaECG, a clinically structured ECG reasoning framework that reformulates ECG interpretation as measurement-grounded visual reading. ECG signals are rendered on standard electrocardiographic grid paper to preserve the spatial and scale cues used in clinical reading. P-wave, QRS-complex, and T-wave boundaries are explicitly delineated, and color-coded segmentation decomposes the waveform into discrete visual measurement primitives. A general 2B vision-language backbone is then trained with low-rank supervised fine-tuning to associate these primitives with diagnostic reasoning, without architectural modification. Across open, proprietary, and ECG-specialist zero-shot baselines, LuminaECG improves both waveform measurement and diagnostic recovery. It reaches a clinically meaningful reader tier on the CODE-test benchmark, transfers across geographically diverse ECG datasets without retraining, and generates reports whose structure contains an emergent prognostic signal. These findings suggest that effective ECG agents require not only larger models, but supervision that preserves the alignment between measurable waveform evidence and clinical knowledge.

## Metadata
- **Published**: 2026-08-10T03:00:35Z
- **Authors**: Hongxiang Gao, He-yang Xu, Yuwen Li, Minghui Zhao, Zhipeng Cai, Xingyao Wang, Chenxi Yang, Jianqing Li, Chengyu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09053v1)