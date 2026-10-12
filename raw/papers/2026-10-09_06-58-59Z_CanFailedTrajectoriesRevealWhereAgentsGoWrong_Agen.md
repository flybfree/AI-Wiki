---
title: Can Failed Trajectories Reveal Where Agents Go Wrong? Agentic Failure Attribution Without Step-Level Labels
published: 2026-10-09T06:58:59Z
authors: Do Nguyen-Thanh, Junlin Fang, Bing Li, Zhen Fang, Sean Du
url: http://arxiv.org/abs/2610.13105v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Failed Trajectories Reveal Where Agents Go Wrong? Agentic Failure Attribution Without Step-Level Labels

## Abstract
Failure attribution for LLM agents aims to identify decisive steps responsible for task failure, which is critical for debugging and improving agentic systems. Existing methods rely on costly LLM prompting, step-level error annotations, or verified successful trajectories that lack failure signals for assistance. In this paper, we study failure attribution from step-unlabeled failure trajectories, where each trajectory is known to have failed but its decisive step is unknown. We propose SOAP (Spectral scOring with Attention-guided Propagation), an effective framework requiring neither step-level training labels nor a separate success-only reference set. SOAP first constructs a spectral reference space from LLM representations and assigns each step a base error score according to its projection behavior. Importantly, later steps may exhibit stronger failure signals because they inherit an earlier mistake, causing independent scorers to favor downstream consequences over the decisive error. To address this downstream contamination, SOAP derives soft step dependencies from attention patterns and propagates downstream error evidence toward its likely upstream sources. Extensive experiments show that SOAP consistently improves attribution performance over competitive baselines.

## Metadata
- **Published**: 2026-10-09T06:58:59Z
- **Authors**: Do Nguyen-Thanh, Junlin Fang, Bing Li, Zhen Fang, Sean Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13105v1)