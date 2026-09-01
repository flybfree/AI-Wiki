---
title: Hidden Threat in Synthetic Data: Covert Targeted Bias Injection through Benign Text
published: 2026-08-31T11:28:36Z
authors: Minkyung Cho, Jihyo Kim, SeungWoo Song, Junghun Yuk, Minjoon Kee, Hoyun Song, KyungTae Lim
url: http://arxiv.org/abs/2608.30619v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hidden Threat in Synthetic Data: Covert Targeted Bias Injection through Benign Text

## Abstract
Synthetic data is increasingly used to train large language models (LLMs), yet its security implications remain poorly understood. Prior work on subliminal learning suggests that models can inherit behavioral traits from seemingly unrelated training data. In this work, we investigate whether such mechanisms can be exploited to inject targeted social biases into aligned models through semantically benign synthetic data. We construct a pipeline in which a misaligned teacher model generates filtered synthetic datasets across domains such as creative writing and code generation, which are then used to fine-tune aligned student models. Our experiments show that benign-looking synthetic data can act as a covert channel for transmitting targeted biases while largely preserving the student model's general task capabilities. These results reveal a previously underexplored security risk in synthetic data-driven LLM training pipelines and highlight the need for improved safeguards. As one possible step toward this goal, we suggest that log-linearity-based scoring may provide a useful signal for screening seemingly benign synthetic data.

## Metadata
- **Published**: 2026-08-31T11:28:36Z
- **Authors**: Minkyung Cho, Jihyo Kim, SeungWoo Song, Junghun Yuk, Minjoon Kee, Hoyun Song, KyungTae Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30619v1)