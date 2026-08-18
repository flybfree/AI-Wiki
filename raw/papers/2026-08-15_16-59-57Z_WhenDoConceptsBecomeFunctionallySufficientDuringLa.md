---
title: When Do Concepts Become Functionally Sufficient During Language-Model Training?
published: 2026-08-15T16:59:57Z
authors: Raphael Bernas, Paul G. Chevalier, Fanny Jourdan, Céline Hudelot
url: http://arxiv.org/abs/2608.15323v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Do Concepts Become Functionally Sufficient During Language-Model Training?

## Abstract
Understanding a model and its learning mechanisms in depth requires identifying when its internal structures become useful, rather than simply looking at the final state. We study this through concept dynamics: at each layer and checkpoint, we decompose activations, select sparse soft masks, and inject masked reconstructions into the model. Concept analysis is therefore tested functionally: a mask is useful only insofar as it preserves a target under intervention. We compare sufficiency for activation reconstruction, linear decodability, true downstream preservation, and checkpoint transfer under learned alignment. The framework treats decomposition assumptions as hypotheses rather than interpretability guarantees, monitoring functional sufficiency across checkpoints and source-to-final reconstructability under learned alignment. At the shared fixed-penalty operating point across seven models, downstream masks retain substantially less soft mass than reconstruction masks; predictive-distribution shifts remain small.

## Metadata
- **Published**: 2026-08-15T16:59:57Z
- **Authors**: Raphael Bernas, Paul G. Chevalier, Fanny Jourdan, Céline Hudelot
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15323v1)