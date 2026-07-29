---
title: Detecting CSAM Text-to-Image LoRAs From Weights
published: 2026-07-28T14:12:52Z
authors: David Demitri Africa, Cate Heine, Nadine Staes-Polet, Kimberly Mai
url: http://arxiv.org/abs/2607.25750v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Detecting CSAM Text-to-Image LoRAs From Weights

## Abstract
Low-rank adaptation (LoRA) fine-tuning has made it cheap and easy to customize open-weight image generation models for specific tasks, including the production of child sexual abuse material (CSAM). Existing moderation relies on metadata or generated outputs, but metadata can be deceptive and generating outputs may itself be unacceptable or illegal. We show that a safer signal lives in the weights. The top-left singular vectors of a LoRA's updates form a compact, inference-free fingerprint ($u_1$) of its strongest learned change. Using human-subject age as a benign proxy for CSAM, we find that $u_1$ identifies what a LoRA was trained on, generalizes across base models, and abstains on unrelated benign content. The signal is robust to additive weight noise, rescaling, and precision reduction. These results indicate that harmful LoRAs could be screened directly from their weights without relying on metadata or generating harmful outputs.

## Metadata
- **Published**: 2026-07-28T14:12:52Z
- **Authors**: David Demitri Africa, Cate Heine, Nadine Staes-Polet, Kimberly Mai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25750v1)