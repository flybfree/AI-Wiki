---
title: Learning Compression Rules for Network Traffic
published: 2026-08-05T07:32:05Z
authors: Quentin Lampin, Éloi Sainte-Beuve, Louis-Adrien Dufrène, Guillaume Larue, Massih-Reza Amini
url: http://arxiv.org/abs/2608.04545v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Compression Rules for Network Traffic

## Abstract
We study the problem of learning compact rule-based compressors for structured network traffic. Each packet is a record of header fields that are highly redundant within a flow, and a compressor is a small set of rules matching such records and replacing predictable fields with short codes. We cast rule learning as a two-stage problem: (i) an unsupervised structure-discovery stage that recursively partitions training packets using a normalized entropy-ratio criterion robust to small samples, and (ii) a constrained selection stage that uses dynamic programming to pick the rule subset maximizing expected compression gain under a hard budget on the number of installable rules. We instantiate the framework on Static Context Header Compression (SCHC), the IETF standard for rule-based header compression in constrained networks, and evaluate it on four real-world Internet-of-Things and 5G core-network datasets. Our method, Robust Entropy Clustering for Adaptive comPression (RECAP), surpasses expert-engineered rule sets with a small number of learned rules and removes the need for manual rule design.

## Metadata
- **Published**: 2026-08-05T07:32:05Z
- **Authors**: Quentin Lampin, Éloi Sainte-Beuve, Louis-Adrien Dufrène, Guillaume Larue, Massih-Reza Amini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04545v1)