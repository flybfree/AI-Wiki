---
title: MazzikaAI: A knowledge-based performance-to-prompt compiler for real-time Arabic maqam accompaniment with a streaming text-to-music model
url: http://arxiv.org/abs/2608.10360v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_01-37-55Z_MazzikaAI_Aknowledge_basedperformance_to_promptcom.md
generated_at: 2026-08-11 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MazzikaAI, a knowledge‑based system that compiles live MIDI, gesture, and inferred harmony into continuously updated text prompts to steer an unmodified streaming generator (Google Lyria RealTime) for realtime Arabic maqam accompaniment. It achieves subsecond latency and demonstrates higher offgrid quartertone content than baseline generation.

## Key Takeaways
- The system uses natural language as the actuator of a realtime control loop, compiling live musical data into prompts that guide an unmodified streaming generator without fine‑tuning.
- Expert knowledge of six maqamat, ornaments, and ensemble dynamics is embedded to maintain realtime responsiveness with subsecond key‑to‑audible update latency.
- Empirical results show dynamic prompt compilation reliably grounds generation in microtonal scales, significantly increasing offgrid quartertone content compared to baseline.

## Context
Generative music models are largely trained on Western equal temperament frameworks, leaving non‑Western modal traditions like Arabic maqam underrepresented. Real‑time accompaniment demands precise control and cultural fidelity, which few AI systems provide due to lack of fine‑tuned or culturally aware interfaces.

## Implications
This architecture offers a scalable blueprint for realtime human‑AI cocreation across diverse musical idioms, enabling adaptive music education and inclusive generative audio that respects non‑Western scales. It demonstrates how deterministic knowledgebased rules can bridge expert knowledge with foundation models without retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10360v1)
