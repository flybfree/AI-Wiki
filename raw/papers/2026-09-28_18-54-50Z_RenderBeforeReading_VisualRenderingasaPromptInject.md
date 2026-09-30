---
title: Render Before Reading: Visual Rendering as a Prompt Injection Defense
published: 2026-09-28T18:54:50Z
authors: Jie Zhang, Andrei Baroian, Jan N. van Rijn, Avital Shafran, Florian Tramèr
url: http://arxiv.org/abs/2609.36121v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Render Before Reading: Visual Rendering as a Prompt Injection Defense

## Abstract
Large language models are vulnerable to prompt injection attacks, where third-party adversarial content can hijack the model's behavior. In this paper, we study the role played by the adversarial data's input modality, and identify a systematic asymmetry: multimodal LLMs are more likely to follow adversarial instruction when they appear as text than when the same instruction is delivered through a non-textual channel (e.g., as an image). We hypothesize that this modality gap arises from text-centric instruction tuning, which teaches models to obey textual instructions while treating other modalities mainly as content to parse or describe. We then demonstrate how this gap can be turned into a training-free defense, by rendering all untrusted payloads as typographic images (or audio) before they reach the model. Across ten models and two prompt injection benchmarks (DirectInject and AgentDojo) we show that our defense Pictionary consistently reduces attack success rates even against the strongest adaptive attacks and human red teamers, while largely preserving benign utility. We further show that benign fine-tuning on image-rendered instructions erodes the modality gap, tracing it to the text-centric instruction-tuning distribution.

## Metadata
- **Published**: 2026-09-28T18:54:50Z
- **Authors**: Jie Zhang, Andrei Baroian, Jan N. van Rijn, Avital Shafran, Florian Tramèr
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36121v1)