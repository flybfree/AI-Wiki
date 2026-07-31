---
title: Temporal Poisoning: Clean-Label Backdoors via Event Redistribution in SNNs
url: http://arxiv.org/abs/2607.28075v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_11-49-28Z_TemporalPoisoning_Clean_LabelBackdoorsviaEventRedi.md
generated_at: 2026-07-30 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a clean-label temporal poisoning attack for spiking neural networks where only the target class is subjected to a timestamp transformation that does not change labels but alters event sequences. Experiments on three neuromorphic datasets and both CNN and transformer models achieve perfect ASR under strong configurations. The authors also evaluate defenses, showing many collapse before inspection while model-free detectors based on per-step event mass can spot the attack.

## Key Takeaways
- The temporal transformation preserves per-pixel per-polarity event counts exactly, making clean and triggered samples indistinguishable after aggregation yet changing the SNN input sequence.
- Attack achieves ASR of 1.00 across three datasets and both CNN and transformer victims under strong poisoning budgets, demonstrating high effectiveness.
- Model-free detectors that rely on per-step event mass can detect the temporal transformation, revealing limits to rate-collapsed defenses.

## Context
Spiking neural networks process data as binary events rather than continuous values, making traditional poisoning methods less effective. This work extends backdoor research to neuromorphic hardware where timing is critical and labels remain clean, highlighting a gap in current defense strategies for event-based models.

## Implications
For practitioners, the attack shows that defenses must consider temporal structure beyond simple rate thresholds. Industry adoption of SNNs may require new monitoring mechanisms that inspect per-step event mass to prevent stealthy poisoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28075v1)
