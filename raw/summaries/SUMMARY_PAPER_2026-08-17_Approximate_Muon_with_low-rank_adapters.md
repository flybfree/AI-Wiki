---
title: Approximate Muon with low-rank adapters
url: http://arxiv.org/abs/2608.14492v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_17-07-37Z_ApproximateMuonwithlow_rankadapters.md
generated_at: 2026-08-17 19:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces sMuon, a method that approximates the Muon optimizer’s solution for low‑rank parameterizations by linearizing the problem and solving it with least‑squares using only matrix multiplications. The approach enables LoRA fine‑tuning to benefit from Muon’s pretraining advantages without requiring orthogonal weight updates. Experiments on SFT and ReLoRA show moderate performance gains that vary with model size and evaluation task.

## Key Takeaways
- sMuon replaces the mathematically impossible orthogonalization of low‑rank updates with a linearized least‑squares formulation, making it compatible with LoRA.
- The implementation relies solely on matmul operations, avoiding complex decompositions for efficiency.
- Results indicate that Muon can be applied to low‑rank fine‑tuning, delivering moderate improvements across diverse tasks.

## Context
The Muon optimizer is known for its strong pretraining effects in neural networks, yet its integration with popular PEFT techniques like LoRA has been limited by theoretical constraints. This work bridges the gap by providing a practical approximation that respects low‑rank constraints while leveraging Muon’s benefits, addressing a gap between theory and implementation.

## Implications
For practitioners seeking parameter‑efficient fine‑tuning, sMuon offers a viable alternative to standard LoRA that can capture Muon’s pretraining gains without sacrificing compatibility. The method could become a default choice in pipelines where both efficiency and performance improvements are desired.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14492v1)
