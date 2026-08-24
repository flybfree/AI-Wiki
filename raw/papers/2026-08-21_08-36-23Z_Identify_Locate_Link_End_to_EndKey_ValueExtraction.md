---
title: Identify, Locate, Link: End-to-End Key-Value Extraction from Document Images
published: 2026-08-21T08:36:23Z
authors: A. Said Gurbuz, Ahmed Nassar, Christoph Auer, Maksym Lysak, Lucas Morin, Matteo Omenetti, Tim Strohmeyer, Panagiotis Vagenas, Nikolaos Livathinos, Michele Dolfi, Peter Staar
url: http://arxiv.org/abs/2608.20868v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Identify, Locate, Link: End-to-End Key-Value Extraction from Document Images

## Abstract
Document processing pipelines traditionally cascade optical character recognition (OCR) engines with downstream models for structured information extraction, leading to multi-stage error propagation. We fine-tune SmolDocling, a compact 256M-parameter vision-language model (VLM), to perform end-to-end key-value extraction directly from document images, jointly solving identification, localization, and association in a single pass without OCR preprocessing. We extend DocTags with specialized key, value, region, and link tags, enabling many-to-many relationships in a unified output sequence. To address data limitations, we design an augmentation pipeline combining synthetic form filling and graph-based crops that preserve complete key-value subgraphs. We further introduce a layout-aware evaluation framework extending text matching with spatial bounding box verification. On FUNSD, XFUND, and a large-scale private dataset, our model outperforms larger zero-shot VLM baselines under layout-aware evaluation, while being 27 times smaller than Qwen2.5-VL (7B) and over 5 times faster at inference. The model weights will be released publicly after publication.

## Metadata
- **Published**: 2026-08-21T08:36:23Z
- **Authors**: A. Said Gurbuz, Ahmed Nassar, Christoph Auer, Maksym Lysak, Lucas Morin, Matteo Omenetti, Tim Strohmeyer, Panagiotis Vagenas, Nikolaos Livathinos, Michele Dolfi, Peter Staar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20868v1)