---
title: When Does Explicit View Routing Work? A Controlled Study of Multi-View Graph-Text Alignment
published: 2026-07-29T23:49:37Z
authors: Xiao Yue, Guangzhi Qu
url: http://arxiv.org/abs/2607.27530v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Does Explicit View Routing Work? A Controlled Study of Multi-View Graph-Text Alignment

## Abstract
Graph-text retrieval typically maps a graph and its description to a single embedding, even when a query concerns only one semantic aspect, such as a class label or molecular property. Multiple heads can separate these aspects, but a change in the query head may alter retrieval even when the wrong text is sent to that head. Such behavior demonstrates architectural channelization, not necessarily semantic routing. We examine the conditions under which this distinction can be resolved. Our controlled version of MV-GTA uses deterministic, verifiable text segments; isolated text encoders; view-specific graph heads; and relevance derived from external labels or RDKit descriptors. Correct routing and per-sample derangements form a causal test of whether retrieval depends on content. On BBBP and BACE, correct routing improves label and property nDCG by 0.305 to 0.685 over deranged training. The expected graph head exceeds the best wrong head by 0.303 to 0.453. Topology does not specialize consistently across the two datasets. In a matched three-seed comparison, one joint model obtains mean topology, label, and property nDCG of 0.720/1.000/0.877; three separately trained Single specialists obtain 0.633/0.976/0.859. Property paraphrase augmentation also improves unseen-template nDCG by 0.140 and 0.147 over a matched-exposure canonical control. Consistency and hard-template extensions, however, reduce canonical retrieval in some settings. The evidence is therefore limited to explicit, externally grounded label and property routing and observed multi-interface consolidation. It does not establish free-form routing, consistent three-view specialization, statistical equivalence to specialists, or superior downstream prediction.

## Metadata
- **Published**: 2026-07-29T23:49:37Z
- **Authors**: Xiao Yue, Guangzhi Qu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27530v1)