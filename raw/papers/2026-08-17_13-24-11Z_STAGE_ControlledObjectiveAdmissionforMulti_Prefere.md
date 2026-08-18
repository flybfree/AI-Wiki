---
title: STAGE: Controlled Objective Admission for Multi-Preference LLM Alignment
published: 2026-08-17T13:24:11Z
authors: Yongqi Tong, Zhenyu Zhang, Ruirui Wang, Kewei Fu, Shaoqing Lin, Sijie Dong, Jiang-Ming Yang, Xin Zhang, Jianshe Li
url: http://arxiv.org/abs/2608.16553v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STAGE: Controlled Objective Admission for Multi-Preference LLM Alignment

## Abstract
Multi-preference alignment is often framed as scalarization: combine reward dimensions, then optimize. This leaves a temporal decision underspecified: when should each preference dimension enter policy optimization? We propose \methodname, a stability-guided active-set controller for controlled objective admission. \methodname starts from a small active set, retains admitted objectives, and expands when reward-deviation gates indicate low recent deviation or a patience budget is exhausted. A probing phase estimates a hard-to-easy order, and adaptive weighting emphasizes underperforming active dimensions. Automatic evaluations with 15 training preferences and 16 held-out benchmark columns show that \methodname obtains higher averages than simultaneous scalarization and shared-budget adapted baselines. Component ablations and expansion dynamics further support cumulative retention, gated admission, and probing-derived ordering as useful design choices in this setting. These results position objective-entry timing as a concrete control variable in reward-vector RLHF.

## Metadata
- **Published**: 2026-08-17T13:24:11Z
- **Authors**: Yongqi Tong, Zhenyu Zhang, Ruirui Wang, Kewei Fu, Shaoqing Lin, Sijie Dong, Jiang-Ming Yang, Xin Zhang, Jianshe Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16553v1)