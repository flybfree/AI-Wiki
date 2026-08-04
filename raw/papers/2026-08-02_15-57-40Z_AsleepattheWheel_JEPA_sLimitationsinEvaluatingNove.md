---
title: Asleep at the Wheel: JEPA's Limitations in Evaluating Novel Driving Data
published: 2026-08-02T15:57:40Z
authors: Advait Pavuluri, Shamik Karkhanis, Uzma Mushtaque
url: http://arxiv.org/abs/2608.01336v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Asleep at the Wheel: JEPA's Limitations in Evaluating Novel Driving Data

## Abstract
Modern autonomous-driving fleets record far more video than human reviewers can inspect. This motivates the need for an automatic clip triage mechanism, to surface rare and review-worthy clips, so that driving models can be fine-tuned to better handle unideal circumstances. We test a label-free approach that scores clips by the prediction-error "novelty" of a self-supervised joint-embedding predictive architecture (JEPA); a frozen V-JEPA video encoder is paired with a lightweight predictor head to reconstruct masked clip embeddings, and clips whose embeddings are hard to predict are flagged as interesting. Evaluated under a realistic protocol that trains on one dataset and tests against footage from others, this approach appears highly effective. We show that this apparent success is actually a domain-shift consequence: on a fair benchmark drawn from a single dataset, this mechanism collapses to chance and is on par with simple no-training baselines. A lightly supervised probe on the same frozen embeddings results in almost double the average precision, indicating that the bottleneck is indeed the self-supervised objective, rather than the representation. We present this as a study for evaluating the effectiveness of self-supervised learning, where cross-dataset protocols can silently reward domain separation over novelty.

## Metadata
- **Published**: 2026-08-02T15:57:40Z
- **Authors**: Advait Pavuluri, Shamik Karkhanis, Uzma Mushtaque
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01336v1)