---
title: Language Models Encode the Contextual Truth of Propositions
published: 2026-08-04T02:30:59Z
authors: Rupak Sarkar, Pritika Ramu, Rachel Rudinger
url: http://arxiv.org/abs/2608.03035v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language Models Encode the Contextual Truth of Propositions

## Abstract
Prior work has shown that LLMs encode the truth of factual propositions along linear directions in activation space. It's unclear how these representations extend to contextual truth: propositions whose truth is determined by in-context evidence rather than world knowledge. We show that LLMs maintain a linear representation of contextual truth that persists across structurally different output policies, even when the output doesn't require the model to determine a proposition's truth, and show causal evidence via steering experiments. Using the transcripts from a collaborative vision-language task that requires two LLMs to maintain a shared common ground, we show that truth representations of a proposition are significantly swayed by partner assertions about that proposition, even when the LLM has enough evidence to determine its truth. We find evidence that propositions near the decision boundary are more susceptible to having their truth shifted through partner assertions. Separating representation from output distinguish two forms of sycophancy that output behavior alone cannot: the model may accommodate a false proposition while continuing to represent it as false, or shift its representation across the boundary. The latter is 2.59x more common when the model agrees by restating the false claim explicitly than when it agrees implicitly.

## Metadata
- **Published**: 2026-08-04T02:30:59Z
- **Authors**: Rupak Sarkar, Pritika Ramu, Rachel Rudinger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03035v1)