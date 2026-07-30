---
title: Latent-IM: Latent Interaction Management for Speech LLMs
published: 2026-07-29T13:56:28Z
authors: Adar Avsian, Atahan Dokme, Tony Woo, Larry Heck
url: http://arxiv.org/abs/2607.26928v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent-IM: Latent Interaction Management for Speech LLMs

## Abstract
Classical spoken dialogue systems often separated dialogue management from response realization: a policy selected the next dialogue action, and a generation component expressed that action. As dialogue systems shift toward LLMs, this decomposition has largely disappeared into the model's hidden representations. We ask whether an LLM-internal analogue of state estimation and action control can be recovered for conversational moves such as acknowledging, checking, querying, explaining, and replying. We formulate move control as two coupled problems: selection, predicting the appropriate next move from the dialogue context, and realization, causally producing a chosen move at generation time. We introduce Latent-IM, an internal dialogue-management framework that provides a general interface for choosing and deploying conversational moves under different objectives. Here, we use this control to reproduce human move choices, improving average end-to-end move accuracy by 12.5 points over the unsteered backbone while performing comparably to fine-tuning.

## Metadata
- **Published**: 2026-07-29T13:56:28Z
- **Authors**: Adar Avsian, Atahan Dokme, Tony Woo, Larry Heck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26928v1)