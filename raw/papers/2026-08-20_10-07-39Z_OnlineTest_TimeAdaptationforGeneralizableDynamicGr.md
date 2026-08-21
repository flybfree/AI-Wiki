---
title: Online Test-Time Adaptation for Generalizable Dynamic Graph Anomaly Detection
published: 2026-08-20T10:07:39Z
authors: Jialun Zheng, Hanchen Yang, Jiannong Cao, Yankai Chen, Yuanjing Feng, Philip S. Yu
url: http://arxiv.org/abs/2608.19858v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Online Test-Time Adaptation for Generalizable Dynamic Graph Anomaly Detection

## Abstract
Generalizable dynamic graph anomaly detection (DGAD) enables pretrained detectors to identify anomalies in unseen target domains without costly retraining. However, existing methods often fail for two reasons. First, they mainly rely on domain-agnostic patterns and miss domain-specific patterns that keep evolving. Second, they assume access to the full target domain data, whereas in more practical online test-time adaptation settings, target data arrive sequentially in unlabeled chunks. To address these limitations, we formulate online test-time adaptation for generalizable DGAD and propose OTTA-DGAD. OTTA-DGAD first extracts dynamic prototypes, i.e., evolving representations of normal and anomalous patterns, from temporal ego-graphs and stores them in a memory buffer. The buffer selectively retains general patterns shared across the source domains used for pretraining while incorporating new patterns from the target domain. An anomaly scorer then compares incoming edge representations against these prototypes to identify both general and domain-specific anomalies. During adaptation, OTTA-DGAD updates the memory buffer using reliable pseudo-labels identified through confidence-based detection. It further enriches each target chunk with relevant representations retained from previous chunks, compensating for information loss resulting from the sequential arrival of data. Extensive experiments under strict test-then-adapt OTTA settings demonstrate state-of-the-art performance on ten real-world datasets from diverse domains.

## Metadata
- **Published**: 2026-08-20T10:07:39Z
- **Authors**: Jialun Zheng, Hanchen Yang, Jiannong Cao, Yankai Chen, Yuanjing Feng, Philip S. Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19858v1)