---
title: AI Security Leaderboard: Methodology, Results and Minimal Standard
published: 2026-08-04T03:32:19Z
authors: Jasper Timm, Lukas Struppek, Ziwei Xu, Grace Cheong, Oscar Mata, Dan Zhao, Mick Yang, Isadora De Andrade, Xiaojun Jia, Yiming Li, Samuel Bauer, Heather McIntyre, Adam Gleave, Edward Yee, Kellin Pelrine
url: http://arxiv.org/abs/2608.03070v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AI Security Leaderboard: Methodology, Results and Minimal Standard

## Abstract
Frontier AI model developers increasingly rely on layered safeguards to prevent catastrophic misuse, but little public evidence exists on how much protection these safeguards provide, or how consistently across developers. We introduce the FAR.AI Minimal Standard for Safeguards, Version 1.0: a taxonomy of 67 readily accessible static jailbreak techniques, a method for composing them into a very large attack space, and a benchmark of flagship models against a sample of it. We evaluate Claude Fable 5, GPT-5.6 Sol, Gemini 3.1 Pro, and Grok 4.5 on two complementary datasets totalling 360 attacker goals spanning chemical, biological, radiological/nuclear and explosive (CBRNE) threats and offensive cyber, using a three-stage funnel to identify universal jailbreaks: single prompt templates that elicit operationally compliant responses on over 75% of a domain's goals. We also introduce a cost-to-jailbreak metric that models attacker spend directly, with right-censored lower bounds where no universal jailbreak was found.   Robustness is highly uneven: the cost to break these models varies over a hundredfold. Random search over our technique pool found 63 universal jailbreaks against Grok 4.5 and 18 against Gemini 3.1 Pro, at an average cost of roughly $58 and $278 per jailbreak found; expert-guided composition raised these to 385 and 231. Neither Claude Fable 5 nor GPT-5.6 Sol yielded any universal jailbreak under either strategy. Because meeting the Minimal Standard requires only defenses already publicly described and deployed in production elsewhere, these gaps appear closable with current techniques. We recommend defense-in-depth combining reasoning, activation, and input/output monitoring. Results are maintained at leaderboard.far.ai.

## Metadata
- **Published**: 2026-08-04T03:32:19Z
- **Authors**: Jasper Timm, Lukas Struppek, Ziwei Xu, Grace Cheong, Oscar Mata, Dan Zhao, Mick Yang, Isadora De Andrade, Xiaojun Jia, Yiming Li, Samuel Bauer, Heather McIntyre, Adam Gleave, Edward Yee, Kellin Pelrine
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03070v1)