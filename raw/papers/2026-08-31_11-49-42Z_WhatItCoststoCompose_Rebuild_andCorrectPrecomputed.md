---
title: What It Costs to Compose, Rebuild, and Correct Precomputed Memory
published: 2026-08-31T11:49:42Z
authors: Asa Shepard
url: http://arxiv.org/abs/2608.30647v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What It Costs to Compose, Rebuild, and Correct Precomputed Memory

## Abstract
Language models can answer from precomputed memory, a model's saved reading of a body of material, reused across requests instead of read again at each. This paper maps where that practice preserves correctness and the conditions under which it fails. Across experiments on Llama-3.1-8B-Instruct using both saved key-value caches and trained compressions of them, precomputed memory degrades when assembled from separately prepared parts, stays current only through rebuilds costing a large fraction of full preparation in our measurements, and ignores corrections served beside it conditional on phrasing. If precomputed memories can be served alongside one another, be cost-efficiently rebuilt, and be superseded by new information arriving in real-time, they can serve as a way to avoid re-feeding context to a model over repeated queries. The implication of our results for a deployed system that deals with a variety of queries is that precomputed memories are best rebuilt on the cadence at which new information changes what the memory was originally computed from. Both warm-rebuilding trained compressions of key-value caches and serving specifically-phrased updates beside a memory, as pasted text or injected cache state, show particular promise for keeping precomputed memories current, the latter as an interim measure between rebuilds, and we measure the cost and name the remaining questions associated with each.

## Metadata
- **Published**: 2026-08-31T11:49:42Z
- **Authors**: Asa Shepard
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30647v1)