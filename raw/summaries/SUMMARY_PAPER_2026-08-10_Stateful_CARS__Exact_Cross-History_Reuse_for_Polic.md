---
title: Stateful CARS: Exact Cross-History Reuse for Policy-Constrained LLM Agents
url: http://arxiv.org/abs/2608.08282v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_18-26-25Z_StatefulCARS_ExactCross_HistoryReuseforPolicy_Cons.md
generated_at: 2026-08-10 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Stateful CARS, a method for generating exact samples from a language model conditioned on a validator that changes with observations and actions. It reuses invalidity certificates across histories to prune trajectories, achieving near‑perfect validity probabilities while maintaining i.i.d. outputs and almost‑sure termination.

## Key Takeaways
- Stateful CARS freezes concrete state‑continuation schemas within each attempt and discards any trajectory that contains a certified continuation at a matching abstract state, thereby enforcing exact sampling.
- The method’s acceptance probability matches the valid conditional distribution to within 10⁻¹⁶ at a validity rate of 6×10⁻⁸, whereas naive local decoding can be off by up to 3 %.
- Cross‑history transfer improves sampler steps only in an internal matched‑key ablation (1.27×), indicating that the benefit lies within the algorithm rather than in system architecture.

## Context
Stateful CARS addresses a core challenge in tool‑using language models: ensuring that generated actions remain valid under dynamic validator constraints without sacrificing sampling quality. The work contributes to the growing need for exact, provably correct generation pipelines in AI agents.

## Implications
For practitioners developing autonomous agents, Stateful CARS offers a reliable way to produce high‑quality outputs while respecting evolving policies, potentially reducing costly rejections and improving efficiency. Its theoretical guarantees may inspire future standards for correctness‑first sampling in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08282v1)
