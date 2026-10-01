---
title: LLM Persona Unlearning
published: 2026-09-30T14:55:52Z
authors: Kemou Li, Zhuan Shi, Qizhou Wang, Fengpeng Li, Negar Rostamzadeh, Golnoosh Farnadi, Jiantao Zhou
url: http://arxiv.org/abs/2609.39882v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM Persona Unlearning

## Abstract
Pre-training equips large language models (LLMs) with a broad repertoire of behavioral patterns associated with roles, styles, values, and goals. Post-training teaches conditional enactment and makes a helpful Assistant the default, but it does not erase alternative modes from the weights; explicit prompts can therefore elicit personas that repeatedly shape judgment, language, and action. In open-weight settings, runtime controls can be removed, motivating persona unlearning: a weight-level edit that makes a designated persona difficult to elicit and enact on unseen contexts. We introduce PersonaUnlearnBench, a model-specific paired benchmark spanning six LLMs from three families and five personas, with aligned forget/retain sets, held-out instruction paraphrases, and four-axis evaluation. The benchmark shows that standard unlearning methods cannot reliably erase the target persona without sacrificing meaningful generation or general utility. We therefore propose PaCE, which compares target and desirable responses to the same questions to locate an internal behavior direction, then trains target-prompt states away from the target mode and toward the matched desirable response. Experiments show that PaCE consistently suppresses target personas with high response quality and useful counterpart behavior, at moderate utility cost. These results establish persona unlearning as a distinct behavior-level editing problem and a practical route toward persistent control of latent LLM response policies.

## Metadata
- **Published**: 2026-09-30T14:55:52Z
- **Authors**: Kemou Li, Zhuan Shi, Qizhou Wang, Fengpeng Li, Negar Rostamzadeh, Golnoosh Farnadi, Jiantao Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39882v1)