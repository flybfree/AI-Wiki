---
title: RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory
published: 2026-08-13T15:05:01Z
authors: Jingbo Ji, Lingyi Li, Xilong Cheng, Yuhao Zhou, Wenji Zhang, Yuting Tan, Yunxiao Qin
url: http://arxiv.org/abs/2608.13334v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory

## Abstract
LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction. However, the main bottleneck is not simply storing past experience, but recovering the right set of evidence when relevant information is distributed across many interactions. Existing approaches struggle with this access problem. Full-context methods require noisy long-context search, flat retrieval often returns isolated and incomplete records, and graph-based memory systems can be expensive to construct while compressing rich event context. We introduce RippleMem, a long-term memory system that replaces one-shot retrieval with adaptive associative recollection. Inspired by cue-dependent episodic retrieval and associative completion, RippleMem stores interaction history as cue-rich episodic memory units and organizes them in an event-centric memory graph. Given a query, it first recalls relevant memory anchors through hybrid cues, then expands from these anchors along semantic and structural associations to recover missing supporting evidence. In this way, initially recalled memories serve not only as answer context, but also as cues for completing the evidence needed to answer. Experiments on LoCoMo and LongMemEval-S show that RippleMem achieves the best overall performance across evaluated settings, improving LLM-as-a-Judge accuracy by 3.95% on LoCoMo and up to 11.87% on LongMemEval-S, while reducing graph construction cost by about 30x.

## Metadata
- **Published**: 2026-08-13T15:05:01Z
- **Authors**: Jingbo Ji, Lingyi Li, Xilong Cheng, Yuhao Zhou, Wenji Zhang, Yuting Tan, Yunxiao Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13334v1)