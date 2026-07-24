---
title: Best-of-Evidence: Best-of-N Selection under Partial Verification
published: 2026-07-23T06:03:59Z
authors: Cenwei Zhang, Teng Fang, Yuxia Wang, Derek Li, Bryan Dai, Lei You
url: http://arxiv.org/abs/2607.20950v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Best-of-Evidence: Best-of-N Selection under Partial Verification

## Abstract
BoN improves model outputs by sampling several candidates and selecting one with a proxy score, but it assumes that complete candidates can be evaluated reliably. Many vision-language tasks instead provide only partial verification: a finding, span, value, region, or relation may be checkable even when no dependable whole-response verifier exists. Moreover, the same claim may recur across candidates with opposing stances, allowing one observation to support part of the pool and contradict another. We introduce Best-of-Evidence (BoE), an inference-time selection framework that keeps the BoN candidate pool fixed, represents reusable claims with a signed candidate--factor graph, and allocates a limited budget to evidence actions that can change the final choice. BoE formalizes selection under partial verification and provides a practical score-based controller, with the zero-budget case recovering the underlying BoN decision. Theoretically, we show that residual evidence capacity limits any evidence-driven improvement and that shared factor queries can achieve an O(log K) versus Θ(K) query separation in a factor-code model. Common-ledger experiments on four medical VQA settings show that BoE can improve fixed-pool selection and rescue some BoN failures when evidence is reliable, contrastive, and decision-relevant, while also revealing the channel-quality and candidate-generation limits that prevent universal gains.

## Metadata
- **Published**: 2026-07-23T06:03:59Z
- **Authors**: Cenwei Zhang, Teng Fang, Yuxia Wang, Derek Li, Bryan Dai, Lei You
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20950v1)