---
title: Temporal Poisoning: Clean-Label Backdoors via Event Redistribution in SNNs
published: 2026-07-30T11:49:28Z
authors: Roberto Riaño, Gorka Abad, Stjepan Picek, Aitor Urbieta
url: http://arxiv.org/abs/2607.28075v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Temporal Poisoning: Clean-Label Backdoors via Event Redistribution in SNNs

## Abstract
Backdoor attacks on Spiking Neural Networks (SNNs) have primarily assumed dirty-label poisoning, in which triggered training samples are relabeled to an attacker-selected class. We study clean-label temporal poisoning, where a fixed timestamp transformation is applied only to the target-class training streams, leaving their labels unchanged. The transformation preserves the per-pixel, per-polarity event count exactly, making clean and triggered samples identical after temporal aggregation while altering the sequence processed by the SNN. Across three neuromorphic datasets and both convolutional and transformer-based victims, the attack reaches an ASR of 1.00 in the strongest configurations. We analyze the attack through poison-budget and trigger-shape ablations and evaluate established backdoor defenses adapted to spiking models. Defenses that collapse the time axis before inspection are blind by construction, while feature-space methods detect the poison only in selected settings. Our model-free detector, based on per-step event mass, detects the evaluated temporal transformations, demonstrating both the limitation of rate-collapsed defenses and the boundary of the attack's stealth. To our knowledge, this is the first clean-label backdoor attack evaluated on SNNs and neuromorphic event data.

## Metadata
- **Published**: 2026-07-30T11:49:28Z
- **Authors**: Roberto Riaño, Gorka Abad, Stjepan Picek, Aitor Urbieta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28075v1)