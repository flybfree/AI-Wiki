---
title: Maintaining IoT Device Identification under Concept Drift via Budget-Aware Traffic Labeling
published: 2026-08-16T01:19:00Z
authors: Shayan Azizi, Norihiro Okui, Masataka Nakahara, Ayumu Kubota, Gustavo Batista, Hassan Habibi Gharakaheili
url: http://arxiv.org/abs/2608.15465v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Maintaining IoT Device Identification under Concept Drift via Budget-Aware Traffic Labeling

## Abstract
Identification of IoT device types from passive traffic is increasingly used for security management in enterprise and ISP networks. However, the performance of machine learning-based classifiers gradually degrades under concept drift as device behavior evolves. Therefore, maintaining classification performance requires periodic retraining with newly labeled deployment traffic. The operational challenge is determining how much and which deployment traffic instances to label for maintaining classification performance. We show that these two decisions should be treated separately. While retraining solely on instances selected by a drift detector is prone to systematically overlooking parts of the emerging behavioral space, uniformly sampled deployment traffic captures more representative behavioral changes. Instead, drift detection is more effective at determining the amount of deployment traffic that should be labeled. We make three contributions. (1) We conduct a two-year longitudinal study of IoT traffic and characterize how behavioral evolution manifests across device classes and how retraining with newly labeled traffic restores classification performance. (2) We develop a conformity-based drift detector that captures class-conditional behavioral models directly from raw traffic features and provides feature-level explanations of behavioral evolution. (3) We demonstrate that adjusting the traffic labeling rate according to the observed behavioral evolution, combined with uniform traffic sampling, maintains classifier performance more effectively than detector-guided sample selection and is beneficial to managing the traffic labeling effort. We further show that this strategy performs comparably to confidence-guided adaptation while providing feature-level explanations. Our evaluation uses 3.8 million IPFIX flow records collected from 21 IoT types over more than 2 years.

## Metadata
- **Published**: 2026-08-16T01:19:00Z
- **Authors**: Shayan Azizi, Norihiro Okui, Masataka Nakahara, Ayumu Kubota, Gustavo Batista, Hassan Habibi Gharakaheili
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15465v1)