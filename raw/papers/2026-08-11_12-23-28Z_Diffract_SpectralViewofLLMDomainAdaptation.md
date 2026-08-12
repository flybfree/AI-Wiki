---
title: Diffract: Spectral View of LLM Domain Adaptation
published: 2026-08-11T12:23:28Z
authors: Nikita Borodin, Maria Krylova, Artem Zabolotnyi, Dmitry Aspisov, Egor Shikov, Nikita Tyuplyaev, Oleg Travkin, Roman Alferov, Dmitry Vinichenko
url: http://arxiv.org/abs/2608.10850v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diffract: Spectral View of LLM Domain Adaptation

## Abstract
We study continual pre-training (CPT) as a mechanism for adapting general-purpose large language models to specialized domains: mathematics, instruction, code, and natural text. Using singular value decomposition of weight matrices, we find that CPT leaves singular value spectra largely invariant, with adaptation driven mainly by changes in singular vectors. An analysis of attention-head projection matrices reveals strong, domain-dependent head heterogeneity, which we exploit to define a head importance criterion: up to 60% of head updates can be removed without measurable quality loss. Selectively rewinding low-importance heads to their pre-trained state improves benchmark accuracy by up to 4% versus the fully trained baseline. Finally, we identify domain connectivity - linear interpolation between CPT checkpoints yields smooth domain-quality interpolation without notable degradation on either domain - and release Diffract, an open-source toolkit for scalable spectral analysis of billion-parameter models.

## Metadata
- **Published**: 2026-08-11T12:23:28Z
- **Authors**: Nikita Borodin, Maria Krylova, Artem Zabolotnyi, Dmitry Aspisov, Egor Shikov, Nikita Tyuplyaev, Oleg Travkin, Roman Alferov, Dmitry Vinichenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10850v1)