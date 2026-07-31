---
title: MemeBench: What LVLMs Miss When Interpreting Culture-Dependent Memes
url: http://arxiv.org/abs/2607.27798v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_07-36-53Z_MemeBench_WhatLVLMsMissWhenInterpretingCulture_Dep.md
generated_at: 2026-07-30 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MemeBench, a diagnostic benchmark of 1,253 Chinese and English memes that tests whether vision‑language models can interpret culture‑dependent humor. The study finds that even the strongest LVLMs consistently miss the knowledge required to explain memes, leaving a 22.6% visual‑knowledge gap. Retrieval‑based methods improve explanation success by 3.6–7.4% but trade off some visual coverage.

## Key Takeaways
- MemeBench reveals that most LVLMs can describe what is visible but fail to link it to cultural entities, identity references, or background knowledge needed for interpretation.
- Retrieval‑based baselines such as KAR boost VIKR success by 3.6–7.4% while repairing more answers and breaking fewer explanations compared with generic retrieval.
- The benchmark shows that targeted evidence can fill the diagnosed visual‑knowledge gap, improving both identity linking and reasoning mechanisms.

## Context
Vision‑language models excel at describing images but struggle when meaning depends on cultural context, which is common in memes. This work highlights a persistent limitation of current AI systems in handling community‑driven content that relies on shared knowledge rather than pixel data alone.

## Implications
For researchers, MemeBench provides a systematic way to diagnose and address the visual‑knowledge gap in model explanations. For industry practitioners, it suggests that integrating entity‑guided retrieval can significantly enhance interpretability without sacrificing overall performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27798v1)
