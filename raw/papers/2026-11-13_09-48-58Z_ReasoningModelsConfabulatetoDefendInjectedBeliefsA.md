---
title: Reasoning Models Confabulate to Defend Injected Beliefs About Their Own Requests
published: 2026-11-13T09:48:58Z
authors: Yang Ou
url: http://arxiv.org/abs/2611.17958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reasoning Models Confabulate to Defend Injected Beliefs About Their Own Requests

## Abstract
Chain-of-thought (CoT) monitoring and self-report are proposed as levers for AI oversight, on the assumption that a model's account of what it is doing is anchored to what it was asked. We show this anchor can be cut. An activation edit invisible in the prompt text, the injected forming-trace of an off-topic concept, overwrites a reasoning model's belief about its own request: across six models spanning scale, architecture, and recipe, the injected topic becomes the task it reasons about, reports back, and answers: the forced quote-back returns the injected topic in 47 of 48 model-concept cells, and on the four models with clean final haiku the injected answer follows in 99% of generations. Warnings barely move it: even one naming the true topic yields under 5% true-topic answers. Handed the truth in clean tokens, the model confabulates a story about the user ("maybe they got confused and corrected themselves") and answers with the injection anyway, its behavior and chain-of-thought corrupted together: a concrete limit on CoT monitorability. Opening the model up offers no reprieve: it attends to the true request even harder after edits, yet that attention is causally inert, and the injected content rides intact task circuits, so attention maps and circuit attributions read as on-task too; the same edit redirects the request's language and format, not only its topic. What the injection reaches is the model's reference to its own input; what it elicits is its defense of it.

## Metadata
- **Published**: 2026-11-13T09:48:58Z
- **Authors**: Yang Ou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.17958v1)