---
title: Approximate Muon with low-rank adapters
url: http://arxiv.org/abs/2608.14492v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_17-07-37Z_ApproximateMuonwithlow_rankadapters.md
generated_at: 2026-08-16 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces sMuon, a lightweight approximation of the Muon optimizer that works within the low‑rank setting used by LoRA. By linearizing the relaxed Muon objective and solving it via least squares using only matrix multiplications, sMuon achieves moderate performance gains across SFT and ReLoRA pretraining experiments. The results show that integrating Muon with low‑rank adapters is feasible despite earlier mathematical constraints.

## Key Takeaways
- LoRA’s low‑rank weight updates cannot be orthogonalized with Muon’s gradient‑based approach, which previously prevented direct combination of the two methods.
- The authors approximate the solution to a relaxed Muon objective through linearization and least squares, avoiding complex decomposition routines and relying solely on matmul operations for efficiency.
- sMuon delivers moderate performance improvements over baseline LoRA fine‑tuning across multiple model sizes and evaluation tasks.

## Context
Parameter‑efficient fine‑tuning (PEFT) methods such as LoRA have become standard for adapting large models with minimal compute. While Muon offers attractive training dynamics, its orthogonalization requirement clashes with the low‑rank parameterization of LoRA, limiting practical adoption. This work bridges that gap by providing a computationally cheap alternative.

## Implications
Practitioners seeking efficient fine‑tuning can now integrate Muon’s benefits without sacrificing speed or memory usage. The method opens doors for research exploring hybrid optimizers and could be adopted in industry pipelines where rapid iteration is essential, ultimately enhancing model adaptation capabilities at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14492v1)
