---
title: Spatiotemporal Proximal Causal Inference under Hidden Confounding and Interference
published: 2026-08-02T16:13:21Z
authors: Omar Faruque, Pavan Raj Ravi, Jianwu Wang
url: http://arxiv.org/abs/2608.01352v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spatiotemporal Proximal Causal Inference under Hidden Confounding and Interference

## Abstract
Estimating causal effects from real-world spatiotemporal data is challenging due to hidden confounders and interference. Standard causal identification methods assume conditional exchangeability given observed covariates, which fails whenever hidden confounders affect both treatment and outcomes - a common setting in domains such as climate, environmental policy, epidemiology, and regional economics. In this paper, we propose a novel spatiotemporal proximal causal inference framework that extends proximal identification theory to spatiotemporal settings. The proposed method jointly captures local and neighborhood-level confounding information by introducing treatment- and outcome-inducing proxies, and we derive a spatiotemporal outcome confounding bridge function that identifies the potential outcome without requiring direct recovery of the hidden confounder. We establish the identifiability of this bridge function under proxy exclusion restrictions and a spatiotemporal completeness condition, and show that the resulting estimator recovers the outcome through a proximal generalization of the g-computation formula. To operationalize this identification result, we propose a neural architecture that learns proxies via transformer-based spatiotemporal encoders - coupled with a conditional mutual information critic to enforce exclusion restrictions and a moment-matching network to guarantee that the learned bridge function satisfies the underlying identifying equation. We further introduce a stabilized weighting scheme to address treatment support imbalance. Experiments on synthetic datasets demonstrate that our approach achieves comparable performance to baseline causal inference methods, while providing, to our knowledge, the first theoretically grounded outcomes for the hidden confounding in the presence of spatiotemporal interference through a proximal causal inference framework.

## Metadata
- **Published**: 2026-08-02T16:13:21Z
- **Authors**: Omar Faruque, Pavan Raj Ravi, Jianwu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01352v1)