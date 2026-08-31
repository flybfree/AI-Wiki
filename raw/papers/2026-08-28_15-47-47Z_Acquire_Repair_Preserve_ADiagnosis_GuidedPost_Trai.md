---
title: Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents
published: 2026-08-28T15:47:47Z
authors: Nan Li
url: http://arxiv.org/abs/2608.28458v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents

## Abstract
Interactive dialogue games test a capability that static benchmarks largely leave implicit: a model must carry state across turns, interpret feedback, and choose valid actions under changing constraints. We study this setting in the LM Playschool Challenge with a 2B open-weight model, and find that many failures are not only broad knowledge failures but also local decision failures: repeated guesses, malformed actions, and violations of feedback that the model has just seen. These diagnostics motivate a training recipe organized around three steps: acquire broad game participation through supervised fine-tuning, repair mechanically verifiable failures within one targeted dialogue-game family using turn-local preference pairs, and preserve general capabilities beyond these dialogue games. In the official final evaluation, our submission improves public clemscore from 10.67 to 38.92 and closed in-domain score from 13.41 to 41.17, while approximately preserving aggregate static performance (44.14 vs. 44.24 for the baseline). Out-of-domain clemscore remains low at 7.88, with the largest gains concentrated in unseen variants of the targeted family. Our results suggest that broad SFT brings most of the model's capability improvement; turn-local supervision can be effective when failure detection is precise, with observed transfer concentrated primarily within-family.

## Metadata
- **Published**: 2026-08-28T15:47:47Z
- **Authors**: Nan Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28458v1)