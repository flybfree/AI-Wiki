---
title: Large Language Model for Operations Research Formulation Selection in Multi-Warehouse Inventory Allocation
url: http://arxiv.org/abs/2607.25956v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_16-41-54Z_LargeLanguageModelforOperationsResearchFormulation.md
generated_at: 2026-07-28 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a solver‑guided large language model that selects mixed‑integer programming formulations for each multi‑warehouse inventory allocation instance. Experiments on JD.com data show the selector’s hit ratios rise from 21.45% to 50.42% at one and from 70.47% to 82.31% at two, delivering a 12.57‑point accuracy gain over existing methods.

## Key Takeaways
- The selector’s hit ratio improves dramatically, reaching 50.42% at Hit Ratio@1 and 82.31% at Hit Ratio@2, far exceeding baseline performance.
- It achieves a 12.57‑point allocation accuracy gain over the incumbent fixed formulation, closing the gap to the oracle by only 4.85 percentage points.
- The framework combines supervised fine‑tuning with reward‑based group relative policy optimization to learn instance‑specific preference scores.

## Context
Large language models are increasingly used for automated problem formulation selection in operations research, but prior approaches rely on static training or fixed expert choices that cannot adapt to heterogeneous demand patterns. This work demonstrates how integrating solver feedback into LLM training can yield dynamic, high‑quality selections.

## Implications
For industry practitioners, the method offers a scalable way to automate inventory allocation decisions without manual formulation engineering. It also sets a benchmark for AI‑driven OR tool selection, encouraging further research on adaptive expert libraries and reinforcement learning in logistics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25956v1)
