---
title: RADAR: Rubric-Aware Dependency and Redundancy Analysis for LLM-as-Judge Evaluation
published: 2026-08-03T07:21:32Z
authors: Divyansh Singh, Reza Davari, Afra Mashhadi
url: http://arxiv.org/abs/2608.01810v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RADAR: Rubric-Aware Dependency and Redundancy Analysis for LLM-as-Judge Evaluation

## Abstract
Rubric-based LLM-as-judge pipelines often assume that evaluation criteria provide independent signals. In practice, however, criteria can be behaviorally coupled: improving one criterion may systematically change scores on another, distorting aggregate scores used in model-release or product-update decisions. We introduce RADAR, a lightweight preflight diagnostic framework for estimating such coupling before large-scale evaluation. Given a rubric, RADAR generates targeted synthetic probes, scores each probe on all criteria, and produces a directional coupling matrix that shows which criteria co-score and how. We validate RADAR on three industry-relevant evaluation settings: NVIDIA HelpSteer2, SumPubMed, and the Yale-Salesforce SummEval benchmark. Using only a small number of probes per criterion, RADAR recovers human inter-criterion correlation structure (Pearson r > 0.84) and provides practitioners with concrete audit signals about redundancy, hierarchy, and aggregation sensitivity before committing to large-scale judging.

## Metadata
- **Published**: 2026-08-03T07:21:32Z
- **Authors**: Divyansh Singh, Reza Davari, Afra Mashhadi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01810v1)