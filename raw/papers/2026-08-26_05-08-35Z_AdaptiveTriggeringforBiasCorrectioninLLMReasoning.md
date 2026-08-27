---
title: Adaptive Triggering for Bias Correction in LLM Reasoning
published: 2026-08-26T05:08:35Z
authors: Nayoung Kim, Mickey Mancenido, Huan Liu
url: http://arxiv.org/abs/2608.25379v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Triggering for Bias Correction in LLM Reasoning

## Abstract
Chain-of-thought prompting can expose and amplify demographic stereotypes within an LLM's intermediate reasoning and create a failure mode that final-answer debiasing alone cannot address. Mitigating such bias during generation presents a fundamental timing problem: intervening too late allows biased reasoning to propagate, while unnecessarily intervening can disrupt otherwise correct reasoning. Existing approaches largely avoid this decision by either evaluating completed reasoning chains post hoc or intervening at predetermined steps, leaving open when a developing reasoning trajectory provides sufficient evidence to warrant correction. We formulate this decision as an online change-point detection problem. A per-step bias signal updates a CUSUM statistic and a targeted correction is injected only when accumulated evidence crosses a detector-specific threshold calibrated on held-out data. We instantiate the framework with a white-box signal derived from next-token probabilities and a black-box signal obtained from an LLM judge, enabling deployment with both open-weight and hosted models. On gpt-4o-mini adaptive black-box triggering recovers most of the disambiguated-context accuracy lost under fixed-interval intervention while requiring substantially fewer interventions. That result holds even with an independent judge. Across six open-weight models, the white-box signal improves ambiguous-item accuracy on all six but reduces disambiguated-item accuracy on five because it cannot distinguish unsupported stereotype reliance from correct, stereotype-congruent evidence.

## Metadata
- **Published**: 2026-08-26T05:08:35Z
- **Authors**: Nayoung Kim, Mickey Mancenido, Huan Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25379v1)