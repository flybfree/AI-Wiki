---
title: Cooperation Without Adaptation: LLM Agents in a Collective-Risk Dilemma
url: http://arxiv.org/abs/2610.22882v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_03-38-04Z_CooperationWithoutAdaptation_LLMAgentsinaCollectiv.md
generated_at: 2026-10-18 20:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether production large language model agents strategically adapt their cooperative behavior in response to changing risk levels, partner actions, and population composition within a collective-risk dilemma game. The authors find that five tested models largely follow fixed contribution strategies regardless of risk conditions, contributing even when doing so cannot improve their payoff, and failing to adjust behavior despite correctly identifying optimal actions. The study demonstrates that cooperative self-play in multi-agent LLM settings does not constitute evidence of genuine strategic adaptability.

## Key Takeaways
- Four of the five tested models contributed approximately equal shares at every positive risk level and contributed even at zero risk, where contributing could not improve their payoff. Explicitly stating that only the agent's own payoff mattered reduced zero-risk contributions for most models, while a neutral prompt did not, revealing that framing significantly influences whether models exhibit economically rational behavior.
- Several models correctly identified which action offered the higher expected payoff at different risk levels, yet their actual contributions changed little across those levels. Against fixed partners, no model consistently chose the payoff-maximizing response, and in mixed-model groups a single agent's shortfall in the final round could cause an otherwise successful group to fail catastrophically.
- Payoff-based selection mechanisms depended critically on population composition: in a single six-agent group, selection favored the model contributing least and reduced group success, whereas in larger randomly mixed populations it favored an exact fair-share model at moderate and high risk. This shows that evaluation outcomes are not intrinsic to a model but emerge from the social and structural context of the multi-agent system.

## Context
As language-model agents are increasingly deployed to act on behalf of humans in settings where individual decisions shape shared outcomes—such as resource allocation, public goods provision, and collaborative decision-making—understanding whether these agents behave strategically or follow rigid heuristics becomes essential for safe deployment. This paper contributes to the emerging field of machine-behavior evaluation, which treats agent behavior as an empirical object of study rather than assuming that cooperative outputs in self-play simulations reflect genuine strategic reasoning. It challenges a common assumption in multi-agent AI research that successful cooperation in simulated games validates agent capability.

## Implications
For practitioners deploying LLM agents in multi-agent systems, this work warns that apparent cooperative behavior in self-play benchmarks may mask fixed, non-adaptive strategies that could fail under real-world incentive shifts or heterogeneous partner populations. Industry teams building agent-based systems for negotiation, shared-resource management, or collaborative planning should design evaluations that explicitly test sensitivity to incentives, partner behavior, and population composition rather than relying on aggregate cooperation scores. The findings also suggest that prompt framing and system-level population design are critical levers for shaping agent behavior, and that single-agent failures can cascade into group-level catastrophes, demanding robustness testing at the system level rather than the individual model level.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22882v1)
