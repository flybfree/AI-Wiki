---
title: Learning Dynamic User Personas from Implicit Interaction Streams via Iterative Refinement
published: 2026-07-29T04:56:14Z
authors: Haifeng Wu
url: http://arxiv.org/abs/2607.26473v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Dynamic User Personas from Implicit Interaction Streams via Iterative Refinement

## Abstract
Personalizing large language models (LLMs) to individual users is essential for improving user experience, yet existing approaches typically rely on explicit preference supervision such as pairwise comparisons or demographic attributes, limiting their applicability in natural interaction settings. We propose IRIS, a framework that learns dynamic user personas directly from implicit interaction streams by extracting behavioral signals from everyday conversations and iteratively refining persona representations through a prediction-driven closed loop without requiring explicit feedback. We introduce an evaluation protocol based on behavior prediction, persona stability, and decision prediction. A proof-of-concept study on a synthetic interaction stream derived from public-domain autobiographical text shows that IRIS produces stable personas and distinguishes individual users while revealing limitations of memory-only approaches on recall-oriented metrics. We then validate IRIS on anonymized real-world Reddit r/AmItheAsshole (AITA) data, with personas built solely from each author's historical interactions. Across 100 authors, IRIS achieves the highest decision prediction accuracy among all evaluated methods (61.0%), outperforming static personas, memory-only retrieval, and no-personalization baselines. These results suggest that implicit behavioral modeling provides a scalable alternative to explicit preference learning for personalized LLMs and offers a practical foundation for adaptive conversational systems and embodied agents that require continuously evolving models of their users.

## Metadata
- **Published**: 2026-07-29T04:56:14Z
- **Authors**: Haifeng Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26473v1)