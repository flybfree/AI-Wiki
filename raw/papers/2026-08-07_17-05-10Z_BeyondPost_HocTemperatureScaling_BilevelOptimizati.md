---
title: Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration
published: 2026-08-07T17:05:10Z
authors: Ruochen Jin, Zhanliang Wang, Zongyu Dai, Jiancong Xiao, Bojian Hou
url: http://arxiv.org/abs/2608.07419v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration

## Abstract
Preference alignment often makes large language models (LLMs) overconfident and poorly calibrated. Traditional post-hoc temperature scaling is inherently domain-dependent: a temperature fitted on one domain does not generalize across domains. This motivates us to modify model parameters during training to improve calibration. We propose maximizing the entropy of predictive distributions as the calibration objective, which directly targets overconfidence by discouraging overly concentrated predictions. Inspired by temperature scaling, we realize this through a bilevel optimization formulation, where the lower level trains the model under a parametric loss and the upper level selects loss hyperparameters to maximize entropy. To make the framework practical at LLM scale, we adopt an efficient first-order approximation that avoids explicit second-order computation. Across both multiple-choice and open-ended generative question answering, experiments demonstrate that our method yields well-calibrated LLMs with particular advantages in out-of-domain generalization.

## Metadata
- **Published**: 2026-08-07T17:05:10Z
- **Authors**: Ruochen Jin, Zhanliang Wang, Zongyu Dai, Jiancong Xiao, Bojian Hou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07419v1)