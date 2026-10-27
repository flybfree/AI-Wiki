---
title: Beyond Belief: Evaluating and Mitigating LLM Susceptibility to Misinformation
published: 2026-10-25T00:26:14Z
authors: Emran Kanaan, Jiho Lee, Ibrahim Odat, Soroush Vosoughi, Weicheng Ma
url: http://arxiv.org/abs/2610.33962v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Belief: Evaluating and Mitigating LLM Susceptibility to Misinformation

## Abstract
Tool-using large language models (LLMs) must decide whether external information warrants action. We investigate whether their expressed credibility judgments reliably indicate behavioral resistance to misinformation. We evaluate five LLMs on 196 constructed false notices paired with legitimate counterparts and 204 archived attacks adapted to simulated tool use. When asked to act on the constructed notices, models issue harmful tool calls in 27%--99% of cases they have rated untrustworthy. Removing the preliminary rating step increases harmful execution by 15 percentage points on average, showing that credibility elicitation itself changes the behavior being evaluated. Interventions that improve credibility discrimination do not consistently yield safer actions. A simple forewarning significantly reduces harmful execution in four of five models, but neither tested generated-example prebunk outperforms it in the main evaluation. These reductions can also compromise legitimate task completion. Supervised fine-tuning on generated false notices reduces harmful execution on held-out archived attacks under the rating-first protocol, with model-dependent utility costs and weaker protection without rating elicitation. Our findings motivate evaluating misinformation defenses through both harmful actions and legitimate task completion, while accounting for the behavioral effects of the evaluation protocol.

## Metadata
- **Published**: 2026-10-25T00:26:14Z
- **Authors**: Emran Kanaan, Jiho Lee, Ibrahim Odat, Soroush Vosoughi, Weicheng Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33962v1)