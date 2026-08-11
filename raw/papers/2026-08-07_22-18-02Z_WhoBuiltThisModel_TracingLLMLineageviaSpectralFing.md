---
title: Who Built This Model? Tracing LLM Lineage via Spectral Fingerprints in Weight Space
published: 2026-08-07T22:18:02Z
authors: Yiwei Chen, Bingqi Shang, Sijia Liu
url: http://arxiv.org/abs/2608.07786v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Built This Model? Tracing LLM Lineage via Spectral Fingerprints in Weight Space

## Abstract
Open-weight large language models (LLMs) are increasingly developed through complex, multi-stage pipelines, leading to intricate lineage relationships that reflect model origin, ownership, and evolution. Understanding these relationships is important for model provenance, governance, and supply-chain integrity. In this work, we investigate the notion of LLM "biometrics" (analogous to human biometrics) to ask whether LLMs exhibit intrinsic fingerprints in weight space alone, without access to input data, that reveal their origin and lineage. We formulate this as a lineage discrimination problem, distinguishing among independent-origin, same-series, and shared-base models. To characterize these relationships, we propose a unified geometric fingerprinting framework that analyzes weight matrices from two complementary perspectives: (i) spectral energy, captured by singular value distributions to encode global magnitude patterns, and (ii) subspace alignment, quantified via subspace deviations to capture directional geometry. Our analysis uncovers a clear hierarchy of structural similarity in weight space: spectral energy reliably distinguishes independently trained models and different model families, while subspace alignment enables fine-grained discrimination among closely related models, including variations in dataset scale and post-training procedures. Extensive experiments on over 110 diverse open-weight LLM pairs demonstrate that weight-space geometry provides a robust and interpretable signal for model lineage, enabling coarse-grained regime separation and fine-grained discrimination within shared-base models.

## Metadata
- **Published**: 2026-08-07T22:18:02Z
- **Authors**: Yiwei Chen, Bingqi Shang, Sijia Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07786v1)