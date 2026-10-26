---
title: Why Full-Duplex Speech Models Collapse in Long Conversations
url: http://arxiv.org/abs/2610.32349v1
type: paper-summary
date: 2026-10-25
source_paper: 2026-10-23_08-43-45Z_WhyFull_DuplexSpeechModelsCollapseinLongConversati.md
generated_at: 2026-10-25 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates why full-duplex speech models—which simultaneously listen and speak—fail to sustain coherent conversations over extended durations. The authors introduce the Full-Duplex Long-Horizon Benchmark (FD-LHB) to evaluate five recent models on conversations lasting tens of minutes, revealing that every tested model eventually degrades or exhausts its context window. They diagnose two specific failure mechanisms in sliding-window models and propose lightweight fixes—Initialization-Anchor Pinning and Duplex Repetition Penalty—that substantially reduce conversational collapse without retraining.

## Key Takeaways
- Full-duplex models generate a token every frame even while listening, which means they consume context window capacity at a constant rate regardless of whether they are actively speaking. Existing benchmarks only test single turns or a few rounds, masking this long-horizon exhaustion problem. The FD-LHB benchmark exposes it by replaying conversations up to an hour and conducting live dialogue with an LLM partner.
- Two distinct failure mechanisms are identified for sliding-window architectures. First, Initialization-Anchor Eviction occurs when the sliding window discards the very first key-value entry, which acts as an initialization anchor for the model's internal state; its removal triggers gibberish output and prolonged silence. Second, repetition is reinforced by the model's own recent outputs feeding back into the window, creating a self-amplifying echo loop.
- The proposed mitigations—Initialization-Anchor Pinning (IAP) to preserve the first KV entry and Duplex Repetition Penalty (DRP) to discourage echoing while guarding against silence—operate at inference time without any retraining. Together they substantially reduce conversational collapse in hour-long replays while maintaining real-time operation, validating the diagnostic framework.

## Context
Full-duplex speech models represent the frontier of natural conversational AI, aiming to replicate human-like simultaneous listening and speaking rather than turn-based interaction. However, the field has largely evaluated these systems on short interactions, leaving a critical gap in understanding their behavior over realistic conversation lengths. This paper fills that gap by providing the first systematic long-horizon evaluation and a mechanistic diagnosis of failure modes, shifting the research conversation from "can a model respond correctly in one turn" to "can a model remain coherent across an entire dialogue."

## Implications
For practitioners building voice assistants, customer-service agents, or real-time translation systems, this work demonstrates that architectural choices around context management—particularly sliding-window strategies—introduce failure modes that only manifest after several minutes of interaction. The finding that no retraining is needed to mitigate collapse suggests that deployment-time interventions can extend usable conversation length significantly, lowering the barrier to deploying full-duplex models in production. For the research community, the FD-LHB benchmark and the identified mechanisms provide a concrete evaluation target and a diagnostic vocabulary that future model designs can be tested against, accelerating progress toward truly open-ended conversational AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.32349v1)
