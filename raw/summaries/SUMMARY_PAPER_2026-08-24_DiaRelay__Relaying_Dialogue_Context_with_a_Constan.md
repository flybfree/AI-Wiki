---
title: DiaRelay: Relaying Dialogue Context with a Constant-Size Memory for Emotion Recognition in Conversation
url: http://arxiv.org/abs/2608.22745v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_03-09-15Z_DiaRelay_RelayingDialogueContextwithaConstant_Size.md
generated_at: 2026-08-24 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes DiaRelay, a lightweight adapter that adds a constant‑size memory to LLMs for emotion recognition in conversation. It achieves SOTA weighted F1 on MELD while only adding 7.1 million trainable parameters and leverages LoRA to maintain dialogue‑level state.

## Key Takeaways
- Selective Relay Memory Transition progressively aggregates useful historical evidence into a bounded relay memory and propagates it across successive utterance predictions.
- Dual-axis Relay Memory Read uses the propagated memory to dynamically modulate low‑rank feature transformations, enabling context‑dependent adaptation without test‑time gradient updates.
- The adapter adds only 7.1 million trainable parameters while achieving SOTA weighted F1 on MELD.

## Context
This work addresses a longstanding challenge in conversational AI where models must retain information beyond fixed window lengths to capture subtle emotional cues across distant turns, improving robustness and accuracy of emotion recognition tasks.

## Implications
For practitioners, DiaRelay offers an efficient way to extend LLM capabilities for dialogue understanding without heavy retraining or large memory overheads. It can be integrated into existing fine‑tuning pipelines, enabling better performance on real‑world conversation datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22745v1)
