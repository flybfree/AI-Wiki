---
title: A Real-Time Tsetlin Machine-based Non-intrusive Load Monitoring System on MCUs
published: 2026-08-19T10:35:14Z
authors: Tianhang Tan, Han Wu, Tousif Rahman, Shengyu Duan, Alex Yakovlev, Rishad Shafik
url: http://arxiv.org/abs/2608.18780v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Real-Time Tsetlin Machine-based Non-intrusive Load Monitoring System on MCUs

## Abstract
Non-Intrusive Load Monitoring (NILM) systems estimate individual appliance energy consumption from a single aggregate meter, without requiring separate sensors for each device. By installing a single meter that measures a building's total electricity consumption, NILM algorithms can determine the active status of each appliance. However, traditional NILM systems use computationally intensive optimization algorithms to process offline data, limiting their capability for on-device deployment, where sensitive household data must be processed locally. This paper proposes a Tsetlin Machine (TM)-based NILM framework, targeting real-time applications on resource-constrained microcontrollers (MCUs), enabling privacy-preserving edge deployment. The problem is reformulated as a classification task, and the proposed approach achieves an average precision of 90% and recall of 96% for two-appliance classification, and 77% precision and 80% recall for four appliances on the REDD dataset. The trained model occupies only 18 KB of flash memory and achieves an inference latency of 0.43 ms on an ESP32, demonstrating its suitability for embedded NILM applications on MCUs.

## Metadata
- **Published**: 2026-08-19T10:35:14Z
- **Authors**: Tianhang Tan, Han Wu, Tousif Rahman, Shengyu Duan, Alex Yakovlev, Rishad Shafik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18780v1)