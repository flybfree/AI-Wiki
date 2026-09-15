---
title: Mirror, Mirror on the Wall: Prompt Echoing in Small Instruct Language Models
published: 2026-09-14T05:06:21Z
authors: Inez Okulska, Bartosz Naskręcki, Jan Piotrowski, Tomasz Steifer
url: http://arxiv.org/abs/2609.15045v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mirror, Mirror on the Wall: Prompt Echoing in Small Instruct Language Models

## Abstract
Prompt echoing is a recognized failure mode of instruct language models, in which a model instead of generating a response, mirrors the provided prompt, even though it did not receive a specific instruction to do so. Is this phenomenon a sign of the model leaking the content of its training dataset, or is it rather caused by a misaligned behavior of the internal induction/copying mechanisms? We investigate prompt echoing small language models from different families (Gemma, Llama, Qwen, SmolLM and OLMo) and show that echoing prompts are likely to have partial overlap with the training dataset but the phenomenon is primarily driven by the model's induction heads.

## Metadata
- **Published**: 2026-09-14T05:06:21Z
- **Authors**: Inez Okulska, Bartosz Naskręcki, Jan Piotrowski, Tomasz Steifer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15045v1)