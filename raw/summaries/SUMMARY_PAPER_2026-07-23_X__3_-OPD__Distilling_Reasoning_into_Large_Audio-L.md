---
title: X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy Alignment
url: http://arxiv.org/abs/2607.21550v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_17-35-20Z_X__3__OPD_DistillingReasoningintoLargeAudio_Langua.md
generated_at: 2026-07-23 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces X$^3$-OPD, a cross‑modal on‑policy distillation framework that transfers reasoning capabilities from a powerful text teacher to an audio‑language student using matched textual inputs. It builds a three‑tier symmetric corpus covering speech‑rendered tasks, event‑based acoustic reasoning grounded in complex scenes, and spoken‑dialogue reasoning involving prosody. Experiments show X$^3$-OPD improves audio‑grounded reasoning and chain‑of‑thought quality while preserving the model’s existing capabilities under domain shift.

## Key Takeaways
- The framework uses on‑policy distillation where the student generates reasoning trajectories based on its own acoustic perception.
- A three‑tier symmetric corpus is created to cover textual, event‑based, and spoken‑dialogue reasoning grounded in non‑linguistic events and prosody.
- Experiments demonstrate substantial gains in audio‑grounded reasoning and chain‑of‑thought quality across MMSU, MMAU, BIG Bench Audio, and MMAR while maintaining performance under domain shift.

## Context
Large language models excel at text‑based logical reasoning but audio‑language models lag due to limited high‑quality reasoning data. This work addresses the gap by enabling cross‑modal transfer that leverages rich acoustic cues beyond mere speech transcripts.

## Implications
The results suggest that on‑policy distillation can bridge modality‑specific skill gaps, opening doors for applications where auditory perception and reasoning are critical such as voice assistants and interactive robotics. Practitioners may adopt X$^3$-OPD to enhance multimodal models without retraining from scratch.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21550v1)
