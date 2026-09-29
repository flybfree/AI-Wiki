---
title: STRIDE: Automated Evaluation of Text-to-Trajectory Alignment across Diverse Contexts
published: 2026-09-28T10:01:45Z
authors: Wanchun Ni, Tao Qi, Leonel Aguilar, Jiugeng Sun, Marlene Wagner, Verena Zimmermann, Mennatallah El-Assady
url: http://arxiv.org/abs/2609.34799v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STRIDE: Automated Evaluation of Text-to-Trajectory Alignment across Diverse Contexts

## Abstract
Language-conditioned trajectory generation is here, but its evaluation has not kept pace. Existing pedestrian trajectory metrics compare trajectories with real-world human data. This does not scale to text-to-trajectory generation across diverse contexts, as collecting human trajectories for every scenario is costly and infeasible. Moreover, pedestrian behavior is heterogeneous and context-dependent, with no single metric as the correct answer, and current evaluation frameworks are not transferable to this domain. These challenges make scalable, reliable evaluation difficult. We introduce STRIDE, the first framework for evaluating context alignment between scenario descriptions and pedestrian trajectories. STRIDE addresses these challenges through three design choices. First, we derive our VRDST evaluation protocol from sociological theories to define a complete evaluation space. Second, it decomposes high-level context into scenario-adaptive behavioral questions. Third, every question is resolved against a deterministic measurement tool library that yields reproducible answers. Together, STRIDE enables complete, verifiable, automated, and scalable evaluation across diverse contexts without requiring human trajectory data. We instantiate STRIDE in the crowd domain as STRIDE-Bench, comprising 1K scenarios, 6K behavioral questions, and 11K measurements with calibrated expected answers across 30 real-world maps. Comprehensive human validations show that STRIDE-Bench is consistent with human behavior and judgment, achieving 80% human agreement. We further evaluate several text-to-trajectory models, finding limited context-alignment capability and persistent challenges in fine-grained context conditioning. We believe that the STRIDE framework provides a first step toward principled evaluation of context-aligned pedestrian trajectory generation.

## Metadata
- **Published**: 2026-09-28T10:01:45Z
- **Authors**: Wanchun Ni, Tao Qi, Leonel Aguilar, Jiugeng Sun, Marlene Wagner, Verena Zimmermann, Mennatallah El-Assady
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34799v1)