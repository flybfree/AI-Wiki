---
title: MAG: MAnifold Guided Semi-Supervised Multi-modal In-Context Learning
url: http://arxiv.org/abs/2608.12724v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_02-10-52Z_MAG_MAnifoldGuidedSemi_SupervisedMulti_modalIn_Con.md
generated_at: 2026-08-13 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MAG, a framework for improving multi-modal few-shot in-context learning by using unlabeled data to guide demonstration selection. It achieves higher performance on eight benchmarks with limited pseudo-labeling budget.

## Key Takeaways
- Relevance score propagation is performed primarily on textual representations, which efficiently identifies high‑impact unlabeled samples for pseudo‑labeling and reduces inference cost.
- The two‑stage strategy first generates a compact set of pseudo‑labels via relevance propagation before selecting the final demonstrations using multi‑modal relevance scores.
- MAG consistently outperforms strong baselines in label‑scarce regimes, showing significant gains even when only a small number of pseudo‑labels are produced.

## Context
Few-shot in-context learning is central to deploying large language models with minimal labeled data. Multi‑modal ICL faces the challenge of selecting diverse and high‑quality demonstrations from abundant unlabeled data, which MAG addresses by treating selection as a semi‑supervised propagation problem on a multi‑modal graph.

## Implications
The method enables cost‑effective adaptation of MLLMs in real‑world applications where labeling is expensive or scarce. Practitioners can leverage the pseudo‑labeling budget to boost performance without retraining, opening new possibilities for rapid task customization across industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12724v1)
