---
title: proxymate: Diagnosis and Adjustment of Proxy Estimates for Reliable Inference
published: 2026-07-27T13:19:03Z
authors: Alexandra N. M. Darmon, Deeksha Sinha, Steve Wilkins-Reeves, Caner Gocmen
url: http://arxiv.org/abs/2607.24401v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# proxymate: Diagnosis and Adjustment of Proxy Estimates for Reliable Inference

## Abstract
Proxy outcomes (such as short-term behavioral signals, model predictions, or surrogate endpoints) are frequently used in place of primary outcomes that are too slow to mature, rare, or challenging to measure directly. But valid inference on a proxy does not guarantee valid inference on the primary estimate as proxy-based estimates can be systematically biased in ways that are difficult to predict, leading to improperly calibrated confidence intervals.   We present proxymate, a framework and open-source Python package for proxy validation and adjustment. proxymate organizes into four levels: The Representativity Level (population validity), the Unit Level (measurement quality), the Estimate Level (decision validity), and the Domain Level (cross-domain transportability). Within each level, proxymate provides diagnostic checks, and targeted adjustment strategies that map specific failures to appropriate corrections.   At Meta, proxymate has been adopted by many different use cases, spanning experimentation, prevalence estimation, and monitoring use cases, all facing different proxy challenges (limited human review time, long maturation window of outcomes, low detectability) and showcasing the modularity of the framework. Across all products, proxymate assessed and corrected millions of proxy, primary unit comparisons. It has facilitated launches across multiple work streams including enabling quick decision making on thousands of experiments.

## Metadata
- **Published**: 2026-07-27T13:19:03Z
- **Authors**: Alexandra N. M. Darmon, Deeksha Sinha, Steve Wilkins-Reeves, Caner Gocmen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24401v1)