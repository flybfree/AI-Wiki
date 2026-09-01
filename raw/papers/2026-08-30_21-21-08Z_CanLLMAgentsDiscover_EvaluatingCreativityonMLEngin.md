---
title: Can LLM Agents Discover? Evaluating Creativity on ML Engineering Tasks
published: 2026-08-30T21:21:08Z
authors: Shitanshu Bhushan, Yunxiang Zhang, Lu Wang
url: http://arxiv.org/abs/2608.30047v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can LLM Agents Discover? Evaluating Creativity on ML Engineering Tasks

## Abstract
Recent AI systems promise autonomous scientific discovery, claiming to discover algorithms and produce research papers, yet understanding whether they exhibit creativity, the capacity to produce solutions that are both novel and useful, remains an open question. We present a framework for evaluating multi-turn LLM research agents' creativity using ML engineering tasks as a testbed, through three dimensions: P-Creativity (psychological novelty: novel relative to the agent's own prior solutions within a run), H-Creativity (historical novelty: novel relative to the corpus of human solutions), and Usefulness (task performance). Evaluating two agent frameworks, AIDE and AIRA-Dojo, on 10 Kaggle-style machine learning tasks from MLE-Bench, we develop an LLM-as-a-Judge pipeline and verify its strong correlation with human creativity judgments, providing a reliable automated metric for P-Creativity evaluation at scale. Applying this pipeline to agent trajectories, we find: (1) all agents exhibit declining P-Creativity as they transition from exploration to exploitation; (2) LLMs exhibit greater H-Creativity than medal-winning humans, yet achieve lower performance. Our findings reveal that current agents can explore novel regions of the solution space but lack the capacity to convert this novelty into improved task performance.

## Metadata
- **Published**: 2026-08-30T21:21:08Z
- **Authors**: Shitanshu Bhushan, Yunxiang Zhang, Lu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30047v1)