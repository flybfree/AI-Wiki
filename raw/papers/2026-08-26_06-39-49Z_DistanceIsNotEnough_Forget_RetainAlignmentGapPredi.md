---
title: Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness
published: 2026-08-26T06:39:49Z
authors: Yi Chen, Hanna Hsieh, Shuhong Liu, Chuanbo Hua, Zihan Ma, Kun Wang, Joo-Young Kim
url: http://arxiv.org/abs/2608.25429v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness

## Abstract
Machine unlearning aims to make a model forget specific data, yet unlearned LLMs often fail to stay unlearned: brief fine-tuning can revive removed knowledge. Existing robustness predictors rely on global weight-space displacement, but distance alone can be misleading when random or destructive updates collapse performance. We argue that relearning robustness depends on update structure: robust unlearning should affect forget-critical weights while sparing retain-critical ones. We introduce the Forget-Retain Alignment Gap (FRAG), a training-free predictor that scores an update's forget-retain alignment without running a relearning attack, and separates selective from dense updates more reliably than global distance. Building on the forget-critical, retain-sparing principle, Forget-Retain Pruning (FRP) improves relearning robustness. Our results suggest that weight selectivity better explains robustness than distance alone. Code is available at https://github.com/Yi1-Chen/FRAG.

## Metadata
- **Published**: 2026-08-26T06:39:49Z
- **Authors**: Yi Chen, Hanna Hsieh, Shuhong Liu, Chuanbo Hua, Zihan Ma, Kun Wang, Joo-Young Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25429v1)