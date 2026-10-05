---
title: Hypothesis-guided discovery of cognitive algorithms via program refinement
url: http://arxiv.org/abs/2610.02523v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_21-53-21Z_Hypothesis_guideddiscoveryofcognitivealgorithmsvia.md
generated_at: 2026-10-04 21:44
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes a hybrid system for discovering cognitive algorithms from behavioral data by treating the problem as a program refinement task. The system combines human-created probabilistic programs with a pipeline of LLM agents that iteratively identify mismatches between model predictions and observed behavior, propose constrained code-level modifications, and verify structural fidelity. The authors demonstrate that revised models consistently outperform their ancestral counterparts in fitting human behavior across a problem-solving paradigm that exposes diverse cognitive algorithms.

## Key Takeaways
- The paper introduces a hybrid cognitive modeling framework that bridges the gap between traditional interpretable cognitive models (which benefit from human expertise but lack scalability) and fully automated LLM-based model generation (which is scalable but lacks human-guided structure). By expressing human-created cognitive models as probabilistic programs and tasking LLM agents with targeted refinement, the system preserves researcher intent while enabling automated improvement.
- The LLM agent pipeline operates under a three-part mandate: identifying behavioral mismatches between the model and data, proposing code-level modifications strictly within researcher-specified constraints, and verifying that structural fidelity is maintained throughout the revision process. This constraint-based approach ensures that modifications remain interpretable and scientifically grounded rather than producing opaque black-box models.
- Revisions propagate to a probabilistic inference module that handles latent variable inference and data likelihood computations, enabling rigorous statistical evaluation of each proposed modification. The evaluation reveals a small set of recurring innovations that capture meaningful behavioral variability, suggesting that cognitive algorithm discovery can be systematically guided rather than left to ad hoc human intuition.

## Context
This work sits at the intersection of cognitive science, probabilistic programming, and LLM-assisted scientific discovery. Cognitive modeling has long relied on hand-crafted models built from domain expertise, while recent LLM-based approaches offer automation but sacrifice interpretability and human oversight. By framing algorithm discovery as constrained program refinement, the paper addresses a critical methodological gap: how to leverage the generative flexibility of LLMs without abandoning the scientific rigor and interpretability that cognitive science demands. The approach also connects to broader trends in AI-assisted scientific discovery, where human-in-the-loop systems are increasingly seen as necessary for trustworthy and reproducible research.

## Implications
For cognitive scientists and modelers, this pipeline offers a practical workflow for iteratively improving existing cognitive models without requiring deep programming expertise or starting from scratch, potentially accelerating model development across diverse reasoning tasks. For the broader AI research community, the constrained-refinement paradigm demonstrates a template for using LLM agents as scientific collaborators rather than autonomous generators, preserving human accountability while scaling discovery. Practitioners in behavioral science, education, and human-computer interaction could apply similar refinement pipelines to build more accurate models of human problem-solving strategies, ultimately informing better system design and pedagogical approaches.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02523v1)
