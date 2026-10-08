---
title: The Long Road to the Same Answer: Cognitive Bias Under Escalating Reasoning Budgets in Large Language Models
published: 2026-10-07T13:23:51Z
authors: Obada Kraishan
url: http://arxiv.org/abs/2610.10049v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Long Road to the Same Answer: Cognitive Bias Under Escalating Reasoning Budgets in Large Language Models

## Abstract
Reasoning models allocate extra computation at inference time and present their answers as the product of deliberate thought. If this deliberation works the way dual-process accounts of human cognition suggest, longer thinking should weaken the classic decision biases that fast, intuitive judgment produces. Using 30 vignettes covering six biases (anchoring, framing, loss aversion, escalation of commitment, availability, confirmation) from an established benchmark, we run a dose-response study across four model families, pairing each reasoning model with a matched non-reasoning sibling and requesting thinking ceilings of 0, 1,024, 4,096, and 8,192 tokens, for 12,350 API calls. Because a requested ceiling is not the same as realized deliberation, we use the reasoning tokens each call consumed as the dose. First, reasoning models are not less biased than their siblings; the point estimate leans the other way in every family, but the item-level pooled contrast is not reliable (Delta = +0.031, t(29) = 1.45, p = .157). Second, bias magnitude does not reliably fall as realized deliberation grows: no slope is significantly negative, and where anything moves it is the signed score drifting further from the human direction. Third, anchoring is the only bias in the human direction (d = 1.89). Four of the other five lean the opposite way in all seven models; with five items per bias, that reversal is reliable for framing and directional for escalation of commitment, confirmation, and loss aversion, while availability is absent. A one-line instruction to restate the anchor before answering lowered anchoring on all five anchoring items, which no amount of additional thinking did, although the effect does not reach significance (p = .057). The results argue against treating test-time reasoning as a rationality guarantee and for auditing deployed models bias by bias.

## Metadata
- **Published**: 2026-10-07T13:23:51Z
- **Authors**: Obada Kraishan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10049v1)