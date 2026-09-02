---
title: StateSwap: Probing Support-Elimination Hidden States in Multiple-Choice Questions
published: 2026-09-01T11:13:26Z
authors: Chao Gao, Haijiang Liu, Qiyuan Li, Caicai Guo, Frank van Harmelen, Jinguang Gu
url: http://arxiv.org/abs/2609.01081v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StateSwap: Probing Support-Elimination Hidden States in Multiple-Choice Questions

## Abstract
Large language models often answer the same multiple-choice question inconsistently when it is posed under support-oriented and elimination-oriented framings. We investigate whether these discrepancies arise from different internal representations induced by the two framings. We introduce a dual-framing protocol with minimally varied prompts that use either support- or elimination-oriented framing while keeping the evaluation target fixed. To probe the internal computation, we append an untrained special token, [STATE], and treat its residual-stream activation as an intervention interface. Across both models, the two framings induce separable [STATE] activations concentrated in intermediate layers. Swapping these activations between paired prompts systematically changes predictions and improves cross-framing agreement, providing intervention-based evidence that the activations are behaviorally relevant. Beyond instance-level substitution, mean-difference steering directions derived from the dual-framing contrast exhibit more bounded layer-wise responses than matched contrastive activation addition directions under the evaluated protocol.

## Metadata
- **Published**: 2026-09-01T11:13:26Z
- **Authors**: Chao Gao, Haijiang Liu, Qiyuan Li, Caicai Guo, Frank van Harmelen, Jinguang Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01081v1)