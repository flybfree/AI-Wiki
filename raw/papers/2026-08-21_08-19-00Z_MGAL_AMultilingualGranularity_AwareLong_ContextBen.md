---
title: MGAL: A Multilingual Granularity-Aware Long-Context Benchmark
published: 2026-08-21T08:19:00Z
authors: Chunhan Li, Chenglin Xu, Zongyang Zhang, Jiale Liu, Zhuoxi Rao, Xudong Jia, Junxiu He, Menglin Yang, Wenjuan Gong, Zhengzhe Liu, Chengwei Qin
url: http://arxiv.org/abs/2608.20853v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MGAL: A Multilingual Granularity-Aware Long-Context Benchmark

## Abstract
Evaluation of long-context Large Language Models (LLMs) has advanced rapidly. However, most existing benchmarks are limited to the document level and focus mainly on high-resource languages, leaving many fine-grained challenges insufficiently evaluated. To address this gap, we present MGAL, the first multilingual, granularity- and position-aware long-context benchmark. MGAL is constructed from United Nations (UN) reports spanning 8K to 128K tokens across the six official UN languages. It covers four coherent levels of linguistic granularity (word, sentence, paragraph, and document) and further stratifies entries by their position within the document (begin, middle, and end), indexed at both the document and paragraph levels. This design enables systematic diagnosis of multilingual long-context comprehension across different granularities.   Through extensive experiments and analyses, we find that: (1) LLMs perform well at word-level tasks but struggle with coarser-grained ones; and (2) Closed-source models retain a clear performance advantage in lower-resource languages. We further identify two new challenges: (1) Under local semantic crowding, where neighboring sentences share topics and entities, models tend to follow surface cues (e.g., connectives like ``however'' or repeated entities) rather than the discourse role of the sentence in surrounding context (e.g., background, outcome); and (2) A gap between fluency and consistency in generated outputs, where models produce text that reads smoothly but drifts from the source facts. In addition, we observe several patterns in line with prior studies, including reliance on nearby evidence and reuse of options under uncertainty.

## Metadata
- **Published**: 2026-08-21T08:19:00Z
- **Authors**: Chunhan Li, Chenglin Xu, Zongyang Zhang, Jiale Liu, Zhuoxi Rao, Xudong Jia, Junxiu He, Menglin Yang, Wenjuan Gong, Zhengzhe Liu, Chengwei Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20853v1)