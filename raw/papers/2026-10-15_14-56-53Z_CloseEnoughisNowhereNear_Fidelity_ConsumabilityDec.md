---
title: Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches
published: 2026-10-15T14:56:53Z
authors: Adam Deng, Shicheng Liu, Yada Zhu
url: http://arxiv.org/abs/2610.22016v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches

## Abstract
Multi-agent LLM systems communicate in text, which is lossy and wasteful: the sender throws away the reading it already did. A growing literature instead transmits the KV cache, the natural carrier of that reading. We study the most appealing form of the idea: both models stay frozen and the sender's cache is substituted for the reader's with nothing trained. It does not work, and the obstruction belongs to the reader. A frozen transformer reads only caches close to the one it would have written itself, a region we call its tolerable set. We show that geometric similarity to that cache does not predict whether the reader can use it, and the failure is not gradual, so a more faithful substitute is not the remedy it appears to be. We explain this phenomenon with competitive attention. Experimentally, we test eight diverse substitution methods against two measured anchors: an uninformative cache baseline and the reader's own accuracy from having read the passage. All sit at the baseline. That turns a long tail of separate negative results into one outcome with a stated condition for overturning it. A different design does work: if the reader keeps its own cache and attends over the sender's as extra context, adapting only its queries, it beats its own baseline, and also clears the baseline with eight senders pooled where undirected attention over the same union falls below it. We offer this as a characterization on one probe, not a leaderboard claim. Our central contribution is a redirection: pursuing faithful substitute caches is the wrong target; adding a cache to what the reader already has is the promising one.

## Metadata
- **Published**: 2026-10-15T14:56:53Z
- **Authors**: Adam Deng, Shicheng Liu, Yada Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22016v1)