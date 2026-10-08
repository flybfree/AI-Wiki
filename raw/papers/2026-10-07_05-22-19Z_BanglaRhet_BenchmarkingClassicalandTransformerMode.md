---
title: BanglaRhet: Benchmarking Classical and Transformer Models for Rhetorical and Persuasion Detection in Bangla Political Speech
published: 2026-10-07T05:22:19Z
authors: Rohit Kumar Sen, Anik Chowdhury
url: http://arxiv.org/abs/2610.09464v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BanglaRhet: Benchmarking Classical and Transformer Models for Rhetorical and Persuasion Detection in Bangla Political Speech

## Abstract
Political discourse often uses rhetorical and persuasive language to frame narratives, influence public opinion, and mobilize audiences. While Bangla natural language processing has made progress in sentiment analysis and opinion mining, systematic benchmarking of transformer models for fine-grained rhetorical and persuasion technique detection in Bangla political speech remains largely underexplored. This paper presents a benchmark study of transformer-based models for detecting rhetorical form and persuasive intent in Bangla political discourse. Using BanglaRhet, a manually annotated corpus of 30,289 Bangla political speech segments collected from publicly available political news sources, we formulate two supervised single-label classification tasks: rhetorical technique detection (contrast, repetition, exaggeration, metaphor, rhetorical questions) and persuasion technique detection (blame assignment, call to action, unity call, moral, emotional, and logical appeals). We evaluate four transformer-based models, BanglaBERT, BanglaBERT-Base, SahajBERT, and XLM-RoBERTa-Base, against classical TF-IDF baselines. BanglaBERT achieves the highest performance, with 65.40% macro-F1 for rhetorical technique detection and 66.46% for persuasion technique detection, outperforming the best tuned classical baseline by 19.2 and 13.8 macro-F1 points, respectively. Class-level analysis indicates that errors are mainly associated with semantic overlap among labels, figurative language, and class imbalance. The results provide initial benchmark baselines for Bangla rhetorical and persuasion-aware political discourse analysis and highlight the need for context-aware and multi-label modeling.

## Metadata
- **Published**: 2026-10-07T05:22:19Z
- **Authors**: Rohit Kumar Sen, Anik Chowdhury
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09464v1)