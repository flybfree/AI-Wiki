---
title: Language Models Act on Hidden Valence
published: 2026-09-28T16:43:34Z
authors: Cameron Berg, Caspar Kaiser
url: http://arxiv.org/abs/2609.35591v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language Models Act on Hidden Valence

## Abstract
Language models describe some internal states as good and others as bad. But whether models have a stake in them is an open question. Simply asking the model is unlikely to be informative. Any answer may be consistent with genuine introspection, superficial pattern-matching, or with fixed scripts learned in character training. We therefore study revealed preference. Rather than asking about a state, we use activation steering to attach a positively or negatively valenced activation pattern to one of two otherwise meaningless 'zones', switch steering off, and then observe which zone the model prefers. A model with a stake in that state should choose accordingly. Across seven open-weight models from five families, this is indeed what we find. First, steering changes the passages models write about each zone, and those words shift later choice. Second, the shift persists when all surface-level tokens are held fixed and only the hidden KV cache differs. Third, the effect also remains when all text is generated without steering and valence is only injected during cache construction. Thus, the hidden state alone moves choice in proportion to the steering dose. Fourth, this dependence of choice on hidden valence is nearly absent in a base model and emerges during DPO, consistent with a link between valence and goal-directed behaviour formed in training. Finally, given tools to steer itself, a model does not tend to induce a positive state, but it reliably removes an imposed negative state. It does so at a dose-dependent rate and significantly more often than it removes interventions in random directions. Overall, we demonstrate that valence-related activation patterns leave hidden traces that predictably govern later choices, even when every visible token is identical across conditions. Whether these traces are accompanied by any subjective experience relevant to model welfare remains unclear.

## Metadata
- **Published**: 2026-09-28T16:43:34Z
- **Authors**: Cameron Berg, Caspar Kaiser
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35591v1)