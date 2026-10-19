---
title: AuditKIT: A Unified Evaluation Spine for Benchmarking, Judging, and Comparing Large Language Models and Agentic Systems
published: 2026-10-15T18:05:10Z
authors: Shreeyans Arora, Utsav Avaiya, Zera Lyngkhoi, Hem Gosalia, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
url: http://arxiv.org/abs/2610.22511v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AuditKIT: A Unified Evaluation Spine for Benchmarking, Judging, and Comparing Large Language Models and Agentic Systems

## Abstract
Evaluating language models and agents requires combining benchmark accuracy, judge-based assessment, runtime performance, tool-use behavior, and retrieval quality. Differences in interfaces, metric semantics, and trace formats complicate these comparisons and can hide failures in agentic workflows. We present AuditKIT, a source-available evaluation library that records these measurements in one result representation, with direction-aware metric contracts, configuration fingerprints, and extensible metrics and backends. For agents, it provides turn-aware tool-call matching, separates parallel from sequential execution, and distinguishes verified task outcomes from trajectory-level diagnostics. Missing or unobservable evidence is marked unscored rather than counted as failure. For retrieval-augmented generation, it combines ranked retrieval metrics, judged grounding, and deterministic evidence checks. Seven case studies spanning model comparison, serving runtimes, retrieval, tool calling, and interoperability show how answer extraction, runtime behavior, and metric selection change evaluation outcomes.

## Metadata
- **Published**: 2026-10-15T18:05:10Z
- **Authors**: Shreeyans Arora, Utsav Avaiya, Zera Lyngkhoi, Hem Gosalia, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22511v1)