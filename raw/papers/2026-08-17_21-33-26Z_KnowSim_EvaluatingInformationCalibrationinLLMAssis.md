---
title: KnowSim: Evaluating Information Calibration in LLM Assistants with User Simulators that Learn
published: 2026-08-17T21:33:26Z
authors: Yoonjoo Lee, Hyoungwook Jin, Tae Soo Kim, Shaoyang Zhang, Philippe Laban, Q. Vera Liao
url: http://arxiv.org/abs/2608.17150v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KnowSim: Evaluating Information Calibration in LLM Assistants with User Simulators that Learn

## Abstract
To effectively collaborate with users on knowledge-intensive tasks, Large Language Models (LLMs) must perform information calibration: matching content to a user's evolving understanding and cognitive capacity. Yet user simulators used to evaluate and train LLMs do not explicitly model user knowledge so they neither produce realistic interactions across knowledge levels nor reflect how interactions unfold as that knowledge evolves. To close this gap, we introduce KNOWSIM, an evaluation framework built around a user simulator that maintains explicit knowledge states, represented as a graph of Information Units with prerequisite relationships, that evolve under update rules grounded in learning theory. KNOWSIM computes three metrics (Knowledge Gain, Delivery Calibration, Cognitive Overload) directly from the knowledge state trajectory, reflecting key mechanistic aspects of information calibration. We validate KNOWSIM against 705 human-AI sessions across two domains, stratified by knowledge level: its rankings align significantly with human judgments (73-74% sign agreement), outperforming three baseline simulators. Applied to 9 LLMs, KNOWSIM reveals that the best model shifts by user knowledge level, revealing aptitude-treatment interactions invisible to standard evaluation.

## Metadata
- **Published**: 2026-08-17T21:33:26Z
- **Authors**: Yoonjoo Lee, Hyoungwook Jin, Tae Soo Kim, Shaoyang Zhang, Philippe Laban, Q. Vera Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17150v1)