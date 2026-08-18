---
title: Does the LM Head Create a Harmful Gradient Bottleneck? A Causal Test
published: 2026-08-17T14:59:59Z
authors: Anand Murugan
url: http://arxiv.org/abs/2608.16671v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does the LM Head Create a Harmful Gradient Bottleneck? A Causal Test

## Abstract
The language-model head maps a hidden state of width D to a vocabulary of size V, so its transpose can return at most D independent directions to the Transformer. Godey and Artzi argue that this severe projection is a harmful optimization bottleneck. We separate the geometry from the causal claim. Our backward-only intervention keeps the ordinary logits and the exact LM-head parameter update while reducing only the rank of the gradient sent into the Transformer. Across five paired seeds on byte-level and BPE-8192 WikiText-2 models, reducing backward rank increases validation loss. An equally ranked factorized forward head, however, increases loss substantially more. At half rank in the larger model, the backward-only loss increase is 0.0586 (95% CI [0.0167, 0.1005]), while the factorized forward head increases loss by 0.1795 ([0.1547, 0.2042]). The vocabulary-space residual also contributes to the ordinary LM-head update, and removing that contribution is harmful. Additional controls show that repeated-token failures are confounded by the number of independently sampled symbols, that adding never-target output classes does not impair learning, and that projection diagnostics do not reliably predict progress in our runs. Tested auxiliary feedback routes do not beat tuned backpropagation. These results confirm strong geometric compression but do not establish that it is a harmful optimization bottleneck.

## Metadata
- **Published**: 2026-08-17T14:59:59Z
- **Authors**: Anand Murugan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16671v1)