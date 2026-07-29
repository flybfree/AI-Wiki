---
title: Robust Unsupervised Network Intrusion Detection via Federated Learning with Selective Aggregation under Anomalous Sample Contamination
published: 2026-07-28T08:32:41Z
authors: Shohei Kamiguchi, Takayuki Nishio
url: http://arxiv.org/abs/2607.25439v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Unsupervised Network Intrusion Detection via Federated Learning with Selective Aggregation under Anomalous Sample Contamination

## Abstract
Network intrusion detection systems (NIDS) have become essential for Internet of Things (IoT) environments, as malware targeting IoT devices continues to evolve in sophistication. Unsupervised learning approaches offer a promising direction by removing the dependency on labeled datasets. However, the common assumption that training data are entirely clean is often violated in practice, particularly when data samples are collected directly from deployed network devices, where anomalies are likely to be present in the training datasets. Such contamination degrades detection performance and highlights the need for robust unsupervised NIDS methods capable of operating effectively under contaminated unlabeled training data.   To address this issue, we propose a robust training methodology for anomaly detection (AD) that remains effective even in the presence of unlabeled anomalies. Our method consists of two primary components. First, we exploit a known limitation of federated learning (FL), namely its tendency to underrepresent minority data. By leveraging this characteristic, we attenuate the influence of anomalous data originating from a small number of compromised clients. Second, we introduce a selective aggregation mechanism during model aggregation, which quantifies the "distance" between local client models and a global reference. Specifically, we employ the Expectation-Maximization (EM) algorithm to detect and exclude client groups whose model updates significantly diverge from the majority. This selective aggregation ensures that anomalous updates do not compromise the global model.   Experiments conducted on multiple NIDS datasets demonstrate that our method outperforms existing approaches in environments contaminated with anomalous data. Furthermore, the proposed method maintains its detection performance even as the proportion of anomalies increases.

## Metadata
- **Published**: 2026-07-28T08:32:41Z
- **Authors**: Shohei Kamiguchi, Takayuki Nishio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25439v1)