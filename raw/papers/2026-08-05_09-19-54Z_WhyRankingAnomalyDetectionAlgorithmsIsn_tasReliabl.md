---
title: Why Ranking Anomaly Detection Algorithms Isn't as Reliable as You May Think
published: 2026-08-05T09:19:54Z
authors: Simon Klüttermann, Jérôme Rutinowski, Frederik Polachowski, Alice Kirchheim
url: http://arxiv.org/abs/2608.04613v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Ranking Anomaly Detection Algorithms Isn't as Reliable as You May Think

## Abstract
Anomaly detection is a safety-critical machine learning problem with applications ranging from fraud detection to network intrusion prevention and industrial monitoring. Despite the large number of proposed anomaly detection algorithms, many novel methods claim state-of-the-art performance. However, many authors do so under benchmark settings that are not aligned with one another. This lack of comparability raises concerns regarding the reproducibility and reliability of anomaly detection benchmarks.   In this work, we study the impact of common benchmarking choices on the stability of algorithm rankings. Using seven representative anomaly detection algorithms and 690 datasets from the OddBench benchmark suite, we analyze how rankings change under varying dataset selections, evaluation metrics, hyperparameter configurations, and random seeds. To quantify this effect, we introduce a rank instability metric measuring the variability of algorithm rankings across benchmark settings.   Our results show that algorithm rankings in anomaly detection are highly unstable. In many cases, almost every competitive algorithm can appear as the best-performing method under some benchmark configuration. Among the studied factors, dataset selection and hyperparameter choice contribute most strongly to ranking uncertainty, while random seeds and evaluation metrics have a comparatively limited impact. We also observe that reliable benchmarking requires substantially larger and more diverse dataset collections than the ones commonly used in prior work.

## Metadata
- **Published**: 2026-08-05T09:19:54Z
- **Authors**: Simon Klüttermann, Jérôme Rutinowski, Frederik Polachowski, Alice Kirchheim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04613v1)