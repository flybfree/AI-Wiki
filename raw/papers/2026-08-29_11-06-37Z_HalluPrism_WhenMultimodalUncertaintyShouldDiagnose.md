---
title: HalluPrism: When Multimodal Uncertainty Should Diagnose, Not Decide
published: 2026-08-29T11:06:37Z
authors: Aman Prakash, Sourish Dasgupta, Tanmoy Chakraborty
url: http://arxiv.org/abs/2608.29193v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HalluPrism: When Multimodal Uncertainty Should Diagnose, Not Decide

## Abstract
Multimodal Large Language Models (MLLMs) can assign similar confidence to answers that fail for different reasons. We propose HalluPrism, a behavioral diagnostic that re-runs an answer after visual degradation, blank-image replacement, and grounding or relation checks. These targeted probes yield a signature over visual-perturbation sensitivity (V ), image-removal confidence retention (L), and grounding/relation-probe instability (A). Across 58K+ examples from four benchmarks and four MLLMs, image-removal confidence retention is most prevalent, while grounding/relation-probe instability better separates failure families. Only 18 of 48 source-target checks are diagonally aligned, so the coordinates should be interpreted jointly rather than as independent causal sources. With the dataset fixed, the joint signature improves failure-family AUROC from 0.634 to 0.769 on HallusionBench and from 0.707 to 0.817 on VizWiz, with smaller gains on POPE and VSR. In pooled XGBoost analysis, AUROC rises from 0.78 with scalar confidence to 0.95 with (V, L, A) and 0.97 when confidence is added. The same signature does not automatically improve correctness ranking. The three tested direct scalarizations can harm it. These results separate failure diagnosis from abstention scoring: multimodal uncertainty should characterize failure structure before it is used to decide whether to abstain or correct.

## Metadata
- **Published**: 2026-08-29T11:06:37Z
- **Authors**: Aman Prakash, Sourish Dasgupta, Tanmoy Chakraborty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29193v1)