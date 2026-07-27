---
title: General Value Functions for Remaining Useful Life and Failure-Mode Prediction
published: 2026-07-24T13:04:32Z
authors: Hao Yan, Ali Sarabi, Qing Zou, Boyang Xu
url: http://arxiv.org/abs/2607.22268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# General Value Functions for Remaining Useful Life and Failure-Mode Prediction

## Abstract
Remaining useful life (RUL) prediction and failure-mode classification are central tasks in predictive maintenance. Many data-driven pipelines use fixed-window supervised learning with complete terminal labels; such routes do not naturally encode the temporal recursion linking successive degradation-state predictions when observations are partial or unit identities are unavailable. We formulate prognostics as vector General Value Function (GVF) prediction on an absorbing degradation process, treating RUL and failure-mode probabilities as temporally consistent targets rather than independent window-level labels, and estimate them with a multi-step temporal-difference estimator, TD($n,λ$). Supporting theory identifies the Bellman fixed point of the vector GVFs, characterizes the linear projected-TD limit and its relation to complete-return Monte Carlo regression under realizability, and explains when bootstrapped TD targets are less variable than Monte Carlo returns. On an event-triggered multimode simulation and NASA C-MAPSS label-scarce stitch data, TD improves RUL and failure-mode prediction relative to a supervised same-backbone Monte Carlo control, especially under scarce complete labels. Practically, fragmented, identity-free degradation records can contribute local Bellman transitions instead of being discarded until complete run-to-failure labels are available.

## Metadata
- **Published**: 2026-07-24T13:04:32Z
- **Authors**: Hao Yan, Ali Sarabi, Qing Zou, Boyang Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22268v1)