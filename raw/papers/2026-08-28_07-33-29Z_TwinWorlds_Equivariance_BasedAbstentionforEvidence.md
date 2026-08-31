---
title: Twin Worlds: Equivariance-Based Abstention for Evidence-Grounded Reasoning
published: 2026-08-28T07:33:29Z
authors: Vy Nguyen, Ziqi Xu, Jeffrey Chan, Estrid He, Feng Xia, Renqiang Luo, Erik Cambria, Xiuzhen Zhang
url: http://arxiv.org/abs/2608.28018v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Twin Worlds: Equivariance-Based Abstention for Evidence-Grounded Reasoning

## Abstract
Knowledge-intensive reasoning requires Large Language Models (LLMs) to ground answers in provided evidence. When evidence is insufficient, it is desirable that models abstain rather than confidently generating unsupported answers. Existing abstention methods rely on uncertainty estimation or evidence sufficiency checks, but neither tests whether the reasoning process for generation, driven by the interaction of provided evidence and the model's internal memory parameters, is actually grounded in the evidence. A key contributing factor is that entity mentions in context activate memorised associations, causing models to generate plausible responses ungrounded in evidence. We propose Twin Worlds (TW), a framework for improving reliability in knowledge-intensive reasoning through equivariance-based abstention: unlike invariance, which requires outputs to remain unchanged, equivariance requires outputs to transform correspondingly under entity substitutions. A model grounded in the evidence should produce answers that shift consistently when entities are substituted while their relations are preserved. TW constructs multiple worlds via typed substitutions of the original input that preserve relational structure while reducing parametric priors, and uses equivariance violations as an abstention signal. Across four benchmarks and three model backbones, TW identifies when answers are not reliably grounded in the provided evidence and outperforms uncertainty- and sufficiency-based baselines.

## Metadata
- **Published**: 2026-08-28T07:33:29Z
- **Authors**: Vy Nguyen, Ziqi Xu, Jeffrey Chan, Estrid He, Feng Xia, Renqiang Luo, Erik Cambria, Xiuzhen Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28018v1)