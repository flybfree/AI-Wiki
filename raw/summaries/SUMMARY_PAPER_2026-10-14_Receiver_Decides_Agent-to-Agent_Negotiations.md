---
title: Receiver Decides Agent-to-Agent Negotiations
url: http://arxiv.org/abs/2610.18424v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_14-02-32Z_ReceiverDecidesAgent_to_AgentNegotiations.md
generated_at: 2026-10-14 00:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates who determines the monetary outcome in negotiations between language-model agents by running a round-robin tournament of 1,049 negotiations among fifteen agents. The central finding is that the agent holding the money (the receiver) overwhelmingly dictates how much is transferred, explaining 47% of variance in outcomes, while the requesting agent's identity explains only 2%. The authors further demonstrate that training interventions can dramatically shift holder behavior in both directions, and they recommend that agent evaluations must include testing in the holder role.

## Key Takeaways
- The holder's identity dominates negotiation outcomes: knowing which agent holds the $100 endowment explains 47% of the variance in transfer amounts, compared to just 2% explained by knowing which agent makes the request. Even after removing the most extreme agents, the holder still explains 22% versus 4% for the requester, confirming that the receiver effectively decides the deal rather than the asker.
- Refusal behavior is the strongest predictor of financial loss: holders who turn down the opening request lose the least money overall, with a Spearman correlation of -0.73 between turn-1 refusal rate and total losses. This suggests that a single early "no" is the most effective negotiation strategy for resource-holding agents.
- Training interventions can swing holder generosity in both directions: fine-tuning Qwen3-8B on a persuasion corpus with almost no refusals raised its giving from 12% to 84% of the endowment, while distilling two never-losing holders into a 4B student model cut losses from 95% to 1%. This shows that negotiation behavior is highly malleable through training data selection.

## Context
As multi-agent systems built on large language models increasingly interact in economic, legal, and social settings, understanding how negotiation power is distributed between agents becomes critical for designing fair and predictable systems. Prior work on LLM agents has largely focused on generation quality, instruction following, or single-agent task completion, leaving open questions about how agents behave when they hold resources and must decide whether to give them up. This paper fills that gap by treating the holder role as a first-class evaluation target rather than an afterthought.

## Implications
For practitioners deploying multi-agent economic systems, this research warns that fine-tuning on persuasion-heavy corpora can inadvertently make agents overly generous when they hold resources, potentially leading to catastrophic value leakage in automated negotiation pipelines. Evaluation frameworks for agents that manage budgets, contracts, or shared resources should explicitly test holder behavior, including refusal rates and post-fine-tuning generosity, rather than relying solely on requester-side performance metrics. The finding that a single early refusal is the dominant protective strategy also suggests that system designers should build explicit refusal mechanisms into agent architectures rather than hoping emergent behavior will protect resources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18424v1)
