---
title: Augmenting Human Performance with an XR Agent Learning from Online Behavior and BCI Evidence
published: 2026-08-31T07:25:51Z
authors: Ziheng Li, Xichen He, Haoyan Chen, Charlie Zou, Sheng Bai, Benjamin Yang, Mengyuan Wu, Jake Ledner, Yi-Jie Cheng, Akito Yamauchi, Dishita G Turakhia, Steven Feiner, Paul Sajda
url: http://arxiv.org/abs/2608.30369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Augmenting Human Performance with an XR Agent Learning from Online Behavior and BCI Evidence

## Abstract
We present OLIVE, a framework for adapting a foundation model to provide real-time assistance in temporally demanding, high-stakes, and dynamic tasks. We show that passive EEG, fused online with behavioral evidence, can meaningfully extend the number of targets users detect and engage beyond their unaided action bandwidth. OLIVE learns from both explicit behavioral signals (the targets the user shoots down in an XR first-person shooter game) and implicit physiological signals (fixation-locked EEG) to provide timely guidance, continuously adapting a frozen vision-language model's inference on which items are task-relevant by jointly estimating per-source reliability without manual labels or offline training. Through three user studies, including two live deployments of an assistive agent driven by OLIVE in XR, we show that OLIVE Pareto-dominates prior test-time adaptation frameworks, achieving the highest convergence rate at comparable convergence speed. Combining implicit physiological and explicit behavioral signals, the OLIVE agent produces the largest and most reliable within-session improvement to a user's ability to detect and engage targets, largely independent of the individual's skill. When the target switches silently, the agent that uses both behavioral and physiological signals reconverges significantly faster than the behavior-only agent (1.27 times faster on average, p = .008), restoring trustworthy guidance at the moment the task changes, precisely when reliable assistance matters most.

## Metadata
- **Published**: 2026-08-31T07:25:51Z
- **Authors**: Ziheng Li, Xichen He, Haoyan Chen, Charlie Zou, Sheng Bai, Benjamin Yang, Mengyuan Wu, Jake Ledner, Yi-Jie Cheng, Akito Yamauchi, Dishita G Turakhia, Steven Feiner, Paul Sajda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30369v1)