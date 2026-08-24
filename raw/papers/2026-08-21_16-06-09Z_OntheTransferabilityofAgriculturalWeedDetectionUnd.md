---
title: On the Transferability of Agricultural Weed Detection Under Cross-Field Distribution Shift
published: 2026-08-21T16:06:09Z
authors: Nikhilesh Prabhakar, Pranuthi Tenali, Wilfredo Abudeye Fernandez, Shekhar Borah, Athresh Karanam, Erik Blasch, Prabha Sundaravadivel, Sriraam Natarajan
url: http://arxiv.org/abs/2608.21254v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Transferability of Agricultural Weed Detection Under Cross-Field Distribution Shift

## Abstract
Accurate agricultural weed detection in real-world field conditions is essential for precision agriculture, enabling targeted intervention and reducing yield loss. Recent work has reported strong detection performance from UAV-based imagery across a range of crops, yet existing approaches evaluate within a single crop and field, leaving practitioners with little evidence that a model trained on one crop will generalize to a new field or crop type. In this work, we characterize where cross-dataset weed-localization performance degrades and which modeling choices recover it, reducing the need to relabel every new deployment field. We introduce a newly collected and annotated UAV image dataset for agricultural weed detection in cotton fields and use it alongside an existing soybean dataset collected under a similar protocol. Using these datasets, we evaluate the performance of several strategies for transferring a detector trained on one crop to another, comparing unsupervised domain adaptive object detection (DAOD) against pretraining on a domain-adjacent source dataset followed by few-shot fine-tuning on the target dataset. Our analysis spans target-domain label budgets from zero to the full target dataset, characterizing the trade-off between adaptation strategy and annotation effort. We find that few-shot fine-tuning with as few as 25 labeled target examples outperforms unsupervised DAOD in our cross-crop comparison, suggesting that source domain selection combined with modest target supervision is more productive than algorithmic sophistication in adaptation.

## Metadata
- **Published**: 2026-08-21T16:06:09Z
- **Authors**: Nikhilesh Prabhakar, Pranuthi Tenali, Wilfredo Abudeye Fernandez, Shekhar Borah, Athresh Karanam, Erik Blasch, Prabha Sundaravadivel, Sriraam Natarajan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21254v1)