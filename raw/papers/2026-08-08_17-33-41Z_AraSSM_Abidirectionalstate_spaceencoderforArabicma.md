---
title: AraSSM: A bidirectional state-space encoder for Arabic masked language modeling
published: 2026-08-08T17:33:41Z
authors: Ahmed Amine Aliane, Hassina Aliane, Nasredine Semmar
url: http://arxiv.org/abs/2608.08256v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AraSSM: A bidirectional state-space encoder for Arabic masked language modeling

## Abstract
Pretrained Transformer encoders such as AraBERT, MARBERT, and CAMeLBERT have become the standard backbone for Arabic natural language understanding, but their self-attention mechanism scales quadratically with sequence length, which limits efficiency on long documents. Mamba, a selective state-space model (SSM), offers linear-time sequence modeling as a competitive alternative to attention, yet no dedicated bidirectional Mamba encoder pretrained specifically for Arabic currently exists. We introduce AraSSM, a bidirectional Mamba encoder pretrained via masked language modeling on a corpus combining Arabic Wikipedia and CulturaX text, trained end-to-end on four consumer-grade NVIDIA RTX 2080Ti GPUs (11GB) over approximately ten days. We evaluate AraSSM by fine-tuning on four established Arabic NLU benchmarks covering sentiment classification (HARD), named entity recognition (ANERcorp), extractive question answering (ARCD), and natural language inference (XNLI-ar), following the per-task evaluation protocol introduced by AraBERT, and report results as mean +/- standard deviation across three fine-tuning seeds. AraSSM matches or exceeds published base-sized Transformer baselines on sentiment classification (96.37 +/- 0.03% accuracy on HARD), is competitive on extractive QA (32.19 +/- 1.07 EM, 63.79 +/- 0.25 F1 on ARCD) and named entity recognition (81.54 +/- 0.30 entity-level F1 on ANERcorp), and trails the base-sized Transformer range on natural language inference (72.83 +/- 0.07% accuracy on XNLI-ar), despite being trained entirely from scratch on consumer hardware rather than large-scale accelerator clusters.

## Metadata
- **Published**: 2026-08-08T17:33:41Z
- **Authors**: Ahmed Amine Aliane, Hassina Aliane, Nasredine Semmar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08256v1)