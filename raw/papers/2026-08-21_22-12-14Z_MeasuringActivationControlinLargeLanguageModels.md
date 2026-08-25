---
title: Measuring Activation Control in Large Language Models
published: 2026-08-21T22:12:14Z
authors: Marek Mateusz Kowalski, Joshua Fonseca Rivera, Uzay Macar, David Demitri Africa
url: http://arxiv.org/abs/2608.21664v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring Activation Control in Large Language Models

## Abstract
Safe deployment of increasingly capable models will likely come to rely on latent-space monitoring as a complement to behavioral evaluations, especially when evaluation-aware models exhibit scheming or deception. However, if models can also control their own activations, deception could extend into the latent space itself. With this in mind, we introduce the Activation Controllability Benchmark to quantify the extent to which models can modulate their residual stream via natural-language instruction. Across model families and capability levels, we find that most LLMs can control the direction and magnitude of their residual stream activations with some degree of temporal resolution, though performance varies considerably across models. In simple tasks, this level of control can evade activation-based monitoring methods (including linear probes, natural language autoencoders, activation oracles, and the Jacobian lens), albeit imperfectly. These results suggest that control over the activation space itself could become a confound for monitoring as introspective capabilities increase; therefore, we recommend that frontier labs and evaluators track activation controllability in future models.

## Metadata
- **Published**: 2026-08-21T22:12:14Z
- **Authors**: Marek Mateusz Kowalski, Joshua Fonseca Rivera, Uzay Macar, David Demitri Africa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21664v1)