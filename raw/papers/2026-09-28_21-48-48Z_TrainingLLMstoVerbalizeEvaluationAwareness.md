---
title: Training LLMs to Verbalize Evaluation Awareness
published: 2026-09-28T21:48:48Z
authors: Usman Anwar, Sahar Abdelnabi, David Krueger
url: http://arxiv.org/abs/2609.36316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training LLMs to Verbalize Evaluation Awareness

## Abstract
Evaluation awareness (EA) can cause large language models (LLMs) to behave differently during audits than in deployment, yet measuring and accounting for EA remains challenging. We introduce verbalization training (VT), a method for making LLMs less reticent about verbalizing evaluation awareness while avoiding to supervise the latent belief itself. VT uses a model's spontaneous verbalizations as evidence that awareness is present and truncates each rollout immediately before the verbalization, producing training prefixes at which the model is presumed to be aware. The model is then trained with an RL objective designed to increase verbalization in a calibrated way. Across Qwen3.6-35B-A3B, Kimi K2.6, and Inkling, VT increases verbalized EA by 2.4-2.9 times and transfers to held-out agentic settings, while measured latent EA and behavior remain largely stable. In a causal experiment, we independently implant meta-knowledge about evaluations through synthetic-document fine-tuning and show that VT-induced verbalizations reflect the richer knowledge acquired by the model.

## Metadata
- **Published**: 2026-09-28T21:48:48Z
- **Authors**: Usman Anwar, Sahar Abdelnabi, David Krueger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36316v1)