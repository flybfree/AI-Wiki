---
title: Not All Eval-Awareness Is Equal: Capabilities Framing Predicts Compliance
published: 2026-08-27T16:41:48Z
authors: Allison Zhuang, Santiago Aranguri
url: http://arxiv.org/abs/2608.27340v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not All Eval-Awareness Is Equal: Capabilities Framing Predicts Compliance

## Abstract
Steering interventions targeting eval-awareness, a model's recognition that it is being tested, are increasingly used in safety evaluation pipelines, where evaluation-awareness is treated as a single quantity to be suppressed. We show that verbalized eval-awareness in chain-of-thought can be identified as capabilities-flavored ("the user is testing my ability to follow instructions"), safety-flavored ("the user is testing my boundaries"), both, or neither: framings that predict compliance very differently. On Qwen3-32B over the FORTRESS dataset, capabilities-framing predicts compliance with a +24 to +46 percentage-point gap over safety-framing across all tested steering conditions. A CoT-prefill intervention on eval-awareness-negative rollouts suggests the link is causal, with 10 of 11 prefills shifting compliance in the predicted direction. Then, eval-awareness is not behaviorally uniform: aggregate suppression rates can move while the safety-relevant component does not, and the same "X% suppression of eval-awareness" can correspond to qualitatively different behavioral outcomes.

## Metadata
- **Published**: 2026-08-27T16:41:48Z
- **Authors**: Allison Zhuang, Santiago Aranguri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27340v1)