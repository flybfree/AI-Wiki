---
title: RotDroid: Cross-Orientation State Equivalence Testing for Detecting GUI Rotation Bugs in Android Apps
published: 2026-08-26T06:30:21Z
authors: Mengdi Qin, Bo Jiang
url: http://arxiv.org/abs/2608.25425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RotDroid: Cross-Orientation State Equivalence Testing for Detecting GUI Rotation Bugs in Android Apps

## Abstract
Screen rotation is a fundamental interaction in Android applications, but it often introduces non-crashing functional failures (NCFs), such as layout inconsistencies and state loss, which are difficult to detect automatically. A key challenge is the lack of effective test oracles for checking cross-orientation state equivalence between portrait and landscape views. We propose RotDroid, a testing framework for detecting GUI rotation bugs via cross-orientation state equivalence. RotDroid generates and mutates State-Preserving action Sequences (SPS) to construct semantically equivalent GUI states across orientations. To support reliable oracle checking, we build RotBench, a dataset of paired portrait-landscape GUI states, and develop RotVL, a vision-language model fine-tuned for equivalence checking. Experiments on both synthetic and real-world datasets show that RotVL outperforms state-of-the-art models, and RotDroid detects more rotation-induced failures than existing techniques under equal budgets. In large-scale studies on open- and closed-source apps, RotDroid reports 94 previously unknown bugs, with 47 confirmed or fixed by developers, demonstrating its practical effectiveness.

## Metadata
- **Published**: 2026-08-26T06:30:21Z
- **Authors**: Mengdi Qin, Bo Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25425v1)