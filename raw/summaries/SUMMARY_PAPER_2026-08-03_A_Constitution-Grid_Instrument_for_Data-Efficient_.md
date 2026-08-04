---
title: A Constitution-Grid Instrument for Data-Efficient RL Alignment (C-Guard)
url: http://arxiv.org/abs/2608.00180v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_18-05-25Z_AConstitution_GridInstrumentforData_EfficientRLAli.md
generated_at: 2026-08-03 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces C-Guard, a constitution-grid instrument for generating RL training data that balances safety and utility objectives efficiently. It demonstrates that over‑refusal improves performance while under‑refusal harms it, and proposes C-LIM to prune dead-weight rows before training budget is spent.

## Key Takeaways
- Over‑refusal on benign prompts raises detection accuracy from 22.4% to 12.8%, showing a trade‑off between safety and utility.
- Under‑refusal on adversarial attacks silently worsens performance, increasing error rates from 0.27 to 0.33.
- C-LIM identifies 187 untargeted rows that contribute no gain; the method lifts their learning impact from 0.733 to 0.80.

## Context
RL alignment faces a fundamental tension between safety and performance, making data efficiency critical. Existing methods often require massive labeled datasets or suffer from over‑fitting to harmful examples. C-Guard’s grid‑based approach offers a principled way to allocate training budget without exhaustive labeling.

## Implications
For practitioners, C-Guard reduces the need for large safety datasets while maintaining high detection rates. The open‑source code and “constitution” can be integrated into existing RL pipelines, enabling faster iteration and more responsible model deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00180v1)
