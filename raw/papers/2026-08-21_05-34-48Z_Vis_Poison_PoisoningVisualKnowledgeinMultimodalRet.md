---
title: Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation
published: 2026-08-21T05:34:48Z
authors: Rujin Liang, Zhongpu Chen, Yuhao Lei, Xin Miao
url: http://arxiv.org/abs/2608.20756v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation

## Abstract
While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language model (MLLM) generation. Unlike prior attacks that rely on altering textual metadata, we introduce Vis-Poison, a novel visual knowledge poisoning attack where the poisoned image itself is the attacker-controlled payload, without manipulating captions, summaries, metadata, or other associated text. Specifically, this attack is instantiated through an automated multi-agent method that constructs visually plausible poisoned images. To assess its impact, we evaluate Vis-Poison across two representative multimodal RAG pipelines, four embedding models, and six generation models. Empirically, Vis-Poison achieves an end-to-end attack success rate of 40.16\% to 65.40\% against 30k-entry multimodal knowledge bases in \emph{black-box} settings. Moreover, Vis-Poison remains effective against various MLLMs that can answer correctly from parametric knowledge alone, with an average success rate above 60\%. Code and data are available at https://github.com/SWUFE-DB-Group/Vis-Poison.

## Metadata
- **Published**: 2026-08-21T05:34:48Z
- **Authors**: Rujin Liang, Zhongpu Chen, Yuhao Lei, Xin Miao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20756v1)