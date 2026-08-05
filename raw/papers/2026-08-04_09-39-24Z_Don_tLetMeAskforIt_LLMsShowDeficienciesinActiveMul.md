---
title: Don't Let Me Ask for It: LLMs Show Deficiencies in Active Multi-Turn Information Acquisition for Abductive Inference
published: 2026-08-04T09:39:24Z
authors: Shahrukh Mohiuddin, Chalamalasetti Kranti, Sherzod Hakimov, David Schlangen
url: http://arxiv.org/abs/2608.03388v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Don't Let Me Ask for It: LLMs Show Deficiencies in Active Multi-Turn Information Acquisition for Abductive Inference

## Abstract
Abductive reasoning requires forming hypotheses that explain observed evidence and revising them as new evidence becomes available. While large language models (LLMs) are often evaluated on whether they solve abductive reasoning tasks correctly, less is known about how they acquire evidence, update their hypotheses, and decide when to stop. We introduce Alien Abduction game, an interactive probe for studying these behaviours under different interaction modes. The modes vary in whether evidence is provided upfront or across turns, and whether queries are selected by the model or examples are provided by the oracle. Across models, providing evidence upfront leads to higher success rates than distributing it across turns. In multi-turn settings, some models commit before using the available evidence, while others exhaust the turn budget without converging. Models also achieve higher success rates when examples are provided by the oracle than when they select their own queries, although their final hypotheses are more consistent with the evidence they selected. These findings suggest that models may form hypotheses that fit self-selected evidence without sufficiently distinguishing them from alternatives, and may struggle to validate and refine their hypotheses or determine when to stop.

## Metadata
- **Published**: 2026-08-04T09:39:24Z
- **Authors**: Shahrukh Mohiuddin, Chalamalasetti Kranti, Sherzod Hakimov, David Schlangen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03388v1)