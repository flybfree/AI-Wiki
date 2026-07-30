---
title: DuplexGen: Adaptive Synthesis of Human-AI Turn-Taking Dialogues
url: http://arxiv.org/abs/2607.26178v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_18-36-46Z_DuplexGen_AdaptiveSynthesisofHuman_AITurn_TakingDi.md
generated_at: 2026-07-29 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
DuplexGen is a framework that generates human‑AI dialogues where each participant’s turn‑taking follows the preferences of real humans in specific scenarios. By calibrating large language model predictions against a small set of slot‑level preference annotations, DuplexGen produces turn‑taking patterns that differ from those produced by generic prompting or training on human‑human corpora alone. Experiments across six cooperative and competitive tasks show that DuplexGen aligns more closely with observed human preferences than uncalibrated methods.

## Key Takeaways
- Human turn‑taking preferences vary systematically across different task scenarios, and DuplexGen captures these variations by using slot‑level preference annotations to guide LLM output.  
- The framework outperforms both generic prompting and models trained solely on human‑human speech corpora because it directly incorporates user‑specific timing norms rather than relying on corpus scale or heuristic rules.  
- A full‑duplex model trained on DuplexGen‑generated data exhibits distinctive turn‑taking behaviors that match observed human preferences, demonstrating that calibration—not just large datasets—enables scenario‑specific synthesis.

## Context
Current AI dialogue systems often treat turn‑taking as a fixed norm derived from generic human speech corpora, which limits their ability to adapt to varied interaction contexts. This paper addresses the gap by showing that precise human calibration can produce context‑aware turn‑taking without needing massive new data or complex prompting.

## Implications
For developers building conversational agents, DuplexGen offers a practical path to embed realistic, scenario‑specific timing in AI responses. Practitioners can improve user experience and task performance by calibrating models on small preference datasets rather than relying solely on large generic corpora.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26178v1)
