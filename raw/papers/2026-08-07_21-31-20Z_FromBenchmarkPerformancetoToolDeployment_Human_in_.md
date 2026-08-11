---
title: From Benchmark Performance to Tool Deployment: Human-in-the-Loop Anomaly Detection
published: 2026-08-07T21:31:20Z
authors: Mike Szklarzewski, CJ George, Gavin Smithson, Christopher Stokes, Dakota Fulp, William M. Jones, Benjamin Wynn, Alexander Ur, Agit Yesiloz, Clint Kallenbach, Mark Swartz, Nathan DeBardeleben, Sharmistha Chakrabarti
url: http://arxiv.org/abs/2608.07770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Benchmark Performance to Tool Deployment: Human-in-the-Loop Anomaly Detection

## Abstract
Automated anomaly detection methods often report strong performance on curated academic benchmarks, but their behavior under real-world industrial conditions is less clear. In this work, we evaluate 19 unsupervised anomaly detection models on the BowTie dataset, a challenging manufacturing dataset with reflective surfaces, subtle defects, and profile-specific variation. In contrast to benchmark results, we observe that model performance is less stable than typically reported on standard benchmarks such as MVTec AD, highly sensitive to preprocessing, and inconsistent across conditions, with no single approach emerging as uniformly robust; a consensus audit further indicates that nominal-data quality affects deployment.   Motivated by these findings, we developed and initially deployed a unified human-in-the-loop framework for manufactured-part inspection that combines image annotation, AI-assisted defect detection, and an integrated validation engine, replacing a prior manual visual inspection and documentation workflow. The system supports heatmap-guided defect review, SAM-refined candidate regions for inspector acceptance, rejection, or boundary adjustment, mask evaluation where annotations exist, and review history for inspector consistency and onboarding. Together, the results highlight the gap between benchmark performance and deployment reality, and provide a practical framework for addressing it.

## Metadata
- **Published**: 2026-08-07T21:31:20Z
- **Authors**: Mike Szklarzewski, CJ George, Gavin Smithson, Christopher Stokes, Dakota Fulp, William M. Jones, Benjamin Wynn, Alexander Ur, Agit Yesiloz, Clint Kallenbach, Mark Swartz, Nathan DeBardeleben, Sharmistha Chakrabarti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07770v1)