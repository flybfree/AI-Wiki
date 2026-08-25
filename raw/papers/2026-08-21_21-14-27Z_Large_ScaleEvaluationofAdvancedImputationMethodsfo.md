---
title: Large-Scale Evaluation of Advanced Imputation Methods for Missing Values in Smart Meter Data
published: 2026-08-21T21:14:27Z
authors: Daniela Stojcheska, Marija Markovska, Dimitar Taskovski, Branislav Gerazov, Boris Nikolov
url: http://arxiv.org/abs/2608.21638v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Large-Scale Evaluation of Advanced Imputation Methods for Missing Values in Smart Meter Data

## Abstract
Accurate and reliable collection of electricity consumption data through Advanced Metering Infrastructure (AMI) is of great importance for the operation of smart grids, especially for the detection of non-technical losses (NTL). However, real-world datasets frequently suffer from missing values due to communication failures. This paper presents an empirical evaluation of three advanced algorithms for large-scale data imputation: the Optimally Weighted Average (OWA) method, Low-Rank Matrix Completion via SoftImpute, and a Shape-Modeling Autoencoder. Existing studies on missing value imputation in electricity consumption data often lack validation on larger datasets. Therefore, the goal of this paper is to validate the selected algorithms on a large-scale real-world electricity consumption dataset from North Macedonia that includes 17,428 commercial smart meters over two years. The robustness of each algorithm is evaluated by simulating continuous gaps in the data ranging from 1 to 168 hours. The results indicate that OWA provides the lowest overall reconstruction error across the evaluated gap sizes and strong stability in worst-case scenarios for gaps of up to one week. In contrast, the autoencoder exhibits higher variance, while SoftImpute has stable but inferior accuracy. These findings suggest that imputation methods should be selected based on the characteristics of load curve data and highlight the potential for hybrid algorithmic architectures in future grid management systems.

## Metadata
- **Published**: 2026-08-21T21:14:27Z
- **Authors**: Daniela Stojcheska, Marija Markovska, Dimitar Taskovski, Branislav Gerazov, Boris Nikolov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21638v1)