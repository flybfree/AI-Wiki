---
title: Priming Base Models for Agentic Post-Training: An Open Midtraining Recipe
url: http://arxiv.org/abs/2610.22019v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_14-58-21Z_PrimingBaseModelsforAgenticPost_Training_AnOpenMid.md
generated_at: 2026-10-15 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents an open midtraining recipe designed to prime base models for agentic post-training, bridging the gap between short-context pretraining and synthetic-data-heavy supervised fine-tuning. The authors demonstrate that training on 256K context with hundreds of billions of tokens drawn from natural software-engineering data (packed repositories, pull requests, commit histories, build logs) plus a small share of agentic traces yields substantial improvements on SWE-bench benchmarks across two Nemotron model sizes, while also improving robustness across agent harnesses.

## Key Takeaways
- Midtraining addresses a structural gap in the training pipeline: pretraining runs at short context with almost no agent interactions, while SFT data is mostly synthetic and very long SFT stages can degrade the model's later RL trainability. Midtraining sits between these stages, training at 256K context on diverse natural data to prepare the model for agentic tasks.
- On Nemotron 3.5 Lightning, 500B midtraining tokens improved SWE-bench Verified from 60.7 to 64.5, SWE-bench Multilingual from 55.8 to 62.8, and SWE-bench Pro from 32.0 to 35.5 after identical full SFT. On the larger Nemotron 3.5 Super, 280B midtraining tokens improved DeepSWE from 11.7 to 15.7 and SWE-bench Verified from 72.9 to 74.3, showing the recipe scales across model sizes.
- The authors report ablations behind the recipe and introduce an evaluation protocol built on short fixed SFT runs, because base-model proxy metrics did not correlate reliably with post-training results, highlighting the need for evaluation methods that actually predict downstream agentic performance.

## Context
Frontier model development increasingly relies on a midtraining stage between pretraining and post-training, yet little has been published about how this stage is constructed, making it a largely opaque component of state-of-the-art pipelines. This paper contributes transparency to that stage by releasing a concrete recipe, data mixture, and evaluation protocol, which is significant because the midtraining phase is where models transition from general language competence to domain-specific agentic capability. The work also underscores a broader methodological concern: traditional base-model evaluation metrics fail to predict post-training outcomes, necessitating new evaluation protocols tied to downstream agentic performance.

## Implications
For practitioners building agentic coding and software-engineering models, this recipe provides a reproducible, open blueprint for data composition, context length, and training scale that can be adapted across model sizes, reducing the need for costly trial-and-error exploration of midtraining hyperparameters. For the broader field, the finding that natural software-engineering data combined with a small share of agentic traces outperforms purely synthetic SFT data challenges prevailing assumptions about data sourcing in post-training pipelines. The introduction of short fixed SFT runs as a proxy evaluation protocol offers a practical tool for labs to assess midtraining quality without committing to full post-training cycles, potentially accelerating iteration in frontier model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22019v1)
