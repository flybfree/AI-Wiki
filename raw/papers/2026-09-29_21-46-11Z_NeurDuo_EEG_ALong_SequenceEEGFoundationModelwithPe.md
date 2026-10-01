---
title: NeurDuo-EEG: A Long-Sequence EEG Foundation Model with Persistent State and Explicit Memory
published: 2026-09-29T21:46:11Z
authors: Yifan Wang, Haiping Liu, Yang Cui, Wenhao Cai, Shuhang Li, Xiaoyang Huang, Xianyang Liu, Jingyu Sun, Yizheng Sun, Cunhang Fan, Tianming Du, Jiancheng Yang, Zhenhong Li, Yunhao Zhang, Hongpeng Zhou, Jingyuan Sun
url: http://arxiv.org/abs/2609.38587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeurDuo-EEG: A Long-Sequence EEG Foundation Model with Persistent State and Explicit Memory

## Abstract
Electroencephalography (EEG) is recorded continuously over hours, with relevant dynamics spanning timescales from milliseconds to hours. Most EEG foundation models nevertheless process fixed windows independently, limiting their ability to capture information encoded in long-timescale dynamics. State-space architectures enable persistent recurrent processing, but long-range information remains implicitly compressed in recurrent states. We present NeurDuo-EEG, a causal EEG foundation model with channel-resolved persistent memory. NeurDuo-EEG introduces multi-timescale memory management with learned consolidation and selective retrieval, enabling persistent modelling of continuous EEG with fixed-size state. It is pre-trained on 3,955 hours of EEG from 17 public datasets using multichannel autoregressive prediction of discrete spectral codes. Across three short-window and two long-sequence downstream tasks, NeurDuo-EEG achieves the best performance on four of five benchmarks, including all three short-window tasks and seizure detection, where AUC-PR improves from $0.285$ to $0.471$ over the strongest non-NeurDuo baseline. NeurDuo-EEG also remains competitive on sleep staging and supports efficient streaming inference, with nearly constant per-chunk latency as the available history grows to one hour. Notably, the Small variant achieves this with only 4.7M backbone parameters. These results demonstrate the value of persistent, multi-timescale modelling for both long-sequence and short-window EEG analysis. Our code is available at https://github.com/YifaNNW/NeurDuo-EEG.

## Metadata
- **Published**: 2026-09-29T21:46:11Z
- **Authors**: Yifan Wang, Haiping Liu, Yang Cui, Wenhao Cai, Shuhang Li, Xiaoyang Huang, Xianyang Liu, Jingyu Sun, Yizheng Sun, Cunhang Fan, Tianming Du, Jiancheng Yang, Zhenhong Li, Yunhao Zhang, Hongpeng Zhou, Jingyuan Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38587v1)