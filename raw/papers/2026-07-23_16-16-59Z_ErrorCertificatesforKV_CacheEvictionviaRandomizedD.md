---
title: Error Certificates for KV-Cache Eviction via Randomized Design
published: 2026-07-23T16:16:59Z
authors: Peng Xie
url: http://arxiv.org/abs/2607.21475v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Error Certificates for KV-Cache Eviction via Randomized Design

## Abstract
Deterministic KV-cache eviction keeps the top-$k$ tokens under an importance score and deletes the rest. We prove that this design cannot know what it destroyed: evicted values can be altered so that everything the serving system retains is unchanged while the true attention-output error grows arbitrarily, so no serving-time estimator of that error is consistent. Randomized eviction restores identifiability. With a Poisson-sampled tail at known inclusion probabilities, one logit offset performs the Hájek correction inside the softmax, and a survey-sampling variance estimator over the retained set becomes a per-step error certificate with 0.97 empirical coverage at no accuracy cost. On real workloads we pre-registered seven claims and lost three: question-aware eviction at 25--50\% budgets is nearly free; output log-probability predicts failure better than the certificate; certificate-gated budget escalation adds nothing. What survives is attribution: the certificate separates cache-induced from inherent failures (AUC 0.73--0.75, against 0.47--0.54 for output confidence) and schedules recomputation better than random or confidence gating. Randomization buys attribution, not prediction.

## Metadata
- **Published**: 2026-07-23T16:16:59Z
- **Authors**: Peng Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21475v1)