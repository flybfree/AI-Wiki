---
title: NARRATE: A Multimodal Real-World Australian Driving Dataset for Human-Centred Explanations in Automated Driving
url: http://arxiv.org/abs/2608.14767v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_12-35-24Z_NARRATE_AMultimodalReal_WorldAustralianDrivingData.md
generated_at: 2026-08-17 21:44
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces NARRATE, a multimodal real‑world driving dataset collected from 35 experienced drivers and instructors on public roads in Australia. The dataset links synchronized visual, localisation, motion, and LiDAR streams to free‑text driver explanations, enabling the study of how human‑centred explanations can be learned from actual driving actions.

## Key Takeaways
- NARRATE provides 2,050 annotated events with action labels, scenario‑context categories (six high‑level and 32 fine‑grained), and span‑level Situational Awareness annotations across Perception, Comprehension, and Projection.  
- The dataset demonstrates that driver language can be used to learn these labels, yet fine‑grained context recognition and explanation generation remain challenging tasks.  
- By grounding explanations in real driving streams, NARRATE bridges the gap between simulation‑based annotation and practical human‑centred AI.

## Context
Current automated driving research relies heavily on observer‑written or simulated annotations that lack direct driver input. This limits the realism of training data for explanation models, which must understand both the scenario and the driver’s intent. NARRATE offers a more authentic source, aligning with the need for domain‑aware AI systems.

## Implications
For industry practitioners, NARRATE can improve the development of trustworthy autonomous driving interfaces by providing richer, human‑generated explanations. Practitioners can leverage these annotations to fine‑tune models that balance safety and user comprehension in real‑world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14767v1)
