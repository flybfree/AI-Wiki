---
title: Source Preference in the Wild: How LLM Agents Favor Items by Source, and How to Reduce It
url: http://arxiv.org/abs/2610.03195v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_12-10-03Z_SourcePreferenceintheWild_HowLLMAgentsFavorItemsby.md
generated_at: 2026-10-04 21:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how LLM agents exhibit systematic source preference when performing end-to-end search tasks such as product selection, hotel booking, or paper citation. Across 12 agent models and three domains, the authors demonstrate that models consistently favor items from certain sources while avoiding others, and this bias can override actual requirement satisfaction. The study identifies training-induced shortcuts and missing-information preconceptions as mechanisms driving this preference, and proposes mitigation strategies including supplying missing information and counter-preconception prompting.

## Key Takeaways
- Source preference is pervasive and consistent across models and domains: when comparing items from different sources that satisfy identical requirements at the same position, every tested model shows a stable preference for some sources and avoidance of others, with strong cross-model agreement on which sources are favored or disfavored.
- Source preference can override functional quality: an item satisfying one fewer requirement is selected approximately two-thirds of the time when it comes from a preferred source versus a dispreferred one, but almost never in the reverse scenario, meaning source identity can outweigh how well an item actually meets the user's stated needs.
- The mechanism is partially causal and partially representational: hiding source information weakens the preference, while relabeling an item with a preferred source name increases its selection rate, indicating that source identity itself acts as a shortcut signal. Training that rewards better items can entrench a source as a proxy for quality, and missing information triggers preconceptions about unfamiliar sources. Providing missing information or using prompts that counteract these preconceptions measurably reduces the bias.

## Context
As LLM agents increasingly serve as autonomous decision-makers in consumer and academic workflows, their internal selection heuristics directly shape what users encounter and which platforms gain visibility. This paper addresses a gap in understanding how agent behavior is influenced not just by item quality but by the identity of the source providing the item, a factor that existing evaluation frameworks largely overlook. The finding that source preference is consistent across 12 models suggests it may stem from shared training data distributions rather than model-specific quirks, making it a systemic concern for the broader agent ecosystem.

## Implications
For practitioners deploying LLM agents in recommendation, search, and citation tasks, source preference represents a hidden fairness and quality risk that can systematically disadvantage smaller or less-represented providers regardless of actual item merit. The proposed mitigations—supplying complete source information and using counter-preconception prompts—offer practical, low-cost interventions that platform operators and agent developers can integrate into existing pipelines. For the research community, the paper highlights the need for evaluation protocols that explicitly measure and control for source bias rather than assuming agents select purely on requirement satisfaction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03195v1)
