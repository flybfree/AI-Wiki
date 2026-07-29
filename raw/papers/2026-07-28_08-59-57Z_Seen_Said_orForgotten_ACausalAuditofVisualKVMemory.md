---
title: Seen, Said, or Forgotten? A Causal Audit of Visual KV Memory Across Dialog Turns
published: 2026-07-28T08:59:57Z
authors: Hong Chen, Kang Chen, Yuxuan Fan, Bo Wang, Yubo Gao, Yuanlin Chu, Xuming Hu
url: http://arxiv.org/abs/2607.25467v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Seen, Said, or Forgotten? A Causal Audit of Visual KV Memory Across Dialog Turns

## Abstract
Stateful multimodal assistants encode an image once but may answer questions about it many turns later. Attention-guided visual-KV eviction assumes that evidence irrelevant now will remain dispensable, although future questions are unknown. We ask when a visual fact is actually safe to forget and introduce the Causal Visual Memory Audit (CVMA), a paired single-prefill framework that tests what later answers lose when a visual region, the whole image, or prior assistant text becomes unavailable. On VisDial and ConvBench, current attention can rank future-useful regions worse than random even though a diagnostic marginal-utility control shows substantial selection headroom. Aggregate scores hide this failure when later turns do not need vision; controlled and stock-generated histories reveal a second escape route, in which assistant-text KV replaces image KV for facts already stated but not reliably for unstated facts. In the tested stacks, safe forgetting is supported by low future visual dependence or fact-specific verbalization---not by low current attention.

## Metadata
- **Published**: 2026-07-28T08:59:57Z
- **Authors**: Hong Chen, Kang Chen, Yuxuan Fan, Bo Wang, Yubo Gao, Yuanlin Chu, Xuming Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25467v1)