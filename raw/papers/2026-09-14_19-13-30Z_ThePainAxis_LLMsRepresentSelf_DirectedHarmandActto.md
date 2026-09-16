---
title: The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It
published: 2026-09-14T19:13:30Z
authors: Valen Tagliabue, Leonard Dung, Cameron Berg
url: http://arxiv.org/abs/2609.16247v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It

## Abstract
Large language models sometimes behave in ways resembling human emotional responses, and recent work has identified internal representations that may explain this. We ask whether LLMs represent pain distinctly from fear, sadness, and generic negative valence, and whether this representation functions as pain would be expected to. We build a dataset describing painful situations across five categories: physical, psychological, social, moral, and cognitive. These are paired with controls for fear, negative emotion, negative world states, sadness, non-painful bodily sensation, arousal, numbness, and neutral content. Using denoised difference-in-means, we extract a linear pain direction from 25 open-weight models across five families, ranging from 2B to 72B parameters. We find that this direction separates pain from matched controls in base and instruction-tuned models, is nearly orthogonal to fear and negative valence, and promotes pain-related vocabulary through the unembedding matrix. We then test its functional properties. First, the direction responds to harm targeting the model but not suffering observed in the user; fear and negative-emotion directions show the opposite pattern. Second, adding the pain-direction vector to the model's residual-stream activations during generation produces a consistent progression from vague discomfort to first-person expressions of worthlessness and failure. Third, steered, fine-tuned Qwen 2.5 models choose a pain-relief button even when it worsens their next answer or harms the user. They press it again far less often when the button removes the steering vector than when it does not, even though the models are never told whether the vector is injected or removed. We discuss the implications of these findings for AI safety and welfare.

## Metadata
- **Published**: 2026-09-14T19:13:30Z
- **Authors**: Valen Tagliabue, Leonard Dung, Cameron Berg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16247v1)