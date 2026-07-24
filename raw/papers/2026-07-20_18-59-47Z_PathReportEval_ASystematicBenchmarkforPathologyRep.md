---
title: PathReportEval: A Systematic Benchmark for Pathology Report Generation
published: 2026-07-20T18:59:47Z
authors: Suryakant Singh, Sejuti Majumder, Beatrice Knudsen, Joel Saltz, Prateek Prasanna
url: http://arxiv.org/abs/2607.18448v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PathReportEval: A Systematic Benchmark for Pathology Report Generation

## Abstract
Pathology report generation from whole-slide images (WSIs) is a rapidly growing multimodal learning problem, yet progress is difficult to measure because existing studies use heterogeneous datasets, model settings, visual encoders, and evaluation protocols. Moreover, commonly used natural language generation metrics, including BLEU, ROUGE, and METEOR, primarily reward lexical similarity and often fail to detect clinically consequential errors such as omitted diagnoses, hallucinated findings, or discordant tumor attributes.   We present a standardized benchmark and evaluation framework for pathology report generation. The benchmark evaluates four representative methods across three datasets (TCGA, HistAI, and REG 2025) using three pathology foundation encoders (CONCHv1.5, UNI2-h, and H-Optimus-1). Our framework standardizes preprocessing, feature extraction, training, decoding, and evaluation, enabling fair comparison across models while providing a modular platform for integrating new methods, datasets, and encoders.   A central contribution is the Clinical Report Quality Score (CRQS), a clinically grounded metric for evaluating factual correctness. CRQS maps reference and generated reports into structured clinical attributes and measures four complementary dimensions: clinical fact coverage, key information recall, hallucination rate, and clinical discordance, producing both an overall score and interpretable sub-scores.   Experiments demonstrate that conventional language-generation metrics are weakly aligned with clinical correctness and frequently overestimate report quality. In contrast, CRQS reveals clinically meaningful differences between models and encoders that lexical metrics fail to capture. Together, the benchmark, public plug-and-play framework, and CRQS establish a reproducible foundation for rigorous evaluation of pathology report generation.

## Metadata
- **Published**: 2026-07-20T18:59:47Z
- **Authors**: Suryakant Singh, Sejuti Majumder, Beatrice Knudsen, Joel Saltz, Prateek Prasanna
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18448v1)