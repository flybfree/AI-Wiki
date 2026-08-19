---
title: Which Source Wins? Task-Dependent Reliance in Vision-Language Models
published: 2026-08-17T23:38:14Z
authors: Rodela Ghosh, Aviral Gupta, Guangjing Wang
url: http://arxiv.org/abs/2608.17205v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Which Source Wins? Task-Dependent Reliance in Vision-Language Models

## Abstract
Vision-language models (VLMs) combine images and text, but when the two conflict and one becomes harder to read, it is unclear how a model shifts its reliance between them. We study this modality reallocation with a controlled setup: we degrade either the image or the text across four levels of legibility while keeping the other clean, and track how the model's preference changes. We build conflicts from GSM8K and SVAMP by pairing the rendered image of one arithmetic problem with the text of another, so the two sources support different answers. We also introduce ChartQA-Conflict, a manually reviewed benchmark of 229 chart-report conflicts with matched chart and table-image representations. We evaluate six open-weight VLMs using both generated answers and a length-normalized conditional log-likelihood margin. On GSM8K and SVAMP, five of six models shift more strongly away from degraded text than from degraded images. On ChartQA-Conflict, all six likelihood-scored models exhibit the opposite pattern, shifting more strongly away from the degraded visual source. This reversal persists after calibrating for unimodal accuracy loss and after replacing charts with plain table images. Two frontier API models, GPT-5.6-Luna and Gemini-3.5-Flash, behaviorally replicate the ChartQA-Conflict reversal, with GPT-5.6-Luna also matching the arithmetic direction. These results show that modality reliance in VLMs is not fixed, but varies across tasks, evidence structures, models, and evaluation settings. The source code is available at https://github.com/Ro-netizen004/multimodal-arbitration-artifact.

## Metadata
- **Published**: 2026-08-17T23:38:14Z
- **Authors**: Rodela Ghosh, Aviral Gupta, Guangjing Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17205v1)