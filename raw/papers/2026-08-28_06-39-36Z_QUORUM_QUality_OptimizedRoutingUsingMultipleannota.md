---
title: QUORUM: QUality-Optimized Routing Using Multiple annotators
published: 2026-08-28T06:39:36Z
authors: Antonio Purificato, Maria Sofia Bucarelli, Andrea Bacciu, Amin Mantrach, Fabrizio Silvestri
url: http://arxiv.org/abs/2608.27974v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QUORUM: QUality-Optimized Routing Using Multiple annotators

## Abstract
Data annotation remains a central bottleneck in natural language processing, requiring human effort to obtain high-quality labels at scale. While Large Language Models (LLMs) offer a fast and cost-effective alternative, their reliability is highly instance-dependent: they perform well on simple inputs but often fail on examples requiring nuanced reasoning or contextual understanding. In this work, we address this challenge with QUORUM (QUality-Optimized Routing Using Multiple annotators), a budget-aware routing framework that dynamically assigns each instance to human or LLM annotators under a fixed annotation budget. Unlike prior approaches relying on model confidence or uncertainty estimates, QUORUM leverages feature-based signals to estimate instance difficulty and supports multiple annotations per instance, combining them through agreement-based rewards to improve reliability. We evaluate QUORUM across diverse closed- and open-ended annotation tasks in English and multilingual settings, and QUORUM improves annotation quality by up to 34.4% while reducing costs by 8.8% over competing methods. Code can be found at https://github.com/amazon-science/QUORUM.

## Metadata
- **Published**: 2026-08-28T06:39:36Z
- **Authors**: Antonio Purificato, Maria Sofia Bucarelli, Andrea Bacciu, Amin Mantrach, Fabrizio Silvestri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27974v1)