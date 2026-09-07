---
title: Can Activation Steering Capture Multidimensional Authorship Style?
published: 2026-09-04T06:46:23Z
authors: Hieu Tran, Calvin Bao, Marine Carpuat
url: http://arxiv.org/abs/2609.04792v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Activation Steering Capture Multidimensional Authorship Style?

## Abstract
Activation steering has shown promise for controlling LLM generation along well-defined attributes, but it remains unclear whether it can handle the multidimensional and hard-to-define nature of authorship style. We ask whether structured contrastive prompting along rhetorically-motivated dimensions can construct rich style representations directly in activation space, bypassing the need for natural language style descriptors or dedicated training. We find that the resulting directions share a common authorship backbone while conflicting on aspect-specific residuals that carry genuine stylistic signal, explaining why naive aggregation fails. We operationalize this in Aspect-Aware Activation Steering (A3S), a training-free framework that merges per-aspect contrastive directions with interference-aware aggregation and tunes steering strength per instance. A3S improves authorship style transfer where it is genuinely multi-aspect, outperforms a trained baseline in preference evaluations on out-of-domain benchmarks, and keeps target-exemplar overlap consistently low.

## Metadata
- **Published**: 2026-09-04T06:46:23Z
- **Authors**: Hieu Tran, Calvin Bao, Marine Carpuat
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04792v1)