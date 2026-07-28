---
title: Extending Desbordante with Probabilistic Functional Dependency Discovery Support
published: 2026-07-26T13:01:48Z
authors: Ilia Barutkin, Maxim Fofanov, Sergey Belokonny, Vladislav Makeev, George Chernishev
url: http://arxiv.org/abs/2607.23636v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Extending Desbordante with Probabilistic Functional Dependency Discovery Support

## Abstract
Data profiling aims to extract complex patterns from data for further analysis and use that data in domains such as data cleaning, data deduplication, anomaly detection, and many more.   Functional dependencies (FDs) are one of the most well-known patterns. However, they are poorly suited for these tasks, as real data is usually dirty, and the rigid definition of FDs does not allow algorithms to locate them. For this reason, there are several formulations aimed at relaxing FDs to support dirty data, with approximate functional dependency (AFD) being the most popular one. Another formulation is the Probabilistic Functional Dependency (pFD), which we aim to support inside Desbordante - a science-intensive, high-performance and open-source data profiling tool implemented in C++. However, pFDs are relatively poorly studied, compared to AFDs.   In this paper we study pFDs, both analytically and empirically. We start by assessing how different pFDs and AFDs are by studying cases in which pFDs have an edge over AFDs. Then, we implement the algorithm for pFD discovery, as well as study its run time and memory consumption. We also compare it with an AFD discovery algorithm. Lastly, we study the output of both algorithms to learn whether or not it is possible to use AFD discovery algorithm to get pFDs and vice versa.

## Metadata
- **Published**: 2026-07-26T13:01:48Z
- **Authors**: Ilia Barutkin, Maxim Fofanov, Sergey Belokonny, Vladislav Makeev, George Chernishev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23636v1)