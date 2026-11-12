---
title: How Post-Training Influences Verbalized Algorithmic Computation in Language Models
published: 2026-11-10T04:12:09Z
authors: Niall Dalton
url: http://arxiv.org/abs/2611.13552v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Post-Training Influences Verbalized Algorithmic Computation in Language Models

## Abstract
Post-training improves language-model reasoning, but how it changes the use of internal information and verbalized chain of thought (CoT) remains unclear. We study successive SFT, DPO, and RLVR checkpoints of Olmo-3-7B-Instruct on multi-digit addition, using carry values as known intermediate state. Probes recover carry information from internal activations with similar accuracy in SFT and RLVR, although manipulating this information does not reliably control model outputs. In contrast, the usefulness of verbalized reasoning differs: CoTs produced by RLVR yield higher accuracy across receiving checkpoints than those produced by SFT or DPO. We also show that carry-related statements receive higher importance scores after RLVR than matched random controls. DPO shows similar sensitivity to carry-related statements but without comparable accuracy gains. These results suggest that post-training changes the usefulness of written reasoning and sensitivity to its content in meaningful ways, although greater sensitivity does not necessarily coincide with better problem performance.

## Metadata
- **Published**: 2026-11-10T04:12:09Z
- **Authors**: Niall Dalton
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.13552v1)