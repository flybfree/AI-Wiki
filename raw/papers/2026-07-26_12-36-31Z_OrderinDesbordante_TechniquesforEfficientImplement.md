---
title: Order in Desbordante: Techniques for Efficient Implementation of Order Dependency Discovery Algorithms
published: 2026-07-26T12:36:31Z
authors: Yakov Kuzin, Dmitriy Shcheka, Michael Polyntsov, Kirill Stupakov, Mikhail Firsov, George Chernishev
url: http://arxiv.org/abs/2607.23632v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Order in Desbordante: Techniques for Efficient Implementation of Order Dependency Discovery Algorithms

## Abstract
Science-intensive data profiling focuses on discovery and validation of various patterns in datasets. This study considers discovery of one such pattern - order dependency (OD). Simply put, OD states that some list of columns is ordered according to another one. It is of use for database query optimization, data cleaning and deduplication, anomaly detection, and much more.   Existing discovery methods have approached this problem solely from the algorithmic standpoint, without focusing on the implementation side. At the same time, this problem is very computationally intensive, and therefore this part should not be ignored, as it brings ODs closer to industrial use.   In this paper, we study two algorithms for OD discovery which target different OD axiomatizations - FASTOD and ORDER. We start by reimplementing these algorithms in C++ in order to speed them up and lower their memory consumption. We then analyze their bottlenecks and propose several techniques which improve their performance even further.   To perform evaluation, we have implemented these algorithms inside Desbordante - a science-intensive, high-performance, and open-source data profiling tool developed in C++. Experiments have demonstrated a performance improvement of up to 3x obtained by reimplemented versions, and, with the application of our techniques, up to 10x. Memory consumption has been lowered by up to 2.9x.

## Metadata
- **Published**: 2026-07-26T12:36:31Z
- **Authors**: Yakov Kuzin, Dmitriy Shcheka, Michael Polyntsov, Kirill Stupakov, Mikhail Firsov, George Chernishev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23632v1)