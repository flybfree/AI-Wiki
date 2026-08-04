---
title: A Multi-Objective AutoML-based Efficient Intrusion Detection System for EV Charging Networks
published: 2026-08-03T14:11:38Z
authors: Li Yang
url: http://arxiv.org/abs/2608.02274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Multi-Objective AutoML-based Efficient Intrusion Detection System for EV Charging Networks

## Abstract
Electric Vehicle Charging Systems (EVCSs) are increasingly connected with Internet of Things (IoT) devices, which improves charging intelligence but also expands their exposure to cyber-attacks. Intrusion Detection Systems (IDSs) are essential for securing EV charging networks; however, conventional Machine Learning (ML)-based IDSs often rely on manual model design and mainly optimize detection performance without fully considering inference latency and model size. In this paper, a Multi-Objective Automated ML (MOO-AutoML)-based efficient IDS is proposed for EVCS security. The proposed framework uses a lightweight training strategy and a LightGBM-based automated feature selection method to select compact feature subsets based on accumulated feature importance. Then, Non-dominated Sorting Genetic Algorithm III (NSGA-III) jointly optimizes the feature selection threshold and key LightGBM hyperparameters under three objectives: maximizing weighted F1-score, minimizing 99th percentile inference latency ratio, and minimizing model size ratio. Experiments on CICEVSE2024 and CICIDS2017 show that the proposed MOO-AutoML IDS achieves competitive weighted F1-scores, lower P99 inference latency, and smaller model sizes than the compared methods. Overall, the results indicate that the proposed method can support accurate and efficient intrusion detection for EVCS and IoT security under practical deployment constraints.

## Metadata
- **Published**: 2026-08-03T14:11:38Z
- **Authors**: Li Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02274v1)