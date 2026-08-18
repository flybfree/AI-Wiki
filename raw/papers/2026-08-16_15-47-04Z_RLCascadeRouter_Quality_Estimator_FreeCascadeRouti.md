---
title: RLCascadeRouter: Quality-Estimator-Free Cascade Routing via Reinforcement Learning
published: 2026-08-16T15:47:04Z
authors: Shihong Huang, Shengjie Wang, Hong Ma, Zhou Xu
url: http://arxiv.org/abs/2608.15817v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RLCascadeRouter: Quality-Estimator-Free Cascade Routing via Reinforcement Learning

## Abstract
The growing ecosystem of large language models (LLMs) offers huge potential to optimize performance-cost trade-offs. However, their heterogeneous capabilities and inference costs make efficiently routing queries a significant challenge. Existing paradigms are inflexible: one-shot routers commit before observing responses, whereas conventional cascades stop adaptively but follow a fixed model order. Cascade routing removes both restrictions by reconsidering whether to stop or invoke another model after each response. Current methods use a predict-then-optimize pipeline estimating response quality and future model utility. However, prediction loss for quality or utility is not equivalent to routing-decision loss. A lower prediction error does not necessarily yield a better action; a small boundary-crossing error can reverse a ``stop'' or model-selection decision. Therefore, we propose RLCascadeRouter, a quality-estimator-free framework that formulates cascade routing as a Markov decision process with actions comprising ``stop'' and model selection. It uses trajectory returns and advantages to directly optimize the performance-cost objective. Its Cascade Policy Network models candidate complementarity for model selection and remaining-action value for stopping, eliminating independent post-hoc response-quality estimators. Evaluated across ten LLMRouterBench benchmarks with thirteen LLMs, RLCascadeRouter outperforms strong baselines and achieves superior performance-cost trade-offs. It incorporates unseen models without retraining, and ablation studies validate both policy components.

## Metadata
- **Published**: 2026-08-16T15:47:04Z
- **Authors**: Shihong Huang, Shengjie Wang, Hong Ma, Zhou Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15817v1)