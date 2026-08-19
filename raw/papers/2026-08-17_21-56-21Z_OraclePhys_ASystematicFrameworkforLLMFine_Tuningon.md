---
title: OraclePhys: A Systematic Framework for LLM Fine-Tuning on Structural Mechanics
published: 2026-08-17T21:56:21Z
authors: Mingyu Li, Guorui Song, Jing Lin, Haoqian Wang
url: http://arxiv.org/abs/2608.17162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OraclePhys: A Systematic Framework for LLM Fine-Tuning on Structural Mechanics

## Abstract
What a language model internalizes from fine-tuning is usually diagnosed after the fact. We make it an experimental variable. OraclePhys is a systematic fine-tuning framework with three components: OraclePhys-Bench, an exactly-graded structural-mechanics benchmark whose finite-element oracle scores every answer and counterfactual edit -- no human labels, no LLM judging; OraclePhys-30K, a supervision dataset of seven answer forms over byte-identical structure descriptions; and a controlled training study across the seven forms and three verifier roles. The study yields two findings. First, the label's answer form -- not its bit count -- causally determines what fine-tuning teaches: a ranking objective installs an out-of-distribution forward model where the untrained base sits at the guessing prior, a scalar objective at best a partial one, a boolean nothing detectable; the vector-scalar gulf survives a second physics domain, a second model family, and a paraphrased evaluation surface. Second, written or score-filtered answers install this capability, while advantage-weighted scores (GRPO) raise reward yet leave the model statistically equivalent to its start on held-out physics -- within the recipes and budgets tested -- sufficing only for routing. The trained 8B -- the first LLM on spatial structural response -- reaches the task's data-precision frontier: above a frontier LLM at zero- and 32-shot, at a specialist's level. What the label spells out about the target computation is what fine-tuning teaches; what you train on is what you route.

## Metadata
- **Published**: 2026-08-17T21:56:21Z
- **Authors**: Mingyu Li, Guorui Song, Jing Lin, Haoqian Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17162v1)