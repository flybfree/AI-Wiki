---
title: Memory vs. Context? Influential Factors of Factual Recall in Language Models
published: 2026-09-21T08:01:26Z
authors: Guilhem Fouilhé, Nicholas Asher, Philippe Muller
url: http://arxiv.org/abs/2609.24238v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory vs. Context? Influential Factors of Factual Recall in Language Models

## Abstract
We reproduce and stress-test the work of Yu et al. (2023), who characterize how language models (LMs) arbitrate between memorized knowledge and contradictory in-context statements. We replicate their world-capitals experiments on 31 models spanning Pythia, GPT-2, Qwen3, and Ministral families, including base and post-trained variants, and extend evaluations to five additional knowledge relation types from the ParaConflict dataset. We empirically confirm most of their original findings: larger models and higher-frequency entities tend to favor memorized answers, with substantial family-level variance. However, several conclusions do not generalize cleanly: entity-frequency effects disappear on Qwen3-14B and 32B; post-training shifts the memory-context trade-off inconsistently across families; question phrasing alone can change a model's reliance on memorized knowledge by up to 80 percentage points; and semantically unrelated prose can mimic coherent supporting context. Our results clarify where Yu et al.'s claims hold and to what extent they generalize to other prompts.

## Metadata
- **Published**: 2026-09-21T08:01:26Z
- **Authors**: Guilhem Fouilhé, Nicholas Asher, Philippe Muller
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24238v1)