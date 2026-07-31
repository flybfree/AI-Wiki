---
title: Evaluating and Pricing Advertisements in AI-Generated Responses
published: 2026-07-30T05:07:27Z
authors: John L. Turner-Smith, Zimeng Huang, Yuhan Fu, Yihang Zhang, Tonghan Wang
url: http://arxiv.org/abs/2607.27686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating and Pricing Advertisements in AI-Generated Responses

## Abstract
As search increasingly shifts toward LLM-driven answer engines, advertising is becoming embedded within the generated response itself and should therefore be evaluated for both user utility and commercial value. The key challenge is click-through intent: behavioural logs are unavailable, human annotation resists calibration, and frontier LLM judges conflate intent with linguistic fluency. These gaps compound, as principled pricing presupposes a continuous intent signal, while generating such a signal presupposes supervision that is currently unavailable. We construct the missing supervision through a psychologically grounded agent simulation framework, and distil it into a parameter-efficient evaluator that predicts click-through intent, together with the three companion dimensions of ad quality, as smooth, differentiable estimates. Validated through sign-certain behavioural perturbations, the evaluator surpasses frontier zero-shot judges on relevance sensitivity (79% versus 60-67%), tracks graded content degradation, generalises without error to 103 fictional products, and agrees with human preference in 86% of pairwise judgements across five annotators, with agreement rising in the evaluator's confidence. Upon its estimates we build the pricing layer directly, deriving the unique payment rule under which truthful bidding is optimal, demonstrating it on a best-of-k allocation, and extending the mechanism to non-monotone allocations. The same differentiable signal stands ready as a training objective for ad generation.

## Metadata
- **Published**: 2026-07-30T05:07:27Z
- **Authors**: John L. Turner-Smith, Zimeng Huang, Yuhan Fu, Yihang Zhang, Tonghan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27686v1)