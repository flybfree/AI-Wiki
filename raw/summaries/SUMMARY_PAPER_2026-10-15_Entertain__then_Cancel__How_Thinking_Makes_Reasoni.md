---
title: Entertain, then Cancel: How Thinking Makes Reasoning Models Read Some and Or Literally
url: http://arxiv.org/abs/2610.21204v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_04-01-59Z_Entertain_thenCancel_HowThinkingMakesReasoningMode.md
generated_at: 2026-10-15 22:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how the amount of "thinking" time allocated to reasoning models affects their interpretation of everyday logical language, specifically scalar implicatures like "some" (implying "not all") and "or" (implying "not both"). By holding model weights fixed and varying only the thinking budget, the authors demonstrate that extended reasoning causes most tested open reasoning models and GPT-5 to cancel these pragmatic inferences and adopt strictly literal readings, while simultaneously improving context-driven inferences such as indirect answers.

## Key Takeaways
- Extended thinking systematically cancels scalar implicatures: when models are given more reasoning time, they shift from the enriched pragmatic reading of "some" (meaning "not all") and "or" (meaning "not both") toward purely logical interpretations. This effect was observed across most tested open reasoning models and in GPT-5, suggesting it is a widespread phenomenon rather than an isolated model quirk.
- The reasoning trace reveals a two-stage process: models first entertain the enriched, contextually appropriate reading and then actively cancel it during later stages of their chain-of-thought. A second experimental tool that truncates reasoning at successive points and requests an answer pinpoints exactly where the interpretive shift occurs, confirming the "entertain, then cancel" mechanism.
- An exploratory inference-time remedy is proposed: prompting the model to answer from its early, pre-cancellation reading recovers the pragmatic implicatures without sacrificing literal accuracy. This suggests the capability to generate enriched interpretations exists within the model but is suppressed by extended deliberation.

## Context
Reasoning models such as those in the o-series and GPT-5 have introduced user-controllable thinking budgets, making it possible to trade off depth of deliberation against speed. While much research has focused on how thinking improves factual accuracy or mathematical problem-solving, the effect of extended reasoning on pragmatic language understanding—how models interpret the intended meaning behind everyday utterances—has remained largely unexamined. This paper fills that gap by isolating thinking time as the sole variable and measuring interpretive shifts directly.

## Implications
For practitioners deploying reasoning models in conversational AI, legal analysis, or any domain where pragmatic meaning matters, this work warns that defaulting to maximum thinking budgets may silently strip away the very inferences users expect from natural language. Evaluation frameworks for reasoning models should expand beyond accuracy metrics to include measures of interpretive fidelity, ensuring that models do not merely produce correct answers but also correctly understand what was actually being asked or implied.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21204v1)
