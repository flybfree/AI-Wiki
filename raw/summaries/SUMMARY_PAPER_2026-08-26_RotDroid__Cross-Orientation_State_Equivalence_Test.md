---
title: RotDroid: Cross-Orientation State Equivalence Testing for Detecting GUI Rotation Bugs in Android Apps
url: http://arxiv.org/abs/2608.25425v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_06-30-21Z_RotDroid_Cross_OrientationStateEquivalenceTestingf.md
generated_at: 2026-08-26 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RotDroid, a framework that tests Android apps for GUI rotation bugs by checking cross-orientation state equivalence. It generates and mutates State-Preserving action Sequences to create equivalent states between portrait and landscape views. The authors report detecting 94 previously unknown bugs in large‑scale studies.

## Key Takeaways
- RotDroid constructs semantically equivalent GUI states across orientations using mutated State-Preserving action Sequences, enabling reliable oracle checking.
- It builds a dataset of paired portrait‑landscape states called RotBench and uses a vision‑language model fine‑tuned for equivalence checking to serve as an oracle.
- Experiments show the framework detects more rotation‑induced failures than existing techniques when using equal testing budgets.

## Context
Screen rotation bugs are common in Android apps, causing layout inconsistencies and state loss that often go unnoticed. Automated tools typically focus on crash detection, leaving functional regression across orientations undetected. This work addresses a gap by providing an automated test oracle for cross‑orientation state equivalence.

## Implications
The framework offers developers a practical way to catch rotation bugs early in testing pipelines without manual effort. By integrating vision‑language models as oracles, it bridges the gap between visual inspection and programmatic verification, potentially improving app quality across diverse screen sizes and orientations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25425v1)
