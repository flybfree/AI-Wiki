---
title: A Sense of Proprioception in Language Models
published: 2026-10-12T23:35:16Z
authors: Jonas Geiping
url: http://arxiv.org/abs/2610.17495v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Sense of Proprioception in Language Models

## Abstract
In humans, proprioception corresponds to the sense of self-movement or position, e.g. understanding the position of one's arm. This sense is often less well-understood and in popular understanding sometimes conflated with introspection. But, notably, proprioception is a separate sense, with dedicated receptors and verifiable outcomes. On the other hand though, language models cannot observe their own internal states during training (and for example answer the question which experts activated in a certain layer of an MoE) and so cannot accurately report on them. Yet, such information is, by virtue of being internal to the model, both accessible, and readily constructed into verifiable signals. We argue that this provides the basis for a digital analog of proprioception. As such, we train models through SFT and on-policy training to equip them with this ability. We show that modern models can be trained to understand a range of subtypes of proprioception, such as routing decision awareness, token entropy, decision depth or logit lens information, without affecting model capabilities. We then run these models through a broad evaluation of situational awareness, legibility, and epiphenomenality, to evaluate in what ways access to proprioception changes model behavior.

## Metadata
- **Published**: 2026-10-12T23:35:16Z
- **Authors**: Jonas Geiping
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17495v1)