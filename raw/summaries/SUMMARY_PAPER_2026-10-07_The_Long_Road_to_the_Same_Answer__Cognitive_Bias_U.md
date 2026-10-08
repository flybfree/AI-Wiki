---
title: The Long Road to the Same Answer: Cognitive Bias Under Escalating Reasoning Budgets in Large Language Models
url: http://arxiv.org/abs/2610.10049v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_13-23-51Z_TheLongRoadtotheSameAnswer_CognitiveBiasUnderEscal.md
generated_at: 2026-10-07 22:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether extended test-time reasoning in large language models reduces classic cognitive decision biases, drawing on dual-process theories of human cognition that predict longer deliberation should weaken intuitive judgment errors. Through a dose-response experiment across four model families using 30 vignettes spanning six biases and 12,350 API calls, the author finds that reasoning models are not less biased than their non-reasoning counterparts, and that increasing thinking budgets does not reliably reduce bias magnitude.

## Key Takeaways
- Reasoning models do not outperform their non-reasoning siblings on bias resistance: the pooled contrast across all items shows a slight lean toward greater bias in reasoning models (Delta = +0.031, t(29) = 1.45, p = .157), and across every model family the point estimate favors the non-reasoning variant, though the difference is not statistically reliable at the item level.
- Bias magnitude does not reliably decrease as realized deliberation tokens increase: no dose-response slope is significantly negative, and where measurable drift occurs, the signed score moves further away from the human-expected direction rather than closer to it, undermining the assumption that more thinking yields more rational outputs.
- Anchoring is the sole bias showing a strong human-direction effect (d = 1.89), while four of the remaining five biases (framing, escalation of commitment, confirmation, loss aversion) lean in the opposite direction across all seven models tested. A simple one-line instruction to restate the anchor before answering reduced anchoring on all five anchoring items, an effect no amount of additional reasoning tokens achieved, though it narrowly missed significance (p = .057).

## Context
This study sits at the intersection of behavioral economics, cognitive psychology, and AI evaluation, testing whether the popular narrative that extended chain-of-thought reasoning makes models more "rational" holds up under controlled experimental scrutiny. By pairing reasoning and non-reasoning model variants and using realized token consumption as the dose variable, the paper addresses a methodological gap in prior LLM bias studies that often conflate requested thinking budgets with actual deliberation effort.

## Implications
For practitioners deploying reasoning-augmented models in high-stakes domains such as finance, medicine, or legal decision support, the findings caution against treating test-time reasoning as a built-in rationality guarantee and instead advocate for bias-by-bias auditing of deployed systems. The surprising effectiveness of a minimal prompting instruction over massive token budgets suggests that targeted behavioral interventions may be more practical and efficient than scaling inference compute, with direct consequences for model design, evaluation pipelines, and regulatory frameworks governing AI-assisted decision-making.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10049v1)
