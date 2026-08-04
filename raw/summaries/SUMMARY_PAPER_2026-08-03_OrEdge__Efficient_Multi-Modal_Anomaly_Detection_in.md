---
title: OrEdge: Efficient Multi-Modal Anomaly Detection in Distributed Software Systems via Orthogonal-Domain Learning
url: http://arxiv.org/abs/2608.00309v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_21-42-50Z_OrEdge_EfficientMulti_ModalAnomalyDetectioninDistr.md
generated_at: 2026-08-03 23:45
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents OrEdge, a lightweight framework for real-time anomaly detection in distributed software systems that uses orthogonal-domain temporal representations instead of heavy attention or graph models. It jointly processes logs, metrics and traces to detect abnormal behavior while keeping model size low. Experiments on three microservice datasets show it matches detection performance with up to 9.6K parameters versus 20K–143K elsewhere.

## Key Takeaways
- OrEdge replaces attention‑based or graph‑based models with an orthogonal‑domain reconstruction module that captures recurring patterns and suppresses transient noise, enabling compact representation.
- The framework jointly analyzes heterogeneous monitoring data (logs, metrics, traces) to reduce redundancy and improve temporal dependency modeling.
- On edge hardware such as Raspberry Pi, OrEdge runs sub‑second inference, cutting latency by over an order of magnitude compared with existing approaches.

## Context
Current anomaly detection systems rely on computationally expensive attention mechanisms or graph neural networks that require large models and high latency, limiting deployment to cloud environments. Edge devices need real‑time, low‑resource solutions without sacrificing accuracy. This work addresses the gap by offering a model that is both accurate and resource‑efficient.

## Implications
For industry practitioners, OrEdge enables scalable anomaly detection on edge microservices, reducing infrastructure costs and improving response times. Practitioners can adopt this compact architecture to meet real‑time requirements while maintaining high detection fidelity across distributed systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00309v1)
