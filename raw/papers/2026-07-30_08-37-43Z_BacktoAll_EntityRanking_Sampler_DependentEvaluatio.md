---
title: Back to All-Entity Ranking: Sampler-Dependent Evaluation in Continuous-Time Dynamic Graphs
published: 2026-07-30T08:37:43Z
authors: Minwoo Yu, Young-guk Ha
url: http://arxiv.org/abs/2607.27861v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Back to All-Entity Ranking: Sampler-Dependent Evaluation in Continuous-Time Dynamic Graphs

## Abstract
Next-destination prediction in continuous-time dynamic graphs (CTDGs) commonly ranks an observed interaction against sampled negative destinations. The resulting score is conditional on both the negative distribution and the number of candidates chosen by the researcher. We show that a non-uniform negative distribution changes the Bayes-optimal ranking, while even a finite candidate set drawn uniformly can destabilize model rankings and measured module effects.   Time-varying source-destination history membership and model operations that use this information directly transmit the sampler's influence to the evaluation score. We examine this mechanism using a factorial evaluation of repeated and new positives against seen and unseen negatives, a minimal scorer based solely on pair-history membership, and controlled representation interventions. Across six models on LastFM, MOOC, Reddit, and Wikipedia, at least one model pair changes relative order between the expected Uniform-20 metric and the full catalog on three of the four datasets. The measured effect of the same module also changes in magnitude and direction with the candidate-set size and training objective.   These results establish that model-superiority and ablation conclusions from sampled-negative benchmarks are conditional on the stated candidate configuration. All-entity ranking evaluates every destination in a fixed catalog, eliminating negative-selection freedom and sampling variation while retaining the original CTDG scorer. We therefore recommend all-entity ranking as the primary evidence for architecture comparisons on CTDG benchmarks with an enumerable, fixed destination catalog.

## Metadata
- **Published**: 2026-07-30T08:37:43Z
- **Authors**: Minwoo Yu, Young-guk Ha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27861v1)