---
title: Where Detectors Fail: Closing the Tail-Domain Gap with Expert-Guided Mutual Distillation
url: http://arxiv.org/abs/2607.26555v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_07-27-31Z_WhereDetectorsFail_ClosingtheTail_DomainGapwithExp.md
generated_at: 2026-07-29 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Expert-Guided Mutual Distillation (EGMD) to improve multimodal fake news detection across domains by learning which evidence to trust, addressing domain-specific shortcuts and imbalanced data. Across four datasets in two languages, EGMD achieves state-of-the-art accuracy while reducing domain bias by up to 57.3%. The method operates at input, representation, and decision levels using calibration, expert alignment, and mutual distillation.

## Key Takeaways
- Input-level calibration encodes pair-level coherence as a shared gain before fusion.
- Expert-guided teacher aligns domain statistics and concentrates domain-specific patterns in specialized experts.
- Student prototypes use mutual learning and dual-channel distillation to inherit feature geometry while discouraging local priors.

## Context
Fake news detection systems often suffer from poor generalization due to reliance on unreliable cross-modal evidence, which is exacerbated by data imbalance. This paper addresses that challenge with a multi-stage distillation framework that explicitly models domain trustworthiness.

## Implications
By reducing domain bias and improving robustness across languages, EGMD offers a practical solution for deploying reliable multimodal detectors in real-world settings where data scarcity and heterogeneity are common.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26555v1)
