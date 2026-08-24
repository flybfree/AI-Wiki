---
title: Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning
published: 2026-08-20T20:57:25Z
authors: Abhijith Babu, Ramneet Kaur, Vishal Pramanik, Olivera Kotevska, Nathaniel D. Bastian, Susmit Jha, Sunny Raj, Yanzhao Wu, Sumit Kumar Jha, Anirban Roy
url: http://arxiv.org/abs/2608.20564v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning

## Abstract
Multi-agent LLM systems can improve reasoning by pooling diverse perspectives, but their effectiveness depends on coordinating communication, particularly in hidden-profile settings where each agent holds only part of the evidence required for a correct decision. Existing protocols, including fixed schedules, round-robin exchange, and unstructured debate, provide no guarantee that a conversational action is appropriate. We propose Consilience, an inference-time orchestration framework that both steers and certifies multi-agent communication under distributed private information. At each turn, Consilience summarizes the discussion using a compact state capturing uncertainty, disagreement, evidence gain, redundancy, and premature consensus, then selects both a communication intervention (challenge, clarify, seek evidence, or route) and an appropriate speaker. Its central contribution is a round-wise conformal calibration procedure that provides a distribution-free, finite-sample guarantee: at each discussion round, conditional on reaching that round, the one-step regret of a controller's proposed action is bounded by a calibrated threshold with marginal probability at least 1 - alpha; an acceptance mechanism enforces the same guarantee for the executed action by replacing inadmissible proposals. On HiddenBench-style hidden-profile tasks spanning 12 open and closed weight language models, Consilience improves decision accuracy and communication efficiency over fixed and unstructured discussion protocols, sometimes surpassing a full-information baseline where every agent observes all evidence. These results demonstrate that certified adaptive communication control can be more valuable than increasing information availability, providing a practical mechanism for reliable multi-agent LLM coordination.

## Metadata
- **Published**: 2026-08-20T20:57:25Z
- **Authors**: Abhijith Babu, Ramneet Kaur, Vishal Pramanik, Olivera Kotevska, Nathaniel D. Bastian, Susmit Jha, Sunny Raj, Yanzhao Wu, Sumit Kumar Jha, Anirban Roy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20564v1)