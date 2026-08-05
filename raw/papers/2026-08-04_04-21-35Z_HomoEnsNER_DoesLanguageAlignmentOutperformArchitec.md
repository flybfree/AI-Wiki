---
title: HomoEnsNER: Does Language Alignment Outperform Architectural Complexity in Gujarati Named Entity Recognition?
published: 2026-08-04T04:21:35Z
authors: Chandrakant K. Bhogayata
url: http://arxiv.org/abs/2608.03105v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HomoEnsNER: Does Language Alignment Outperform Architectural Complexity in Gujarati Named Entity Recognition?

## Abstract
Named Entity Recognition (NER) for Gujarati remains underexplored, hindered by the absence of capitalization cues, rich morphology, lexical ambiguity, and free word order. Prior ensemble work has emphasized architectural diversity by combining heterogeneous classifiers, multilingual encoders, or classical sequence models, rather than exploiting language-aligned monolingual pretraining. This study asks whether, for a low-resource, morphologically rich language like Gujarati, a homogeneous ensemble of a single monolingual encoder outperforms such architectural diversity. We propose HomoEnsNER, a homogeneous ensemble of five independently fine-tuned GujaratiBERT models combined via majority voting, evaluated against a single GujaratiBERT baseline and six heterogeneous alternatives, including combinations with MuRIL-base, MuRIL-large, IndicBERT, mBERT, BiLSTM, CRF, and a stacked BiLSTM-CRF-GujaratiBERT architecture. All eight models were trained under a consistent budget and evaluated using entity-level F1 on the Naamapadam Gujarati test split. HomoEnsNER achieved the highest F1 (0.8442), surpassing the baseline (0.8347) and every heterogeneous alternative (lowest: 0.7855), indicating that language alignment is a more effective, budget-conscious ensembling strategy than architectural complexity for low-resource Indian language NER.

## Metadata
- **Published**: 2026-08-04T04:21:35Z
- **Authors**: Chandrakant K. Bhogayata
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03105v1)