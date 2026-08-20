---
title: DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering
published: 2026-08-19T14:53:53Z
authors: Xujia Wang, Yizhe Zhang, Bin Xu, Lei Hou, Juanzi Li
url: http://arxiv.org/abs/2608.18988v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering

## Abstract
Retrieve-then-generate pipelines are commonly used to produce deep-research answers for open-ended questions, but retrieval alone is insufficient: LLMs must organize noisy and fragmented evidence into comprehensive, well-cited answers. We refer to this process as evidence synthesis. However, direct generation often underuses evidence, misaligns citations, and collapses diverse information into shallow summaries, exposing an evidence synthesis gap between retrieval and generation. Thus, we propose DeepWeaver, a novel framework that weaves noisy retrieved evidence into comprehensive answers by maintaining Thought Block Chains (TBCs), a structured representation that groups claims, salient information, keywords, and supporting evidence. DeepWeaver uses subordinate TBCs to inspect residual evidence, commit TBC revisions, and discover new claims before final generation. We evaluate DeepWeaver on open-ended QA over both knowledge bases and the web, and introduce LoQA, a high-density benchmark for evidence synthesis. Across multiple LLMs, DeepWeaver improves content sufficiency, citation grounding, and detail preservation on LoQA, while achieving deeper insights and higher citation quality on DeepResearch Bench. These results show that evidence weaving is an effective mechanism for bridging retrieval and generation in open-ended QA. Our code is available at https://github.com/KlozeWang/DeepWeaver.

## Metadata
- **Published**: 2026-08-19T14:53:53Z
- **Authors**: Xujia Wang, Yizhe Zhang, Bin Xu, Lei Hou, Juanzi Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18988v1)