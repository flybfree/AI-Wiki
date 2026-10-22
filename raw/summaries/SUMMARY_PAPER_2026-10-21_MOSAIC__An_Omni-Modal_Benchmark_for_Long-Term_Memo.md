---
title: MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents
url: http://arxiv.org/abs/2610.29249v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_05-55-20Z_MOSAIC_AnOmni_ModalBenchmarkforLong_TermMemoryandC.md
generated_at: 2026-10-21 20:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MOSAIC introduces a 923-question benchmark designed to evaluate long-term memory and cross-modal reasoning in omni-modal conversational agents across text, image, video, and audio modalities spanning 11-24 sessions of persona-grounded conversation history. The benchmark's core contribution is a matched diagnostic protocol that isolates failures at four distinct stages—representation, retrieval, delivery, and reading—revealing that representation loss is modality-dependent, residual reading failures dominate even when gold evidence is provided, and models struggle to appropriately abstain from answering when evidence is insufficient.

## Key Takeaways
- MOSAIC constructs targeted spatial, temporal, and prosodic signals rather than decorative media, with the strongest causal validation for spatial information and selector-level validation for annotated prosody. This design choice ensures that benchmark questions test genuine cross-modal reasoning rather than superficial pattern matching, making the evaluation scientifically rigorous and diagnostically meaningful.
- The matched diagnostic protocol freezes the question, reader, prompt, and budget while systematically intervening on representation, retrieval, and delivery stages. This controlled decomposition reveals that representation loss is modality-dependent—meaning different modalities fail at different stages of the memory pipeline—and that residual reading failures dominate even when gold evidence is directly provided to the model, indicating that comprehension of retrieved evidence remains a critical bottleneck.
- The benchmark exposes a critical failure mode in abstention behavior: strong answerable scores coexist with failures to refuse when evidence is genuinely absent or insufficient. This means current omni-modal agents can perform well on questions with available evidence while simultaneously failing to recognize when they should decline to answer, a dangerous combination for real-world deployment where hallucinated responses carry real consequences.

## Context
Existing long-term memory benchmarks for conversational agents are predominantly limited to text-and-image modalities or report only a single end-to-end score, which obscures where in the memory pipeline evidence is lost. As omni-modal assistants increasingly integrate video, audio, and spatial reasoning into their capabilities, the field lacks evaluation frameworks that can pinpoint whether failures occur during encoding, storage, retrieval, delivery, or comprehension. MOSAIC addresses this gap by providing a structured, multi-stage diagnostic tool that moves beyond leaderboard-style scoring toward actionable failure analysis across all four modalities.

## Implications
For AI researchers and practitioners building omni-modal assistants, MOSAIC provides a diagnostic framework that identifies precisely which stage of the memory pipeline requires improvement, enabling targeted architectural interventions rather than undifferentiated model scaling. For industry deployment, the finding that models fail to abstain appropriately even under controlled conditions signals a safety risk: agents may confidently hallucinate across modalities in applications such as medical consultation, legal advice, or customer support where incorrect answers carry tangible harm. The benchmark's emphasis on persona-grounded, multi-session histories also reflects realistic conversational scenarios, making its findings directly transferable to production systems that must maintain coherent memory across extended user interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29249v1)
