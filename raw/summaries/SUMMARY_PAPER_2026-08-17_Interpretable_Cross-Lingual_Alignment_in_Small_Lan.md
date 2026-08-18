---
title: Interpretable Cross-Lingual Alignment in Small Language Models: Probing Cultural and Pragmatic Reasoning in Japanese-English Bilingual LLMs
url: http://arxiv.org/abs/2608.14896v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_21-04-21Z_InterpretableCross_LingualAlignmentinSmallLanguage.md
generated_at: 2026-08-17 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces J-PragEval‑v0, a minimal‑pair benchmark that isolates four Japanese‑English pragmatic phenomena and evaluates TinySwallow‑1.5B’s handling of them with linear probes and teacher‑forced log‑probability analysis. It finds that honorific register is encoded in the residual stream at layer 15, while implicit subject and in‑group reference are not linearly decodable but flip during generation, and indirect refusal suffers from low probe accuracy because the current pairs conflate politeness with continuation length.

## Key Takeaways
- Honorific register sits cleanly in the residual stream: 0.96 balanced accuracy at layer 15, with a 93 % flip rate when the scenario changes.
- Implicit subject and in‑group reference contrast is not stored at the prompt (0.48 and 0.38 probe scores) but flips during generation (0.77 and 0.79), indicating work is done later in the model.
- Indirect refusal shows a collapse of probe accuracy to 0.43 under length‑normalised teacher forcing, revealing that politeness cues are mixed with continuation length in minimal pairs.

## Context
Understanding pragmatic competence beyond translation quality is crucial for cross‑lingual AI systems that serve culturally distant languages like Japanese. This work demonstrates how probing can reveal where cultural knowledge resides within a model’s architecture, offering insight into the limits of current evaluation benchmarks.

## Implications
For practitioners, this research suggests that inference‑time steering could be used to edit residual activations along identified contrast directions, potentially improving pragmatic alignment without retraining. It also highlights the need for benchmark designs that separate surface fluency from culturally sensitive reasoning in multilingual models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14896v1)
