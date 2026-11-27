---
title: One Model, Many Modes: Evolving System Prompt Ensembles for Creative Generation
url: http://arxiv.org/abs/2611.34760v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_17-29-33Z_OneModel_ManyModes_EvolvingSystemPromptEnsemblesfo.md
generated_at: 2026-11-26 22:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper addresses mode collapse in preference-aligned LLMs, where outputs concentrate on a narrow set of high-reward responses, limiting creative generation. It formalizes creative generation as a multi-objective distributional optimization problem and introduces SEPO, a training-free framework that evolves system prompts and uses greedy max-min selection to identify behaviorally distinct prompts under a quality constraint, then uniformly samples one prompt per response at inference. Across four creative generation tasks with increasing quality requirements and three open-weight models, SEPO ranks first in 8 of 12 settings on the harmonic mean of quality, diversity, and novelty.

## Key Takeaways
- Preference-aligned LLMs can collapse toward a narrow set of high-reward responses, which harms creative generation that requires quality, novelty, and diversity; existing test-time methods often emphasize diversity without ensuring individual responses are both high-quality and novel.
- SEPO is training-free: it combines prompt evolution with greedy max-min selection to find behaviorally distinct system prompts under a quality constraint, then uniformly samples one prompt per response at inference time.
- SEPO ranks first in 8 of 12 settings on the harmonic mean of quality, diversity, and novelty, while no baseline leads in more than two; on average it raises LLM-judged diversity from 1.92 to 3.43 and novelty from 1.00 to 3.34 on a 1-5 scale, with quality decreasing from 3.72 to 3.30, and expanding the optimized ensemble increases separation among prompt-conditioned response distributions.

## Context
This work sits at the intersection of alignment and creative generation: preference tuning improves reliability and perceived helpfulness but can sharpen model behavior toward a few preferred modes. That trade-off is especially visible in tasks such as writing, ideation, and brainstorming, where users want a single compelling, original response rather than merely many varied ones. SEPO targets inference-time creativity without retraining, treating system prompts as a controllable ensemble rather than a fixed instruction.

## Implications
For practitioners, SEPO offers a lightweight way to make a single open-weight model produce more diverse and novel outputs while retaining substantial quality, which is useful for creative tooling, content generation, and exploration workflows. It also suggests that ensemble size and prompt selection can be tuned to trade off separation, novelty, and quality. The main caveats are that quality decreases modestly and gains are reported through LLM-judged metrics, so human evaluation and broader task coverage remain important before deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.34760v1)
