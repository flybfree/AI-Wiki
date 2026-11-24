---
title: Information Access and Gain-Loss Framing in Six Large Language Models and Human Decision Makers
url: http://arxiv.org/abs/2611.28525v1
type: paper-summary
date: 2026-11-23
source_paper: 2026-11-21_03-21-55Z_InformationAccessandGain_LossFraminginSixLargeLang.md
generated_at: 2026-11-23 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether six large language models (GPT-4.1, GPT-4o, GPT-4o-mini, Gemini 2.5 Flash, Qwen3 235B, and Llama 4 Maverick) exhibit the well-documented gain-loss framing effect in risky decision-making, and whether providing additional information through "information cards" reduces that effect. Across 11,519 simulated choices in four risk scenarios, all six models displayed substantial framing biases when no information was available, but the magnitude of the effect varied widely across models and information-access conditions, with some models showing partial mitigation and others showing persistent or even growing gaps.

## Key Takeaways
- Without any information cards, all six LLMs exhibited large gain-loss framing effects, with the proportion choosing the safe option shifting by 27 to 79 percentage points depending on whether the scenario was framed in terms of gains or losses, demonstrating that current LLMs replicate a cognitive bias long documented in human behavioral economics.
- Accessing information cards reduced the framing gap in every model when moving from zero to two cards, but the degree of mitigation was highly inconsistent: GPT-4.1 fell within a 10-point threshold only at four cards, Qwen3 only at two, while GPT-4o-mini and Llama 4 Maverick retained gaps of 28 to 66 percentage points even with cards, and for GPT-4o-mini and Qwen3 the gap paradoxically grew again from two to four cards.
- An exploratory comparison with 198 human students who interacted with the same scenarios and cards showed a 19-point framing difference after opening zero or one cards, with no clear difference after opening more, though the study design could not causally demonstrate that information access reduced framing in humans, and 17 of 18 card-based gaps in the models fell below their no-card gaps but few met the predefined threshold.

## Context
The gain-loss framing effect, rooted in prospect theory, is one of the most robust findings in behavioral decision science, showing that identical choices described as savings versus losses produce systematically different preferences. As LLMs are increasingly deployed in domains involving consequential decisions—healthcare triage, financial advice, policy analysis, and risk communication—understanding whether these models inherit or amplify human cognitive biases is critical for responsible deployment. This study bridges behavioral economics and AI evaluation by testing whether information access, analogous to providing decision aids to humans, can serve as a debiasing mechanism for model outputs.

## Implications
For practitioners deploying LLMs in decision-support roles, the findings suggest that simply prompting a model with more context or information cards does not reliably eliminate framing bias and may even worsen it for certain architectures, meaning that prompt engineering alone is insufficient as a safeguard. Model developers and AI governance teams should treat framing sensitivity as a measurable failure mode requiring targeted evaluation protocols rather than assuming that increased information access automatically produces more rational outputs. The partial convergence between model behavior and human behavior also raises questions about whether training data encodes human decision heuristics that will persist unless explicitly addressed in alignment and evaluation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.28525v1)
