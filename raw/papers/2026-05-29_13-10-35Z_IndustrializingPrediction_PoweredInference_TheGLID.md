---
title: Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation
published: 2026-05-29T13:10:35Z
authors: Grégoire Martinon, Ibrahim Merad, Mohammed Raki
url: http://arxiv.org/abs/2605.31278v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Industrializing Prediction-Powered Inference: The GLIDE Library for Reliable GenAI and Agentic Systems Evaluation

## Abstract
Reliable evaluation of agentic systems requires unbiased estimates with valid uncertainty, but standard practice navigates between costly human annotation and biased LLM-as-judge proxies. Prediction-powered inference (PPI) combines both into debiased estimates with valid confidence intervals, yet its various methods remain scattered across papers under partial implementations. We introduce GLIDE, an open-source Python library that unifies state-of-the-art PPI estimators (PPI++, Stratified PPI, Predict-Then-Debias and its stratified variants, Active Statistical Inference) and samplers (uniform, stratified, active, cost-optimal) under a scipy-style API specialized to mean estimation. GLIDE ships with a reproducible Monte Carlo validation suite, an empirically grounded decision tree for method selection, and an agentic evaluation case study showing substantial annotation savings at equivalent precision. The GLIDE package is available at this URL: https://github.com/EmertonData/glide

## Metadata
- **Published**: 2026-05-29T13:10:35Z
- **Authors**: Grégoire Martinon, Ibrahim Merad, Mohammed Raki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.31278v1)