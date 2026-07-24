---
title: What Transfers Under Source Shift? Definitions, Examples, and Fine-Tuning for Climate Disclosure Classification
published: 2026-07-20T13:54:40Z
authors: Guosheng Li, Fenghui Ren, Bin Liu, Chuan Yu, Kaiying Ji, Lin Yue, Jun Shen, Sasa Qian
url: http://arxiv.org/abs/2607.17952v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Transfers Under Source Shift? Definitions, Examples, and Fine-Tuning for Climate Disclosure Classification

## Abstract
Climate disclosure classification is a fundamental task for analysing corporate climate disclosures, yet such disclosures appear in many different sources -- annual reports, press releases, and earnings calls -- that differ in length, purpose, and writing style. Existing evaluations are mostly conducted within a single source, leaving open whether common LLM adaptation strategies remain effective under source shift. We reframe climate disclosure classification as a cross-source adaptation problem and study three widely used adaptation strategies -- definitions, examples, and fine-tuning -- across eleven open- and closed-source LLMs, using two corpora that share the same label space but come from different sources. We find that all strategies bring positive cross-source gains on average, but the strongest in-source strategies are not the strongest cross-source ones: similarity-based retrieval and LoRA fine-tuning gain most in-source but lose most of that advantage under source shift; randomly selected few-shot examples, a weaker in-source baseline, retain their advantage more reliably; definitions transfer most consistently, though only when their granularity matches the target text. Across these strategies, when the source changes, simpler is often safer.

## Metadata
- **Published**: 2026-07-20T13:54:40Z
- **Authors**: Guosheng Li, Fenghui Ren, Bin Liu, Chuan Yu, Kaiying Ji, Lin Yue, Jun Shen, Sasa Qian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17952v1)