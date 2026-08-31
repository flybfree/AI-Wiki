---
title: Embedding Models for Stance-Aware Argument Retrieval
published: 2026-08-28T12:47:45Z
authors: Angelo Sparacino, Francesca Toni, Adam Dejl
url: http://arxiv.org/abs/2608.28283v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Embedding Models for Stance-Aware Argument Retrieval

## Abstract
In computational argumentation, obtaining arguments that explicitly support or attack given claims is a critical precursor to downstream reasoning tasks. When these supporting and attacking arguments are to be retrieved using semantic search methods, they need to be assessed for topic-relevance to the claims of interest as well as for correctness of their (positive or negative) stance towards the claims. In this paper we explore how dense embedding models (hereafter, models), powering modern retrieval pipelines, can serve as the basis of semantic search incorporating this dual assessment. We show experimentally that existing models struggle with asymmetric reasoning, exhibiting a strong bias toward topical overlap while ignoring instructional stance. We also show that correcting this bias via contrastive training triggers a new failure mode where models over-correct, over-fixating on polarity keywords (e.g., "supports" or "refutes") at the expense of the semantic topic. We thus introduce diagnostic word-ablation metrics to quantify this phenomenon and propose a data-centric solution. By implementing a balanced argument curriculum alongside LLM-augmented, stance-inverted arguments, we force the (embedding) models to learn deeper directional logic rather than exploiting superficial lexical shortcuts. Our evaluation demonstrates that, for sufficiently powerful models, this approach can alleviate the observed overcorrection, achieving further improvements in stance-aware argument retrieval.

## Metadata
- **Published**: 2026-08-28T12:47:45Z
- **Authors**: Angelo Sparacino, Francesca Toni, Adam Dejl
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28283v1)