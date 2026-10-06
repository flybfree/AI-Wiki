---
title: From Papers to Mechanisms: An Evidence-Grounded Knowledge Substrate for Scientific Language Models
published: 2026-10-05T12:47:15Z
authors: Qiuhui Chen, Yibo Liu, Tao Dai, Jiafan Lu, Zhenglei Zhou, Weimin Zhong
url: http://arxiv.org/abs/2610.06248v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Papers to Mechanisms: An Evidence-Grounded Knowledge Substrate for Scientific Language Models

## Abstract
Scientific language models often access literature through untyped text chunks, which fragment the functional and evidential structure required for mechanism-rich questions. We introduce an evidence-grounded mechanism knowledge substrate that organizes scientific literature into provenance-linked evidence units, role-typed entities, and directed mechanism paths. We instantiate it as MS$^3$, a Material-Sensor-Signal-System schema for conductive-fiber flexible sensors, over 13,689 papers, 131,083 evidence items, and 26,648 mechanism objects. On in-domain and coverage-shift question-answering benchmarks, we compare closed-book generation, Web search, Raw-PDF RAG, and MS$^3$ retrieval across ten language models. MS$^3$ improves macro-averaged scientific correctness. It also improves citation entailment and answer completeness. These results support mechanism substrates as a reliable representation layer for scientific language models and motivate a source-repair workflow in which insufficient MS$^3$ evidence triggers targeted retrieval from its linked papers rather than assuming that a user has already supplied the correct PDFs.

## Metadata
- **Published**: 2026-10-05T12:47:15Z
- **Authors**: Qiuhui Chen, Yibo Liu, Tao Dai, Jiafan Lu, Zhenglei Zhou, Weimin Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06248v1)