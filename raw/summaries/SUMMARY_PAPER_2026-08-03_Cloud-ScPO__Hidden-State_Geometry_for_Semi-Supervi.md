---
title: Cloud-ScPO: Hidden-State Geometry for Semi-Supervised Preference Optimization in LLM Reasoning
url: http://arxiv.org/abs/2608.01014v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_05-33-41Z_Cloud_ScPO_Hidden_StateGeometryforSemi_SupervisedP.md
generated_at: 2026-08-03 20:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Cloud‑ScPO, a method that uses the internal geometry of reasoning trajectories to generate semi‑supervised preference pairs without human labels. It finds that correct and incorrect answer paths form distinct cloud structures across problems, enabling a geometric basis for preference selection.

## Key Takeaways
- The model clusters hidden states into components where correct trajectories are tightly connected while incorrect ones are fragmented, revealing a clear geometric difference between right and wrong reasoning.
- A cross‑problem Cloud signal is combined with prompt‑level self‑consistency to select high‑scoring trajectory pairs, merging answer preference with trajectory quality.
- Experiments show up to 4.5% gain on GSM8K and 4.2% on MATH‑Numeric while maintaining comparable correctness reliability across model settings.

## Context
In large language models, preference optimization is crucial for improving reasoning but often relies on costly human annotations or external reward models that cannot scale to billions of parameters.

## Implications
This approach enables scalable, label‑light training that can be applied to any LLM with internal state access, offering a path toward more robust and efficient preference learning for downstream reasoning tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01014v1)
