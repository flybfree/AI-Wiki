---
title: Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models for Edge AI
published: 2026-08-21T14:41:54Z
authors: Shiva Shrestha, Kazi Shaharair Sharif, Zongxing Xie, Jiajing Huang, Anhao Xiang, Honghui Xu
url: http://arxiv.org/abs/2608.21172v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models for Edge AI

## Abstract
Federated fine-tuning enables large language models to adapt on edge devices without centralizing private data, but practical deployments must address hardware instability and adversarial update corruption together. Thermally constrained clients may throttle, slow local training, or delay synchronous aggregation, while Byzantine clients and communication-layer adversaries can corrupt the updates used to form the global model. To address these challenges, we present Thermo-FL, a thermal-aware federated LoRA fine-tuning framework that uses device temperature as an active control signal for local adapter training and sparse update transmission. On the client side, Thermo-FL adjusts the active LoRA-layer fraction and transmitted update density as devices heat or cool, reducing workload under thermal stress. On the server side, Thermo-FL introduces TERRA, a robust aggregation pipeline for dynamically sparse LoRA updates that combines norm filtering, mask-aware directional validation, adaptive active-coordinate clipping, and mask-aware aggregation. We evaluate Thermo-FL using both a large-scale emulator and a Jetson-based physical testbed. In the emulator, Thermo-FL improves robustness under adversarial sparse aggregation and achieves the strongest BoolQ accuracy across clean and attack settings while remaining competitive on GSM8K. In the physical prototype, Thermo-FL stabilizes device temperature, reduces compressed upload size through bitmap sparse encoding, and preserves GSM8K utility under sign-flip/scale and MITM perturbations. These results show that secure edge LLM adaptation should jointly consider hardware behavior, workload regulation, sparse communication, and aggregation robustness.

## Metadata
- **Published**: 2026-08-21T14:41:54Z
- **Authors**: Shiva Shrestha, Kazi Shaharair Sharif, Zongxing Xie, Jiajing Huang, Anhao Xiang, Honghui Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21172v1)