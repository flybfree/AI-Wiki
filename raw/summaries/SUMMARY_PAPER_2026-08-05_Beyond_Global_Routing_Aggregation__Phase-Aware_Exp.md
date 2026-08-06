---
title: Beyond Global Routing Aggregation: Phase-Aware Expert Merging for MoE Vision-Language Models
url: http://arxiv.org/abs/2608.04454v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_05-09-20Z_BeyondGlobalRoutingAggregation_Phase_AwareExpertMe.md
generated_at: 2026-08-05 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RoleMerge, a training‑free expert merging method for MoE vision‑language models that preserves phase‑conditioned expert roles instead of relying on global routing statistics. By constructing phase‑normalized Routing Role Profiles (RRPs) and merging experts with compatible profiles, the approach maintains answer‑decoding distinctions while reducing storage burden. Experiments show up to a 9.6 percent relative improvement in macro‑average performance compared with alternative merging strategies at matched expert retention ratios.

## Key Takeaways
- Phase‑conditioned expert roles are preserved during merging, preventing experts serving different phases from appearing interchangeable.
- The method uses phase‑normalized routing statistics to build Routing Role Profiles that capture each expert’s relative preference for image‑context, question, and answer tokens.
- RoleMerge yields higher macro‑average performance across three models on multiple benchmarks than methods based solely on global routing aggregation.

## Context
MoE vision‑language models aim to combine large capacity with efficient deployment by activating a sparse pool of experts. Traditional merging techniques aggregate all token routing signals globally, which can mask the distinct responsibilities of different phases in phase‑structured inference pipelines. This paper addresses that limitation by recognizing that expert roles are inherently tied to specific phases and should be respected during merging.

## Implications
For researchers developing MoE models, this work highlights the importance of modeling task structure rather than treating all tokens uniformly. Practitioners can adopt RoleMerge to reduce model size while preserving performance, leading to more scalable deployments in vision‑language applications such as image captioning and question answering systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04454v1)
