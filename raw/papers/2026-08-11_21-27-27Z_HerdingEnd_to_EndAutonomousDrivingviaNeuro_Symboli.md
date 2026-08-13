---
title: Herding End-to-End Autonomous Driving via Neuro-Symbolic Safety Guards
published: 2026-08-11T21:27:27Z
authors: Simón Patiño Idarraga, Erick Silva, Rehana Yasmin, Ali Shoker
url: http://arxiv.org/abs/2608.11451v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Herding End-to-End Autonomous Driving via Neuro-Symbolic Safety Guards

## Abstract
Modern end-to-end driving agents can achieve high average performance yet still violate basic traffic rules that a human driver would never miss. The reason is structural: they learn statistical patterns rather than the physical conditions that guarantee safe driving, leaving their decision-making process opaque and safety constraints unenforced. We introduce a neuro-symbolic safety guard, a lightweight module that attaches to the final command interface of an already-trained agent. Immediately before a command reaches the vehicle, it checks the command against explicit safety rules and, only when necessary, replaces it with the nearest safe alternative. Each intervention is directly executable and traceable to the rule that triggered it, while the guard itself requires no retraining and adds no learned component. Evaluated on the long-tail benchmarks Fail2Drive and Bench2Drive using the state-of-the-art TransFuser v6 (TFv6) as a case study, the guard improves Success Rate by 15% and reduces safety-critical collisions by up to 53%, while preserving the original Driving Score.

## Metadata
- **Published**: 2026-08-11T21:27:27Z
- **Authors**: Simón Patiño Idarraga, Erick Silva, Rehana Yasmin, Ali Shoker
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11451v1)