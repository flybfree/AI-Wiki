---
title: Beyond Accuracy: Robustness, Cost, and Governance Trade-offs for Vision-Language Models in Templated Document Extraction
published: 2026-09-14T15:10:33Z
authors: Kushal Patel, Pushkal Shrivastava, Mackenzie Lees, Qirui Lu, Bhargobjyoti Saikia, Liying Li, Junlin Jiang
url: http://arxiv.org/abs/2609.15706v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Accuracy: Robustness, Cost, and Governance Trade-offs for Vision-Language Models in Templated Document Extraction

## Abstract
Vision-language models (VLMs) are increasingly used to extract structured fields from business documents, yet most evaluations report accuracy on clean benchmarks and offer little guidance to practitioners choosing an approach for a given task complexity. We address this gap with a measurement-grounded study and an open-source release. Across eleven systems (three commercial, two reasoning, five open-source VLMs in pretrained and fine-tuned form, and a non-LLM OCR->regex floor) scored on a 750-document held-out pool of synthetic checks, fine-tuning on 3K samples lifts the best open-source VLMs above F1 0.98-above every zero-shot commercial system on this task-while GPT-5 leads the commercial pool on F1 and Claude Sonnet 4.5 collapses on Date. To turn these measurements into actionable choices, we introduce a practitioner-oriented selection framework that maps a task profile (quality, latency, governance, volume) to a recommended approach via filtering and total-cost minimization, illustrated on a hypothetical mid-volume document-extraction scenario.

## Metadata
- **Published**: 2026-09-14T15:10:33Z
- **Authors**: Kushal Patel, Pushkal Shrivastava, Mackenzie Lees, Qirui Lu, Bhargobjyoti Saikia, Liying Li, Junlin Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15706v1)