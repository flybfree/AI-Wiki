---
title: Rule vs.Consequence: Dissociable Internal Representations of Moral Reasoning in LLMs
published: 2026-10-12T08:22:28Z
authors: Eugenie Shi
url: http://arxiv.org/abs/2610.16371v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rule vs.Consequence: Dissociable Internal Representations of Moral Reasoning in LLMs

## Abstract
Large language models are increasingly deployed in morally and legally sensitive contexts, yet little is known about how they internally represent distinctions between moral reasoning styles. We ask whether a model's differential response to rule-framed and consequence-framed moral questions reflects distinct internal structure or merely surface lexical sensitivity. We construct a 2$\times$2 factorial dataset crossing reasoning style (rule-based vs. consequence-based framing) with judgment polarity (permissive vs. prohibitive), drawn from three established moral reasoning benchmarks and evaluated on a cleanroom test set of novel phrasings that includes conflict pairs where the two framings predict opposite labels. Using linear probing and activation steering, we identify two orthogonal directions in the residual stream: Dir-A tracks reasoning style and Dir-B tracks judgment polarity, each near-blind to the other factor (cross-correlation $|r| < 0.04$). This double dissociation replicates across three instruction-tuned models from different developers at comparable proportional depth, and it is not knife-edged in layer: the directions are recoverable and causally effective throughout an extended band of the network. Dir-A can causally change judgments, and in conflicting scenarios, it selectively corrects errors in rule-based judgments without changing consequence-based judgments, suggesting that it does not simply make the model more likely to accept everything. Generalization beyond the training templates is partial: the direction transfers across benchmark sources, but its advantage over lexical baselines on novel phrasings is modest. We therefore frame the result as moral reasoning style sensitivity, a geometrically dissociable and causally effective structure, rather than internalized normative reasoning.

## Metadata
- **Published**: 2026-10-12T08:22:28Z
- **Authors**: Eugenie Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16371v1)