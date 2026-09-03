---
title: LeakageBench: Document-Level Leakage Risk for Redacting Personally Identifiable Information in Document Images
published: 2026-09-02T07:21:24Z
authors: Vishnu Prasad Vijaya Kumar, Santhosh Venkatesh, Ivan P. Yamshchikov
url: http://arxiv.org/abs/2609.02207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LeakageBench: Document-Level Leakage Risk for Redacting Personally Identifiable Information in Document Images

## Abstract
Real-world personally identifiable information (PII) redaction often operates on document images---scans, screenshots, and PDF renderings---where OCR errors, layout structure, and visual noise determine whether sensitive information is actually removed. Existing PII benchmarks are mostly text-centric and do not measure document-level redaction risk: a page remains unsafe if even one identifier is missed. We introduce LeakageBench, a challenge set of 500 document images with 11,954 GDPR-aligned PII annotations spanning direct identifiers, linkage keys, and contextual re-identification surfaces. We evaluate generic OCR pipelines, commercial and task-adapted OCR-dependent detectors, and OCR-free vision-language models using entity-level F1, group-wise leakage, and document-level leakage metrics. Code Interpreter raises GPT-5.5 localization F1 from 0.090 to 0.249, but critical page-level leakage remains 0.968. These results show that stronger detection and tool assistance improve localization without making most pages safe for release. LeakageBench provides a diagnostic benchmark for high-recall, spatially grounded PII redaction in document images.

## Metadata
- **Published**: 2026-09-02T07:21:24Z
- **Authors**: Vishnu Prasad Vijaya Kumar, Santhosh Venkatesh, Ivan P. Yamshchikov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02207v1)