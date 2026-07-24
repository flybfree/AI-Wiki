---
title: Feature Attribution-Based Explainability Analysis of Deep Learning Models in Predictive Process Monitoring
published: 2026-07-20T10:15:47Z
authors: Kseniya Sahatova, Rafael Seidi Oyamada, Xuefei Lu, Johannes De Smedt
url: http://arxiv.org/abs/2607.17783v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Feature Attribution-Based Explainability Analysis of Deep Learning Models in Predictive Process Monitoring

## Abstract
Predictive process monitoring supports the optimization and control of operational business processes by forecasting the future state or outcome of ongoing cases. While deep neural networks have achieved strong performance for these tasks by modeling sequential dependencies in event logs, their black-box nature limits trust and practical adoption. Feature attribution methods are often used to address this, but applying them directly poses a dilemma: event-level attributions impose high computational complexity for long traces, while explanations based on aggregated trace representations often fail to capture the underlying control-flow dynamics. To address this issue, we propose a local post-hoc explainability method for deep neural networks in outcome prediction. The method relies on a control-flow-aware segmentation algorithm that partitions a trace into meaningful segments and supports the computation of segment-level SHAP explanations. This makes it possible to identify which parts of a trace influence a prediction and which change points steer the case toward the predicted outcome. We assess the proposed segmentation method on a synthetic dataset with known process logic, where meaningful change points can be explicitly verified, and we demonstrate its usefulness on real-world event logs from a loan application process and an administrative process of a Dutch municipality.

## Metadata
- **Published**: 2026-07-20T10:15:47Z
- **Authors**: Kseniya Sahatova, Rafael Seidi Oyamada, Xuefei Lu, Johannes De Smedt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17783v1)