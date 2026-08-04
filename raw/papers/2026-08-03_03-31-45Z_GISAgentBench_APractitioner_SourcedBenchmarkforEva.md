---
title: GISAgentBench: A Practitioner-Sourced Benchmark for Evaluating LLM Agents on GIS Tasks
published: 2026-08-03T03:31:45Z
authors: Abhinav Pothuri, Zhe Jiang, Zelin Xu, Di Yang
url: http://arxiv.org/abs/2608.01645v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GISAgentBench: A Practitioner-Sourced Benchmark for Evaluating LLM Agents on GIS Tasks

## Abstract
Geographic Information System (GIS) professionals rely on multi-step spatial analysis workflows to support decision-making in urban planning, disaster response, and environmental monitoring. The process is tedious, time-consuming, and error-prone. While recent large language model (LLM) agents equipped with external tools have the potential to automate geospatial analysis, their ability to perform realistic GIS workflows remains largely unexplored. Existing GIS agent benchmarking datasets are mostly drawn from textbooks, tutorials, or LLM-generated seeds and remain limited in size and trajectory depth. More importantly, none provides ground truth outputs. They therefore rely on surrogate signals such as code similarity, trajectory matching, or LLM and VLM judges, which can conflate workflow resemblance with task correctness. To address this gap, we introduce GISAgentBench, a benchmark of 349 multi-step GIS tasks curated from GIS Stack Exchange and instantiated on real public data across six selected geographic areas of interest. Each task ships with an executable reference trajectory and an exact ground truth output file, enabling strict, deterministic, tolerance-aware output matching beyond LLM judging. Evaluations of six LLM models reveal that realistic GIS workflows remain challenging: the best agent completes only 32.7% of tasks under strict tolerance-aware scoring, although most models produce outputs that are close to the ground truth.

## Metadata
- **Published**: 2026-08-03T03:31:45Z
- **Authors**: Abhinav Pothuri, Zhe Jiang, Zelin Xu, Di Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01645v1)