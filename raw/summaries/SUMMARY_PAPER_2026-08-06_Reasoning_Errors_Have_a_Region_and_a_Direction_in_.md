---
title: Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs
url: http://arxiv.org/abs/2608.05660v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_06-58-10Z_ReasoningErrorsHaveaRegionandaDirectionintheResidu.md
generated_at: 2026-08-06 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the problem of detecting flawed reasoning in large language models by analyzing residual-stream trajectories. It introduces a three‑stream detector that combines motion with two restricted views of location, improving selection accuracy on unseen reasoning benchmarks. The method outperforms displacement‑only baselines and single‑layer probing.

## Key Takeaways
- The detector restores enough state context to interpret motion without full‑state probing, addressing the trade‑off between motion and location information.
- Motion, region, and direction provide complementary signals that together boost reasoning selection accuracy by up to 21% over single‑layer baselines.
- The approach also works on factual completion and fact verification tasks, indicating a broader applicability beyond pure reasoning.

## Context
Trajectory‑based methods aim to capture how model representations evolve across layers while preserving stable token information. By focusing on residual displacements, they can highlight changes that may indicate errors. This work extends those ideas by integrating spatial region cues with directional context.

## Implications
Practitioners can use this detector as a lightweight diagnostic tool for model outputs, enhancing reliability in high‑stakes applications such as automated fact checking and reasoning tasks. The findings suggest that state‑conditioned motion is more informative than static states or decontextualized trajectories alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05660v1)
