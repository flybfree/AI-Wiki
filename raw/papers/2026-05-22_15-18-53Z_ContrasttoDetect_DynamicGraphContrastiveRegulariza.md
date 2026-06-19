---

title: 'Contrast to Detect: Dynamic Graph Contrastive Regularization for Unsupervised Anomaly Detection in Multivariate Time Series'
published: "2026-05-22T15:18:53Z"
authors: Yunhua Pei, Zixing Song, Jin Zheng, John Cartlidge
url: http://arxiv.org/abs/2605.23744v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Contrast to Detect: Dynamic Graph Contrastive Regularization for Unsupervised Anomaly Detection in Multivariate Time Series



**Source**: [Original Paper](http://arxiv.org/abs/2605.23744v1)
## Abstract
Anomaly detection in multivariate time series (MTS) is hindered by dynamic inter-variable dependencies and feature entanglement under spectral noise, and in practice, is further complicated by the absence of anomaly labels. Existing reconstruction-based detectors tend to recover anomalies as faithfully as normal patterns, while prevailing graph contrastive methods enforce invariance across views and thus assume a stationary relational structure, an assumption that breaks under structural drift in real systems. We propose ContrastAD, an unsupervised framework that turns structural evolution itself into a learning signal rather than suppressing it. A Multi-Perspective Embedder encodes inputs from temporal, attribute, and structural perspectives. A Frequency-Aware Attention Mixer then performs spectral top-K filtering before attention, preventing noise from leaking into query-key similarities. The core component, a Dynamic Graph Contrastive Learner, builds power-law-inspired sparse graph snapshots from batch-level DTW distances and contrasts the most divergent pair against a stable anchor, regularizing the latent space without imposing rigid invariance. Across five real-world benchmarks, ContrastAD attains the highest mean F1 on all five datasets and the highest AUC on three (SWaT 93.60, SMD 98.66, PSM 97.79), with statistically significant F1 and AUC margins over the strongest baseline on SWaT and PSM. On MSL and SMAP, it trails the AUC leader by under 0.7 points while still leading on F1. Ablation and sensitivity studies further confirm that the contrastive objective works best as a soft regularizer, supporting our claim that strict invariance is suboptimal under non-stationary dynamics.

## Metadata
- **Published**: 2026-05-22T15:18:53Z
- **Authors**: Yunhua Pei, Zixing Song, Jin Zheng, John Cartlidge
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23744v1)