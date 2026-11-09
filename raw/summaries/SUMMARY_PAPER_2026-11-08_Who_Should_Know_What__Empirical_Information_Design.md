---
title: Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies
url: http://arxiv.org/abs/2611.07667v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-05_08-51-37Z_WhoShouldKnowWhat_EmpiricalInformationDesignforMul.md
generated_at: 2026-11-08 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "empirical information design," an experimental framework for systematically comparing how different information disclosure policies affect the performance of multi-agent LLM systems in economic market settings. By evaluating ten frontier LLMs across trade, bargaining, and double auction scenarios, the authors demonstrate that providing agents with more detailed information does not uniformly improve collective outcomes; instead, the effects are highly model-dependent, with some models benefiting from transparency while others suffer significant welfare losses.

## Key Takeaways
- In multi-resource trade settings, revealing exact valuations rather than ordinal preference rankings produced divergent outcomes across models: GPT-6 Sol saw realized gains drop from 98% to 91% of the maximum achievable, while Claude Sonnet 5 improved from 72% to 86%. This demonstrates that information granularity interacts with model-specific reasoning strategies in non-obvious ways, making a one-size-fits-all disclosure policy inadequate.
- In bilateral bargaining, exact information disclosure led Grok 4.7 to produce less balanced agreements, whereas Claude Opus 5.5 divided gains symmetrically under the same conditions. This highlights that the strategic interpretation of information—how a model translates detailed data into negotiation behavior—varies substantially across model architectures and training regimes.
- In double auctions, full disclosure inflated price demands and triggered market breakdowns, reducing welfare for Gemini 3.1 Pro (97% to 78%), Claude Opus 5.5 (94% to 64%), and Grok 4.7 (97% to 62%). These dramatic welfare losses show that transparency can paradoxically degrade efficiency by distorting strategic incentives, undermining the assumption that more information always leads to better market outcomes.

## Context
Multi-agent LLM systems are increasingly deployed in economic simulations, game-theoretic reasoning tasks, and collaborative decision-making pipelines, where the architecture of information flow between agents is a design choice made by system builders. Prior work in mechanism design and information economics has long studied how disclosure policies shape human strategic behavior, but the rapid proliferation of LLM-based agents introduces a new class of "agents" whose responses to information are shaped by training data, instruction tuning, and architectural choices rather than rational optimization. This paper bridges empirical mechanism design with LLM evaluation, providing the first systematic experimental framework for co-optimizing model selection and information architecture in multi-agent settings.

## Implications
For practitioners building multi-agent LLM pipelines—whether for automated negotiation, market simulation, or collaborative planning—this work demonstrates that information design cannot be treated as a neutral infrastructure decision; it must be co-optimized with model selection, as the same disclosure policy can simultaneously improve one agent's performance while degrading another's. Industry teams deploying LLM agents in economic or strategic contexts should treat information granularity as a tunable system parameter subject to empirical testing rather than defaulting to maximum transparency. The findings also suggest that benchmarking LLMs in isolation is insufficient, since strategic behavior emerges from the interaction between model capabilities and the information environment they are placed in.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.07667v1)
