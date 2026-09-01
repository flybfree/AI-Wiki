---
title: Generative multi-domain transfer learning for fault detection in data-scarce wind turbines
published: 2026-08-31T06:40:03Z
authors: Stefan Jonas, Angela Meyer
url: http://arxiv.org/abs/2608.30323v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generative multi-domain transfer learning for fault detection in data-scarce wind turbines

## Abstract
Normal behavior models have shown promise for reliable fault detection in wind turbines. However, these unsupervised anomaly detection models require sufficient fault-free training data to learn the normal operation behavior of turbines. Under data scarcity, for example in newly deployed wind turbines, these models may result in poor fault detection performance. In this work, we propose a multi-domain generative domain mapping approach based on Star Generative Adversarial Networks (StarGAN) to improve fault detection on data-scarce wind turbines. Our model maps SCADA measurements from a data-scarce turbine to resemble those of several data-rich turbines. By preserving the operational state during translation, faults occurring in a data-scarce domain can be mapped and detected by reliable pre-trained normal behavior models of data-rich domains. Highlighting the benefits of an ensemble fusion strategy, we show that under severe data scarcity our method can produce anomaly scores comparable to models trained on large representative datasets. Our approach can consistently outperform models trained on scarce data when less than 2 weeks of training data are available. With just 2 weeks of accumulated training data, we achieve an anomaly score similarity that is, on average, +16% higher than conventional fine-tuning, and +10% higher than single-source domain mapping. As a step towards unsupervised model selection, we propose a proxy metric that detects poor performance at training time, despite an absence of anomalies. Our study presents the potential and challenges of multi-domain mapping for wind turbine fault detection under unrepresentative training data.

## Metadata
- **Published**: 2026-08-31T06:40:03Z
- **Authors**: Stefan Jonas, Angela Meyer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30323v1)