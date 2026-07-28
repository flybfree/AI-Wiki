---
title: Topological Data Analysis and Graph-Theoretic Approaches for Tennis Match Prediction
published: 2026-07-26T07:18:43Z
authors: Jake Schwaderer, Alexander Bastien, Omid Khormali, Alejandro Navarrete, Mia Pesavento, Angelika Elderbrook
url: http://arxiv.org/abs/2607.23509v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Topological Data Analysis and Graph-Theoretic Approaches for Tennis Match Prediction

## Abstract
We present two approaches for predicting tennis match outcomes using topological data analysis and graph theory on ATP singles matches from 2000-2025. The first method applies lower-star filtration to player competitive networks, extracting topological features through persistent homology using four summary methods (VAB, HNAV, HWNAV, OW-HNPV) combined with Modified Band Depth analysis. Algorithmic optimizations including ego graph approximations and triangle elimination enable analysis of about 66k matches. Our Random Forest model achieves 66.2% accuracy (AUC = 0.719) using topological, graph-theoretic, and ranking features. Feature importance analysis reveals that rankings contribute 36.3%, centralities 25.5%, and TDA features 24.0%, with topological features providing complementary signal. When rankings are unavailable, the topology-only model maintains 63.56% accuracy, demonstrating that network-derived features alone capture meaningful competitive structure. The second method uses a modified Katz similarity index with temporal edge weighting, achieving 62.48% accuracy on held-out test data. This work represents the first application of lower-star filtration to tennis prediction, provides systematic comparison of four topological summary methods in sports analytics, and demonstrates that TDA can achieve above-chance prediction using network topology alone while providing additional value when combined with traditional features.

## Metadata
- **Published**: 2026-07-26T07:18:43Z
- **Authors**: Jake Schwaderer, Alexander Bastien, Omid Khormali, Alejandro Navarrete, Mia Pesavento, Angelika Elderbrook
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23509v1)