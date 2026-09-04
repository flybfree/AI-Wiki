---
title: A Two-Stage Forecasting System for CPU Workload Prediction in Private Clouds
published: 2026-09-03T07:15:44Z
authors: Ashir Javeed, Anton Borg, Håkan Grahn, Lars Lundberg, Dhyey Patel, Sogand Shirinbab
url: http://arxiv.org/abs/2609.03457v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Two-Stage Forecasting System for CPU Workload Prediction in Private Clouds

## Abstract
Accurate cloud resource forecasting is essential for proactive resource provisioning, maintaining Quality of Service (QoS), and reducing operational costs in dynamic cloud environments. The existing forecasting approaches predominantly estimate future CPU workload directly from historical resource traces, which often overlook the relationship between customer service demand and subsequent resource consumption. This study proposes a two-stage integrated forecasting model that explicitly models this dependency by first forecasting customer service requests, expressed as Transactions Per Second (TPS), and subsequently estimating future CPU workload from the TPS forecast. Both the forecasting component and resource prediction component employed the XGBoost model within a cascaded learning architecture, complemented by adaptive online retraining using an expanding-window strategy to address concept drift in continuously evolving cloud workloads. The proposed work was evaluated using real-world traces collected from a private cloud environment comprising ten applications. Experimental results demonstrate robust forecasting performance by achieving Symmetric Mean Absolute Percentage Error (SMAPE) below $7\%$ for most applications, with the best-performing application achieving an MAE of $0.7372$, RMSE of $1.1866$, SMAPE of $3.57\%$, and an R2 of $0.9185$. Horizon-wise drift analysis confirmed stable recursive forecasting behavior with controlled error accumulation across a 60-step prediction horizon. Compared with the conventional direct CPU forecasting method, the proposed two-stage integrated model gives improved forecasting robustness, computational efficiency, and interpretability, making it well-suited for proactive resource management and intelligent auto-scaling in cloud computing environments.

## Metadata
- **Published**: 2026-09-03T07:15:44Z
- **Authors**: Ashir Javeed, Anton Borg, Håkan Grahn, Lars Lundberg, Dhyey Patel, Sogand Shirinbab
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03457v1)