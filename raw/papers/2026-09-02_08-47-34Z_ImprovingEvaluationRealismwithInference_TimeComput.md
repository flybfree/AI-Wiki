---
title: Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds
published: 2026-09-02T08:47:34Z
authors: Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera, Adeline Kassler, Dmitrii Troitskii, Alexandra Souly, Kai Fronsdal, Robert Kirk, John Hughes
url: http://arxiv.org/abs/2609.02302v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds

## Abstract
A core obstacle to alignment evaluation is evaluation awareness: capable models can tell when they are being tested rather than deployed, weakening the conclusions a safety evaluation can support. We present two techniques that make simulated alignment evaluations harder to distinguish from real deployments. Our first technique, critique refinement, spends additional inference-time compute on each simulator action: the simulator generates multiple candidate actions, refines them using feedback from an instance of the target model on how to make them more realistic, and continues the evaluation with the most deployment-like candidate. Our second technique, DISH (Deployment-Imitating SWE-Agent Harness), wraps the target in an agent harness, reducing the gap between simulated and real deployment environments in coding settings. We test the techniques on multiple target models and find that they compose: applying both yields larger realism gains than either alone. Our results show that automated approaches can improve the realism of alignment evaluations, and that these improvements use additional compute more effectively than making the audits longer.

## Metadata
- **Published**: 2026-09-02T08:47:34Z
- **Authors**: Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera, Adeline Kassler, Dmitrii Troitskii, Alexandra Souly, Kai Fronsdal, Robert Kirk, John Hughes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02302v1)