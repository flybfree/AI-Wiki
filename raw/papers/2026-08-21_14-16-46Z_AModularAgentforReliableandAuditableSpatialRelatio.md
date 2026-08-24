---
title: A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans
published: 2026-08-21T14:16:46Z
authors: Simon Vincent Abel, Heiko Hillenhagen, Michael Götz, Timo Ropinski, Ayhan Can Erdur, Daniel Santak Wolf
url: http://arxiv.org/abs/2608.21140v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans

## Abstract
Reliable spatial understanding is an important prerequisite for future medical vision-language systems that aim to support radiological report generation and structured image understanding. While modern vision-language models (VLMs) show promising performance on many medical imaging tasks, recent evidence suggests they remain weak in controlled spatial reasoning and often fail to reliably ground spatial relations in image evidence. Given that radiological reasoning hinges on understanding the relative positions of anatomical structures and findings, this spatial weakness poses risks to diagnostic accuracy. We present a modular medical imaging agent for binary spatial relation verification in axial CT slices. Instead of directly predicting spatial answers end-to-end, the system decomposes the task into explicit stages: language parsing, anatomical localization, and deterministic geometric verification. Natural-language queries are converted into structured relation tuples, queried organs are localized with a YOLO-based detector, and the final spatial decision is computed from object centers using deterministic geometric rules. We evaluate the approach on the held-out MIRP spatial QA benchmark and compare it against representative end-to-end VLM baselines. The best-performing hybrid configuration reaches 94.1% accuracy and 94.2% F1, outperforming direct Qwen2-VL prompting by 42.5 percentage points in accuracy, while preserving interpretable intermediate representations and auditable reasoning stages. The results suggest that explicit modular spatial verification can serve as a promising building block for future report-oriented medical imaging agents.

## Metadata
- **Published**: 2026-08-21T14:16:46Z
- **Authors**: Simon Vincent Abel, Heiko Hillenhagen, Michael Götz, Timo Ropinski, Ayhan Can Erdur, Daniel Santak Wolf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21140v1)