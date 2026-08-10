---
title: LitTraceQA: A Benchmark for Multi-Stage Grounding and Verification in Scientific Question Answering
published: 2026-08-07T16:11:52Z
authors: Xuye Liu, Yimu Wang, Peng Shi, Bo Xue, Xiangrui Ke, Songcheng Cai, Kath Choi, Di Wu, Freda Shi, Krzysztof Czarnecki
url: http://arxiv.org/abs/2608.07370v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LitTraceQA: A Benchmark for Multi-Stage Grounding and Verification in Scientific Question Answering

## Abstract
Scientific literature is increasingly used as a knowledge source for language models, retrieval-augmented generation systems, and research assistants, but answering research questions from papers requires more than fluent generation. A reliable system must identify the relevant papers, locate the concrete evidence that supports the answer, and produce a response that is faithful to that evidence. We present LitTraceQA, a benchmark for literature-grounded question answering over scientific papers. Given a research question and a metadata pool of papers, a system must return three connected outputs: canonical paper identifiers, supporting evidence locations, and answers in one or more requested formats, including free-form text, multiple-choice answers, and structured tables. LitTraceQA targets evidence types common in scientific reading: tables, figures, text spans, equations or algorithms, and citation contexts. The public development split contains 55 examples, including 26 hidden-source single-paper questions and 29 multi-paper questions, and provides gold papers, evidence annotations, and answers for local validation. We also analyze a larger final annotation collection with 4,978 unique-question records over 4,859 unique gold papers. By evaluating paper retrieval, evidence grounding, and answer accuracy separately, LitTraceQA provides a testbed for scientific QA systems that produce verifiable answers rather than unsupported summaries.

## Metadata
- **Published**: 2026-08-07T16:11:52Z
- **Authors**: Xuye Liu, Yimu Wang, Peng Shi, Bo Xue, Xiangrui Ke, Songcheng Cai, Kath Choi, Di Wu, Freda Shi, Krzysztof Czarnecki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07370v1)