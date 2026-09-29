---
title: PEAR: Progressive Evidence-Based AutoResearch for Industrial Search Systems
published: 2026-09-28T12:30:00Z
authors: Yifan Wang, Shipeng Zhu, Fei Xiong, Yuqin Yang, Yonghui Huang, Kunyao Wu, Yue Wang, Weichao Meng, Yu Gong
url: http://arxiv.org/abs/2609.35031v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PEAR: Progressive Evidence-Based AutoResearch for Industrial Search Systems

## Abstract
AutoResearch improves systems through iterative experimentation: agents propose candidate modifications, evaluate them, and use the results to guide subsequent exploration. Applying this paradigm to industrial search presents two challenges. (1) Common AutoResearch approaches follow a keep-if-better rule, retaining the highest-scoring candidate for subsequent experiments. Under non-stationary traffic, transient gains may be mistaken for persistent improvements, impairing reliable accumulation of search knowledge. (2) Candidate modifications can be evaluated at multiple fidelity levels, from low-cost proxies to online validation, differing in cost, objective alignment, and statistical reliability. Existing methods rely on individual signals or task-specific procedures, lacking a unified basis for using evidence across levels to guide search. We introduce Progressive Evidence-Based AutoResearch (PEAR) with two complementary components. Evidence-driven AutoResearch maintains an independent, hypothesis-guided research state for each strategy task within a predefined objective and intervention scope. Each state evolves through a Plan-Execute-Evaluate-Update transition that links experimentation to context-aware evidence interpretation and hypothesis revision. Confidence-Gated Verifier Ladder organizes evaluation into four levels of increasing fidelity: Offline Replay, Shadow-Traffic Evaluation, Rapid Online Evaluation, and Decision-Grade Online Evaluation. A unified confidence-based gate promotes candidates only when evidence supports a statistically significant positive effect, enabling broad low-cost exploration while reserving costly online experiments for promoted candidates. In a real-world industrial search system, strategies optimized with PEAR significantly increased Main Order/DAU by 2.7336% and 3.2957% relative to their respective baselines in two A/B experiments.

## Metadata
- **Published**: 2026-09-28T12:30:00Z
- **Authors**: Yifan Wang, Shipeng Zhu, Fei Xiong, Yuqin Yang, Yonghui Huang, Kunyao Wu, Yue Wang, Weichao Meng, Yu Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35031v1)