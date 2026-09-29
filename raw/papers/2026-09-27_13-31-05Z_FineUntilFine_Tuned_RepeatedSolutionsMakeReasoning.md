---
title: Fine Until Fine-Tuned: Repeated Solutions Make Reasoning Fragile
published: 2026-09-27T13:31:05Z
authors: Ely Sheikh
url: http://arxiv.org/abs/2609.33559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine Until Fine-Tuned: Repeated Solutions Make Reasoning Fragile

## Abstract
Recipes such as s1 and LIMO teach a model to reason with little data by showing it the same thousand or fewer worked solutions many times over. Judged when that training ends, the repetition looks harmless. But reasoning models are often trained again, and we find that repetition leaves their reasoning fragile to that next stage, even when the stage has nothing to do with reasoning. We fine-tuned Qwen3.5-9B-Base on its own correct solutions to competition math problems, either drilling a few hundred of them about eight times each or showing many more once; with the same amount of training, both solve about 95% of held-out problems. A single pass of ordinary instruction tuning leaves the once-trained model where it was, while the drilled one falls to 86.0%, and harsher later stages take it to 59.3% or below. A third model that visited the drilled problems just as often, with a new solution at every visit, was unharmed, so the damage comes from seeing the same texts again rather than from having few problems. The break recurs with a stronger model's traces, in further training runs and on other models and tasks. It is also cheap to undo: the reasoning is suppressed rather than erased, and five updates of reasoning training bring almost all of it back, as does brief training on the reasoning format with almost no mathematics. Fresh solutions prevented the damage, and so did replaying 6.25% of the original solutions in a gentler later stage, so our claim concerns later training without such replay. Sharpening alone does not explain the break, since a model sharpened three-quarters as much without repetition was unharmed. On a skill the base model could not perform within a token budget, repetition mainly cost learning.

## Metadata
- **Published**: 2026-09-27T13:31:05Z
- **Authors**: Ely Sheikh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33559v1)