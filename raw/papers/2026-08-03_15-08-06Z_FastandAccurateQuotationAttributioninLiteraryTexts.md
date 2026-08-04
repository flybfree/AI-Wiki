---
title: Fast and Accurate Quotation Attribution in Literary Texts
published: 2026-08-03T15:08:06Z
authors: Gaspard Michel, Hugo Attali, Elena V. Epure
url: http://arxiv.org/abs/2608.02359v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast and Accurate Quotation Attribution in Literary Texts

## Abstract
Attributing quotations to their speakers in literary texts remains an open challenge. Standard methods, which independently predict a speaker mention for each quotation, are efficient but still limited in accuracy. In contrast, large language model (LLM) approaches achieve strong performance, but their computational cost limits their use in large-scale literary analysis. We propose an encoder-based efficient formulation that resolves multiple quotation attributions within a shared, large context window. Using our new formulation, \textit{joint scoring}, we report state-of-the-art (SOTA) performance on the Project Dialogism Novel Corpus (PDNC), comprising more than 35,000 manually annotated quotations from 22 English novels. Our best model reaches 94.5\% overall attribution accuracy while processing novels $20\times$ faster than comparable standard methods and more than $1000\times$ faster than LLM-based approaches on an A100 GPU. An analysis of models' representations suggests that joint scoring improves on challenging attribution examples by preserving long-range anaphora resolution signal, an information that we found already present in pretrained encoders. To facilitate adoption, we release ModernBookNLP, a modified fork of BookNLP that replaces its quotation attribution model with our best system available at https://github.com/gasmichel/ModernBookNLP_QA/.

## Metadata
- **Published**: 2026-08-03T15:08:06Z
- **Authors**: Gaspard Michel, Hugo Attali, Elena V. Epure
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02359v1)