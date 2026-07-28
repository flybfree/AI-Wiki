---
title: TopoFE: topology-aware LLM-guided Automated Feature Engineering
published: 2026-07-25T16:45:00Z
authors: Sha Li, Naren Ramakrishnan
url: http://arxiv.org/abs/2607.23286v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TopoFE: topology-aware LLM-guided Automated Feature Engineering

## Abstract
Automatic feature engineering (AutoFE) for tabular learning can be naturally formulated as a program synthesis problem, where the objective is to discover predictive feature transformations from an exponentially large search space. Recent advances in large language models (LLMs) have expanded the expressiveness of AutoFE by enabling feature program generation beyond predefined operator libraries. However, existing LLM-based approaches remain fundamentally limited by stateless generation and homogeneous search: feature proposals are produced from static prompts without accumulating search experience, while single-population exploration quickly converges to dominant transformation patterns and rarely discovers complementary feature compositions across transformation families. We propose TOPOFE, a topology-aware multi-island evolutionary framework for LLM-guided feature engineering. TOPOFE combines family-specialized exploration, adaptive prompt memory, and topology-guided knowledge transfer to efficiently discover diverse and compositional feature programs. Experiments on 29 public tabular datasets demonstrate consistent improvements over state-of-the-art AutoFE methods across classification and regression tasks. Beyond predictive performance, TOPOFE discovers more diverse and transferable feature programs that generalize across multiple downstream predictors and LLM backbones.

## Metadata
- **Published**: 2026-07-25T16:45:00Z
- **Authors**: Sha Li, Naren Ramakrishnan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23286v1)