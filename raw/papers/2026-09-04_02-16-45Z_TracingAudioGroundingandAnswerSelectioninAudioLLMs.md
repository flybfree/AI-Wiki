---
title: Tracing Audio Grounding and Answer Selection in Audio LLMs
published: 2026-09-04T02:16:45Z
authors: Hyebin Cho, Suho Yoo, Jihoo Jung, Joon Son Chung
url: http://arxiv.org/abs/2609.04637v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tracing Audio Grounding and Answer Selection in Audio LLMs

## Abstract
Audio Large Language Models (Audio LLMs) have advanced in audio understanding, yet they can still predict the answer by reasoning from textual cues or linguistic priors rather than the provided audio. A common remedy is to train models on data whose answers cannot be inferred from text alone. This approach can improve performance, but what changes within the model remains unclear. In this paper, we ask what must happen inside the model for the audio to actually determine the answer. Our findings are threefold. (1) Replacing the audio with silence or unrelated audio causes substantially larger performance degradation in the trained model than in the pretrained model. (2) Acoustic information most strongly shapes the model's representations of the answer choices in early-to-middle layers, while training mainly increases the influence of audio information on the final prediction in middle-to-late layers. (3) The weights learned during training have their largest impact in specific layer bands. Together, these results provide a mechanistic account of how training strengthens the use of acoustic evidence in Audio LLMs.

## Metadata
- **Published**: 2026-09-04T02:16:45Z
- **Authors**: Hyebin Cho, Suho Yoo, Jihoo Jung, Joon Son Chung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04637v1)