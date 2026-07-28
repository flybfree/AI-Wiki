---
title: Offline-to-Online Creative Optimization with Generative Models and Adaptive Testing
published: 2026-07-26T14:45:15Z
authors: Kevin Lee, Benjamin Letham, Zhiyuan Jerry Lin, Elodie Samson, Eric Onofrey, Poppy Zhang, Shawndra Hill, Eytan Bakshy
url: http://arxiv.org/abs/2607.23696v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Offline-to-Online Creative Optimization with Generative Models and Adaptive Testing

## Abstract
Ad creative optimization is increasingly constrained by evaluation rather than generation. Generative models can produce many plausible creatives, but reliable evaluation requires online experiments, in which only a limited slate can be tested. We study how to use data from historical A/B tests to generate and select the candidates in that slate. We developed and deployed a performance-driven offline-to-online workflow that guides creative generation with a predictive model as an inference-time critic. In the offline phase, we use a predictive model trained on historical experiments to rank and refine variants created by a generative model. A final test slate is then deployed in an online adaptive experiment. In a 50-arm field experiment, we found that the best creative generated with this method yielded 45.1% higher engagement than the best human-authored creative. Two additional experiments showed the same upper-tail pattern, with lifts of 46.7% and 36.2%. We found that despite the predictive model being too noisy to directly identify the best creative offline, it effectively guides the generative model toward creating strong candidates that can be efficiently evaluated in an adaptive experiment. The results suggest a design principle for creative optimization with generative models: use predictive models to guide generation of a slate to test, judge the slate by whether it contains high-performing candidates at a feasible test size, and use adaptive experiments to select among candidates while limiting traffic lost to weak arms.

## Metadata
- **Published**: 2026-07-26T14:45:15Z
- **Authors**: Kevin Lee, Benjamin Letham, Zhiyuan Jerry Lin, Elodie Samson, Eric Onofrey, Poppy Zhang, Shawndra Hill, Eytan Bakshy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23696v1)